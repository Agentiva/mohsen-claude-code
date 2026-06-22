#!/usr/bin/env python3
"""Merge & dedupe von Unternehmenslisten (Name + Domain).

Verwendung:
    merge_dedupe.py master.csv [neu1.csv neu2.csv ...] > merged.csv

- Erste Datei = bisheriger Stand (master). Weitere = neue Batches.
- Dedupe nach normalisierter Domain (www./Schema/Pfad entfernt, lowercase).
- Output (stdout): saubere CSV mit Spalten company_name,domain.
- Statistik (stderr): Gesamtzahl eindeutig + wie viele NEU gegenüber master.

Akzeptiert flexible Eingabespalten: erkennt Name- und Domain-Spalte
anhand der Header; ohne Header werden Spalte 1 = Name, letzte = Domain
angenommen.
"""

import sys
import csv
import re

NAME_KEYS = {"company_name", "company", "name", "unternehmen", "firma", "organization"}
DOMAIN_KEYS = {"domain", "website", "url", "webseite", "domain_name", "primary_domain"}


def norm_domain(value: str) -> str:
    d = (value or "").strip().lower()
    d = re.sub(r"^https?://", "", d)
    d = re.sub(r"^www\.", "", d)
    d = d.split("/")[0].split("?")[0].strip()
    return d


def read_rows(path: str):
    with open(path, newline="", encoding="utf-8-sig") as f:
        text = f.read()
    if not text.strip():
        return []
    delim = ";" if text.count(";") > text.count(",") else ","
    reader = list(csv.reader(text.splitlines(), delimiter=delim))
    reader = [r for r in reader if any(c.strip() for c in r)]
    if not reader:
        return []
    header = [h.strip().lower() for h in reader[0]]
    has_header = any(h in NAME_KEYS or h in DOMAIN_KEYS for h in header)
    rows = []
    if has_header:
        ni = next((i for i, h in enumerate(header) if h in NAME_KEYS), 0)
        di = next((i for i, h in enumerate(header) if h in DOMAIN_KEYS), len(header) - 1)
        for r in reader[1:]:
            if len(r) <= max(ni, di):
                continue
            rows.append((r[ni].strip(), r[di].strip()))
    else:
        for r in reader:
            if len(r) < 2:
                continue
            rows.append((r[0].strip(), r[-1].strip()))
    return rows


def main():
    # Auf Windows schreibt sys.stdout sonst in cp1252, waehrend read_rows als
    # UTF-8 liest -> beim naechsten Merge crasht es an Umlauten. Zudem verdoppelt
    # der Text-Mode die Zeilenenden (csv \r\n -> \r\r\n) und erzeugt Leerzeilen.
    # newline="" + UTF-8 erzwingen behebt beides.
    try:
        sys.stdout.reconfigure(encoding="utf-8", newline="")
    except (AttributeError, ValueError):
        pass
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    if len(sys.argv) < 2:
        sys.exit("Usage: merge_dedupe.py master.csv [neu.csv ...]")

    seen = {}
    master_domains = set()
    for idx, path in enumerate(sys.argv[1:]):
        try:
            rows = read_rows(path)
        except FileNotFoundError:
            sys.stderr.write(f"WARNUNG: Datei nicht gefunden, übersprungen: {path}\n")
            continue
        for name, domain in rows:
            nd = norm_domain(domain)
            if not nd:
                continue
            if idx == 0:
                master_domains.add(nd)
            if nd not in seen:
                seen[nd] = name or nd

    writer = csv.writer(sys.stdout)
    writer.writerow(["company_name", "domain"])
    for nd, name in sorted(seen.items(), key=lambda x: x[1].lower()):
        writer.writerow([name, nd])

    total = len(seen)
    neu = len([d for d in seen if d not in master_domains])
    sys.stderr.write(f"Eindeutige Unternehmen gesamt: {total} | davon neu gegenüber master: {neu}\n")


if __name__ == "__main__":
    main()
