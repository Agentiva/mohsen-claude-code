#!/usr/bin/env python3
"""Assemble Lindner target lists from the 4 per-playbook raw CSVs.

- Reads each raw/pbXXX_*.csv (columns: company_name, domain — flexible).
- Normalizes domains (lowercase, strip scheme/www/path).
- Drops rows without a plausible domain.
- Final belt-and-suspenders exclusion pass: competitor equipment makers,
  generic non-fit industries, reference exemplars, Lindner itself.
- Dedupes by domain WITHIN each playbook.
- Emits:
    clean/<playbook>.csv         -> company_name,domain   (per playbook)
    lindner_target_companies.csv -> company_name,domain,playbook   (combined)
    review/excluded.csv          -> every dropped row + reason (nothing silent)
Prints stats to stderr.
"""
import csv
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")
CLEAN = os.path.join(BASE, "clean")
REVIEW = os.path.join(BASE, "review")
os.makedirs(CLEAN, exist_ok=True)
os.makedirs(REVIEW, exist_ok=True)

PLAYBOOKS = [
    ("pb264_private_recyclers.csv",  "Private Recyclers & Reprocessors"),
    ("pb263_municipal_waste.csv",    "Municipal & Public Waste Operators"),
    ("pb262_cement_energy_rdf.csv",  "Cement, Energy & RDF Off-takers"),
    ("pb261_wood_biomass.csv",       "Wood & Biomass Recyclers"),
]

# --- exclusions -------------------------------------------------------------
# Competitor equipment/machine makers & dealers (NOT buyers). Matched on
# name OR domain, case-insensitive substring. Kept conservative.
COMPETITOR_TOKENS = [
    "untha", "vecoplan", "komptech", "doppstadt", "weima", "metso outotec",
    "hammel recycling", "erdwich", "bhs-sonthofen", "bhs sonthofen",
    "andritz mewa", "mewa recycling", "jenz gmbh", "eggersmann", "terra select",
    "zerma", "forrec", "pallmann", "genox", "cesaro mac", "arjes", "ecostar ",
    "redwave", "steinert", "pellenc st", "lindner-recyclingtech",
    "lindner recyclingtech", "lindner reisach",
]
COMPETITOR_DOMAINS = [
    "untha.com", "vecoplan.com", "komptech.com", "doppstadt.de", "doppstadt.com",
    "weima.com", "metso.com", "hammel.de", "erdwich.com", "bhs-sonthofen.de",
    "andritz.com", "jenz.de", "f-eggersmann.de", "eggersmann.com",
    "terraselect.com", "zerma.com", "forrec.it", "pallmann.eu", "genoxtech.com",
    "cesaro.it", "arjes.de", "ecostar.eu", "redwave.com", "steinert.de",
    "pellencst.com", "lindner.com", "lindner-recyclingtech.com", "tana.fi",
    "tomra.com", "stadlerselec.com",
]
# Generic non-fit: dropped if these appear in the domain or as a clear token
# in the name. Deliberately narrow to avoid false positives.
NONFIT_TOKENS = [
    "consulting", "consultancy", "beratung", "steuerberat",
    "software", " gmbh & co. kg it", "informatik", "agentur", "werbe",
    "versicherung", "insurance", " bank ", "immobilien", "real estate",
    "rechtsanwalt", "kanzlei", "notar", "universit", "hochschule", "klinik",
    "krankenhaus", "hospital", "personaldienst", "zeitarbeit", "recruit",
    "e-mobilit", "emobilit", "autohaus", "reisen", "touristik", "hotel ",
]
# Reference exemplars — excluded from targets (already known / references).
REFERENCE_DOMAINS = {
    "neuhauser-gmbh.at", "hofmann-entsorgung.de", "knettenbrech-gurdulic.de",
    "lundstams.se", "gojer.at", "fcc-group.eu", "remondis.de", "veolia.de",
    "saubermacher.com", "kab.co.at", "fes-frankfurt.de", "linzag.at",
    "lenzing.com", "energieag.at", "holcim.com", "crh.com",
    "heidelbergmaterials.com", "cemex.de", "heizkraftwerk-altenstadt.de",
    "egger.com", "hrd-recycling.de", "swh-herbertingen.de",
}

NAME_KEYS = {"company_name", "company", "name", "unternehmen", "firma", "organization"}
DOMAIN_KEYS = {"domain", "website", "url", "webseite", "domain_name", "primary_domain"}
DOMAIN_RE = re.compile(r"^[a-z0-9]([a-z0-9\-]{0,61}[a-z0-9])?(\.[a-z0-9\-]{2,})+$")


def norm_domain(value: str) -> str:
    d = (value or "").strip().lower()
    d = re.sub(r"^https?://", "", d)
    d = re.sub(r"^www\.", "", d)
    d = d.split("/")[0].split("?")[0].split("@")[-1].strip()
    return d


def read_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        text = f.read()
    if not text.strip():
        return []
    delim = ";" if text.count(";") > text.count(",") else ","
    reader = [r for r in csv.reader(text.splitlines(), delimiter=delim) if any(c.strip() for c in r)]
    if not reader:
        return []
    header = [h.strip().lower() for h in reader[0]]
    has_header = any(h in NAME_KEYS or h in DOMAIN_KEYS for h in header)
    rows = []
    if has_header:
        ni = next((i for i, h in enumerate(header) if h in NAME_KEYS), 0)
        di = next((i for i, h in enumerate(header) if h in DOMAIN_KEYS), len(header) - 1)
        body = reader[1:]
    else:
        ni, di, body = 0, -1, reader
    for r in body:
        if len(r) <= max(ni, di if di >= 0 else 0):
            continue
        rows.append((r[ni].strip(), r[di].strip()))
    return rows


def reason_to_drop(name, domain):
    n, d = name.lower(), domain.lower()
    if not DOMAIN_RE.match(domain):
        return "invalid_domain"
    if domain in REFERENCE_DOMAINS:
        return "reference_exemplar"
    for t in COMPETITOR_DOMAINS:
        if d == t or d.endswith("." + t):
            return f"competitor_domain:{t}"
    for t in COMPETITOR_TOKENS:
        if t in n or t in d:
            return f"competitor:{t.strip()}"
    for t in NONFIT_TOKENS:
        if t in n or t in d:
            return f"nonfit:{t.strip()}"
    return None


def main():
    combined = []            # (name, domain, playbook)
    excluded = []            # (name, domain, playbook, reason)
    per_pb_counts = {}
    for fname, label in PLAYBOOKS:
        rows = read_rows(os.path.join(RAW, fname))
        seen = {}
        for name, domain in rows:
            nd = norm_domain(domain)
            name = name.strip().strip('"')
            if not nd:
                excluded.append((name, domain, label, "empty_domain"))
                continue
            reason = reason_to_drop(name, nd)
            if reason:
                excluded.append((name, nd, label, reason))
                continue
            if nd not in seen:
                seen[nd] = name or nd
        per_pb_counts[label] = len(seen)
        # per-playbook clean file
        out = os.path.join(CLEAN, fname)
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["company_name", "domain"])
            for nd, name in sorted(seen.items(), key=lambda x: x[1].lower()):
                w.writerow([name, nd])
                combined.append((name, nd, label))

    # combined master (company_name, domain, playbook)
    with open(os.path.join(BASE, "lindner_target_companies.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["company_name", "domain", "playbook"])
        for name, nd, label in sorted(combined, key=lambda x: (x[2], x[0].lower())):
            w.writerow([name, nd, label])

    # review file (nothing dropped silently)
    with open(os.path.join(REVIEW, "excluded.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["company_name", "domain", "playbook", "reason"])
        for row in excluded:
            w.writerow(row)

    # cross-playbook overlap
    from collections import Counter
    dom_pb = {}
    for name, nd, label in combined:
        dom_pb.setdefault(nd, set()).add(label)
    overlap = sum(1 for v in dom_pb.values() if len(v) > 1)

    sys.stderr.write("=== Lindner target lists assembled ===\n")
    for label in [p[1] for p in PLAYBOOKS]:
        sys.stderr.write(f"  {per_pb_counts.get(label,0):>5}  {label}\n")
    sys.stderr.write(f"  -----\n")
    sys.stderr.write(f"  {len(combined):>5}  rows in combined CSV (playbook-tagged)\n")
    sys.stderr.write(f"  {len(dom_pb):>5}  unique domains overall\n")
    sys.stderr.write(f"  {overlap:>5}  domains appearing in >1 playbook\n")
    sys.stderr.write(f"  {len(excluded):>5}  rows excluded (see review/excluded.csv)\n")


if __name__ == "__main__":
    main()
