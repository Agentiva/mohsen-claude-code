#!/usr/bin/env python3
"""Generiert pro Person/Domain exakt 5 E-Mail-Varianten nach amplifa-Regeln.

Input: CSV oder lose Liste, pro Zeile "Vorname, Nachname, Domain".
Trennzeichen Komma oder Semikolon; eine optionale Header-Zeile wird erkannt.
Output (stdout): CSV mit Spalten email,first_name,last_name,domain.
"""

import sys
import csv

TRANSLIT = {
    "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
    "á": "a", "à": "a", "â": "a", "ã": "a", "å": "a",
    "é": "e", "è": "e", "ê": "e", "ë": "e",
    "í": "i", "ì": "i", "î": "i", "ï": "i",
    "ó": "o", "ò": "o", "ô": "o", "õ": "o",
    "ú": "u", "ù": "u", "û": "u",
    "ç": "c", "ñ": "n",
}


def normalize(part: str) -> str:
    """Kleinschreiben, transliterieren, Trenner entfernen."""
    s = part.strip().lower()
    out = []
    for ch in s:
        if ch in TRANSLIT:
            out.append(TRANSLIT[ch])
        elif ch.isalnum():
            out.append(ch)
        # Leerzeichen, Bindestrich, Apostroph etc. fallen weg
    return "".join(out)


def first_token(name: str) -> str:
    """Nur den ersten Vornamen verwenden."""
    return name.strip().split()[0] if name.strip() else ""


def variants(first_raw: str, last_raw: str, domain: str):
    v = normalize(first_token(first_raw))
    n = normalize(last_raw)  # normalize zieht mehrteilige Nachnamen zusammen
    if not v or not n or not domain:
        return []
    initial = v[0]
    locals_ = [
        f"{v}.{n}",      # vorname.nachname
        f"{initial}.{n}",  # v.nachname
        f"{initial}{n}",   # vnachname
        f"{n}.{v}",      # nachname.vorname
        f"{n}",          # nachname
    ]
    return [f"{lp}@{domain}" for lp in locals_]


def parse_rows(path: str):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read()
    delimiter = ";" if sample.count(";") > sample.count(",") else ","
    reader = csv.reader(sample.splitlines(), delimiter=delimiter)
    rows = [r for r in reader if any(cell.strip() for cell in r)]
    if rows and any(h.strip().lower() in {"vorname", "first_name", "firstname", "name"} for h in rows[0]):
        rows = rows[1:]  # Header überspringen
    return rows


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: generate_mailboxes.py <input-datei>")
    rows = parse_rows(sys.argv[1])
    writer = csv.writer(sys.stdout)
    writer.writerow(["email", "first_name", "last_name", "domain"])
    skipped = []
    for i, row in enumerate(rows, 1):
        if len(row) < 3:
            skipped.append((i, row))
            continue
        first_raw, last_raw, domain = row[0].strip(), row[1].strip(), row[2].strip().lower()
        emails = variants(first_raw, last_raw, domain)
        if not emails:
            skipped.append((i, row))
            continue
        for e in emails:
            writer.writerow([e, first_raw, last_raw, domain])
    if skipped:
        sys.stderr.write(f"WARNUNG: {len(skipped)} Zeile(n) übersprungen (unvollständig): {skipped}\n")


if __name__ == "__main__":
    main()
