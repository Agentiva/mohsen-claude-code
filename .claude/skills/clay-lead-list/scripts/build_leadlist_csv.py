#!/usr/bin/env python3
"""
Normalisiert, dedupliziert und validiert Lead-Listen fuer den amplifa-Import.

Erzwingt EXAKT das Spaltenschema des lead_import_template - ohne die
email-Spalte (amplifa findet die E-Mails selbst):

    first_name,last_name,full_name,job_title,company,company_website,linkedin_url,location

Eingabe: eine oder mehrere CSV- oder JSON-Dateien (JSON = Liste von Objekten).
Ausgabe: eine kanonische CSV auf stdout oder via -o.

Beispiele:
    python3 build_leadlist_csv.py --mode people clay_batch1.json > leads.csv
    python3 build_leadlist_csv.py --mode company firmen.csv > firmen_leads.csv
    python3 build_leadlist_csv.py --mode people leads.csv batch2.json -o leads.csv
"""

import argparse
import csv
import json
import re
import sys

COLUMNS = [
    "first_name",
    "last_name",
    "full_name",
    "job_title",
    "company",
    "company_website",
    "linkedin_url",
    "location",
]

# Haeufige Feldnamen aus Clay/Apollo-Exporten -> Zielspalte
ALIASES = {
    "first_name": "first_name",
    "firstname": "first_name",
    "given_name": "first_name",
    "vorname": "first_name",
    "last_name": "last_name",
    "lastname": "last_name",
    "surname": "last_name",
    "family_name": "last_name",
    "nachname": "last_name",
    "full_name": "full_name",
    "fullname": "full_name",
    "name": "full_name",
    "contact_name": "full_name",
    "person_name": "full_name",
    "job_title": "job_title",
    "jobtitle": "job_title",
    "title": "job_title",
    "position": "job_title",
    "headline": "job_title",
    "role": "job_title",
    "company": "company",
    "company_name": "company",
    "companyname": "company",
    "organization": "company",
    "organization_name": "company",
    "account_name": "company",
    "firma": "company",
    "unternehmen": "company",
    "company_website": "company_website",
    "website": "company_website",
    "domain": "company_website",
    "company_domain": "company_website",
    "company_url": "company_website",
    "web": "company_website",
    "linkedin_url": "linkedin_url",
    "linkedin": "linkedin_url",
    "linkedinurl": "linkedin_url",
    "linkedin_profile": "linkedin_url",
    "person_linkedin_url": "linkedin_url",
    "company_linkedin_url": "linkedin_url",
    "profile_url": "linkedin_url",
    "location": "location",
    "city": "location",
    "country": "location",
    "geo": "location",
    "standort": "location",
}

DROPPED_KEYS = {"email", "email_address", "e_mail", "mail", "work_email", "personal_email"}


def norm_key(key):
    return re.sub(r"[^a-z0-9]+", "_", str(key).strip().lower()).strip("_")


def clean(value):
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        value = " ".join(str(v) for v in value if v)
    if isinstance(value, dict):
        return ""
    text = str(value).strip()
    if text.lower() in {"none", "null", "n/a", "na", "-", "nan", "undefined"}:
        return ""
    return re.sub(r"\s+", " ", text)


def norm_domain(value):
    """acme.com aus https://www.acme.com/de/kontakt?x=1 - ohne Schema, ohne www."""
    text = clean(value).lower()
    if not text:
        return ""
    text = re.sub(r"^[a-z]+://", "", text)
    text = re.sub(r"^www\.", "", text)
    text = text.split("/")[0].split("?")[0].split("#")[0].strip().strip(".")
    if "@" in text or "." not in text or " " in text:
        return ""
    return text


def norm_linkedin(value):
    text = clean(value)
    if not text:
        return ""
    text = re.sub(r"^[a-z]+://", "", text, flags=re.I)
    text = re.sub(r"^([a-z]{2,3}\.)?linkedin\.com", "linkedin.com", text, flags=re.I)
    if not text.lower().startswith("linkedin.com"):
        return ""
    text = text.split("?")[0].rstrip("/")
    return "https://" + text


def split_name(full):
    parts = [p for p in clean(full).split(" ") if p]
    if len(parts) < 2:
        return (parts[0] if parts else ""), ""
    return parts[0], " ".join(parts[1:])


def to_row(record, mode):
    row = {c: "" for c in COLUMNS}
    for raw_key, raw_value in record.items():
        key = norm_key(raw_key)
        if key in DROPPED_KEYS:
            continue
        target = ALIASES.get(key)
        if target and not row[target]:
            row[target] = clean(raw_value)

    row["company_website"] = norm_domain(row["company_website"])
    row["linkedin_url"] = norm_linkedin(row["linkedin_url"])

    if mode == "company":
        # Firmenliste: Personenfelder bleiben leer, Schema aber identisch.
        for field in ("first_name", "last_name", "full_name", "job_title"):
            row[field] = ""
        return row

    if not row["full_name"]:
        row["full_name"] = " ".join(p for p in (row["first_name"], row["last_name"]) if p)
    if not row["first_name"] and not row["last_name"]:
        row["first_name"], row["last_name"] = split_name(row["full_name"])
    return row


def is_valid(row, mode):
    if mode == "company":
        return bool(row["company"] and row["company_website"])
    has_person = bool(row["first_name"] or row["full_name"])
    has_anchor = bool(row["company"] or row["company_website"] or row["linkedin_url"])
    return has_person and has_anchor


def dedupe_key(row, mode):
    if mode == "company":
        return ("domain", row["company_website"].lower())
    if row["linkedin_url"]:
        return ("li", row["linkedin_url"].lower())
    anchor = row["company_website"].lower() or row["company"].lower()
    return ("name", row["full_name"].lower(), anchor)


def read_records(path):
    if path.lower().endswith(".json"):
        with open(path, encoding="utf-8-sig") as handle:
            data = json.load(handle)
        if isinstance(data, dict):
            for key in ("results", "data", "rows", "contacts", "companies", "entities"):
                if isinstance(data.get(key), list):
                    data = data[key]
                    break
            else:
                data = [data]
        return [r for r in data if isinstance(r, dict)]
    with open(path, newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("inputs", nargs="+", help="CSV- oder JSON-Dateien (Reihenfolge = Prioritaet beim Dedupe)")
    parser.add_argument("--mode", choices=["people", "company"], default="people")
    parser.add_argument("-o", "--output", help="Zieldatei (Default: stdout)")
    args = parser.parse_args()

    seen, rows = {}, []
    stats = {"gelesen": 0, "unvollstaendig": 0, "dubletten": 0}

    for path in args.inputs:
        try:
            records = read_records(path)
        except Exception as exc:  # noqa: BLE001 - Dateifehler klar melden, nicht verschlucken
            print(f"FEHLER beim Lesen von {path}: {exc}", file=sys.stderr)
            return 1
        for record in records:
            stats["gelesen"] += 1
            row = to_row(record, args.mode)
            if not is_valid(row, args.mode):
                stats["unvollstaendig"] += 1
                continue
            key = dedupe_key(row, args.mode)
            if key in seen:
                stats["dubletten"] += 1
                # Fehlende Felder aus der Dublette nachziehen statt wegwerfen.
                existing = rows[seen[key]]
                for column in COLUMNS:
                    if not existing[column] and row[column]:
                        existing[column] = row[column]
                continue
            seen[key] = len(rows)
            rows.append(row)

    handle = open(args.output, "w", newline="", encoding="utf-8") if args.output else sys.stdout
    try:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if args.output:
            handle.close()

    print(
        f"[{args.mode}] {stats['gelesen']} gelesen -> {len(rows)} sauber "
        f"({stats['dubletten']} Dubletten, {stats['unvollstaendig']} unvollstaendig verworfen)",
        file=sys.stderr,
    )
    print(f"Spalten: {','.join(COLUMNS)}  (keine email-Spalte - amplifa findet die E-Mails)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
