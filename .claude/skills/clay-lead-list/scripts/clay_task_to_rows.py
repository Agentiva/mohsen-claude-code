#!/usr/bin/env python3
"""
Liest eine (meist auf Platte ausgelagerte) Clay-`get-task-context`-Antwort und
macht daraus importfertige Zeilen fuer build_leadlist_csv.py.

Deckt beide Clay-Formen ab:
  * run_subroutine_direct "Find People at Company" (Batch, 10 Personen/Firma)
  * find-and-enrich-contacts-at-company (gefiltert, mit Stadt)

Der Titelfilter matcht auf WORTGRENZEN. Ein nacktes Substring-Match ist hier ein
echter Fehler: "cto" steckt in "Dire*cto*r", "gis" in "Lo*gis*tik".

    python3 clay_task_to_rows.py task.json --titles titles.txt -o rows.json
    python3 clay_task_to_rows.py task.json --titles titles.txt --stats-only
"""

import argparse
import json
import re
import sys
from collections import Counter

COUNTRY = {"de": "Germany", "at": "Austria", "ch": "Switzerland"}


def load_titles(path):
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.split("#")[0].strip()
        if line:
            out.append(line.lower())
    return out


def matcher(titles):
    """Wortgrenzen-Regex; mehrwortige Begriffe duerfen beliebigen Trenner haben."""
    parts = []
    for t in titles:
        words = [re.escape(w) for w in re.split(r"\s+", t) if w]
        if words:
            parts.append(r"\b" + r"[\s\-/]*".join(words) + r"\b")
    return re.compile("|".join(parts), re.IGNORECASE) if parts else None


def people_from_subroutine(entity):
    for enr in (entity.get("enrichments") or {}).values():
        value = enr.get("value")
        if not value:
            continue
        try:
            block = json.loads(value)
        except (TypeError, ValueError):
            continue
        for key in block:
            if "people" in (block[key] or {}):
                for p in block[key]["people"] or []:
                    yield {
                        "first_name": p.get("firstName", ""),
                        "last_name": p.get("lastName", ""),
                        "full_name": p.get("fullName", ""),
                        "job_title": p.get("jobTitle", ""),
                        "company": p.get("companyName", ""),
                        "company_website": p.get("companyDomain", ""),
                        "linkedin_url": p.get("linkedInUrl", ""),
                        "location": COUNTRY.get((p.get("country") or "").lower(), ""),
                    }


def people_from_contacts(doc):
    for c in doc.get("contacts") or []:
        yield {
            "first_name": "",
            "last_name": "",
            "full_name": c.get("name", ""),
            "job_title": c.get("latest_experience_title", ""),
            "company": c.get("latest_experience_company", ""),
            "company_website": c.get("domain", ""),
            "linkedin_url": c.get("url", ""),
            "location": c.get("location_name", ""),
        }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="get-task-context JSON-Dateien")
    ap.add_argument("--titles", required=True, help="Datei mit ICP-Titelbegriffen, einer pro Zeile")
    ap.add_argument("--exclude", help="Datei mit Negativ-Titelbegriffen (Finanz-/HR-/Immobilien-Rollen raus)")
    ap.add_argument("--countries", help="Komma-Liste erlaubter Laender, z. B. 'Germany,Austria,Switzerland'. "
                                        "Filtert Treffer internationaler Konzerne ausserhalb des Zielmarkts.")
    ap.add_argument("--jsonl", action="store_true", help="Eingaben sind bereits Zeilen-JSON (eine Zeile = ein Datensatz)")
    ap.add_argument("-o", "--output", help="Ziel-JSON (Default: stdout)")
    ap.add_argument("--stats-only", action="store_true", help="nur Statistik auf stderr, kein Output")
    args = ap.parse_args()

    rx = matcher(load_titles(args.titles))
    rx_not = matcher(load_titles(args.exclude)) if args.exclude else None
    countries = [c.strip().lower() for c in args.countries.split(",")] if args.countries else None
    raw, incomplete, no_result = [], 0, 0

    for path in args.inputs:
        if args.jsonl:
            raw += [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
            continue
        doc = json.load(open(path, encoding="utf-8"))
        if doc.get("isComplete") is False:
            incomplete += 1
            print(f"WARNUNG: {path} ist isComplete=false - Clay war beim Abruf noch nicht fertig. "
                  f"Nochmal get-task-context aufrufen, sonst fehlen Firmen.", file=sys.stderr)
        for entity in doc.get("entities") or []:
            got = list(people_from_subroutine(entity))
            if not got:
                no_result += 1
            raw += got
        raw += list(people_from_contacts(doc))

    hits = [r for r in raw if rx and rx.search(r.get("job_title") or "")]
    dropped_neg = dropped_geo = 0
    if rx_not:
        before = len(hits)
        hits = [r for r in hits if not rx_not.search(r.get("job_title") or "")]
        dropped_neg = before - len(hits)
    if countries:
        before = len(hits)
        hits = [r for r in hits
                if not (r.get("location") or "")
                or any(c in (r.get("location") or "").lower() for c in countries)]
        dropped_geo = before - len(hits)
    quote = len(hits) / len(raw) * 100 if raw else 0
    print(f"Rohpersonen: {len(raw)} | ICP-Treffer: {len(hits)} ({quote:.0f}%) | "
          f"per Negativliste verworfen: {dropped_neg} | ausserhalb Zielmarkt: {dropped_geo} | "
          f"Firmen ohne Treffer: {no_result}" + (f" | UNVOLLSTAENDIGE Tasks: {incomplete}" if incomplete else ""),
          file=sys.stderr)
    print("Top-Titel: " + "; ".join(f"{c}x {t}" for t, c in Counter(r.get("job_title") for r in hits).most_common(8)),
          file=sys.stderr)

    if args.stats_only:
        return 0
    out = json.dumps(hits, ensure_ascii=False, indent=1)
    if args.output:
        open(args.output, "w", encoding="utf-8").write(out)
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
