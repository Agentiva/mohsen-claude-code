#!/usr/bin/env python3
"""Verification screen: remove competitors + suppliers-to-Lindner + non-operators.

Reads clean/pbXXX_*.csv, classifies each company by name+domain against curated
dictionaries, and writes:
  verified/pbXXX_*.csv                     -> only genuine potential BUYERS
  lindner_target_companies_verified.csv    -> combined, playbook-tagged
  review/flagged_suspects.csv              -> everything removed + why (auditable)

Design:
- competitor  = maker/dealer of shredders/sorting/recycling machinery (won't buy).
- supplier    = would SELL to Lindner (machine builders, plant engineering,
                hydraulics/drives/conveyor/steel-fab/automation/wear-parts...).
- non_operator= association/institute/media/fair/consultancy/finance/edu.
- OPERATOR-keyword exemption protects real waste/wood/energy operators (e.g.
  'Abfallzweckverband') from the non_operator rule. Competitor/supplier rules
  still apply even to operator-named firms (a 'Recycling Maschinenbau' is a maker).
"""
import csv, os, re, sys
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
CLEAN = os.path.join(BASE, "clean")
VER = os.path.join(BASE, "verified")
REVIEW = os.path.join(BASE, "review")
os.makedirs(VER, exist_ok=True)
os.makedirs(REVIEW, exist_ok=True)

PLAYBOOKS = [
    ("pb264_private_recyclers.csv",  "Private Recyclers & Reprocessors"),
    ("pb263_municipal_waste.csv",    "Municipal & Public Waste Operators"),
    ("pb262_cement_energy_rdf.csv",  "Cement, Energy & RDF Off-takers"),
    ("pb261_wood_biomass.csv",       "Wood & Biomass Recyclers"),
]

# --- (a) COMPETITORS: shredder / sorting / recycling / chipper equipment makers
COMPETITOR = [
    "untha", "vecoplan", "komptech", "doppstadt", "weima", "andritz",
    "hammel", "erdwich", "bhs-sonthofen", "bhs sonthofen", "jenz",
    "eggersmann", "terra select", "terraselect", "zerma", "forrec", "pallmann",
    "genox", "cesaro", "arjes", "ecostar", "redwave", "steinert", "pellenc",
    "tomra", "sesotec", "bollegraaf", "backhus", "precimeca", "granutech",
    "ssi shredding", "ssi-shredding", "gep ecotech", "m&j recycling",
    "mj-recycling", "heizohack", "mus-max", "musmax", "eschlböck", "eschlboeck",
    "pezzolato", "bruks", "siwertell", "kesla", "junkkari", "hartner",
    "stadler anlagen", "stadlerselec", "w-stadler", "lindner-recyclingtech",
    "lindner recyclingtech", "lindner reisach", "retech recycling",
    "vermeer", "morbark", "rotochopper", "diamond z", "peterson pacific",
    "willibald", "teuwsen", "terex ecotec", "untha shredding",
    # forestry / wood machinery makers (would sell to, or compete with, Lindner)
    "uniforest", "tajfun", "pfanzelt", "krpan", "binderberger", "forsttechnik",
    "ledinek", "springer maschinen",
]
COMPETITOR_DOMAINS = [
    "untha.com", "vecoplan.com", "vecoplan.de", "komptech.com", "doppstadt.de",
    "doppstadt.com", "weima.com", "metso.com", "hammel.de", "erdwich.com",
    "bhs-sonthofen.de", "andritz.com", "jenz.de", "eggersmann.com",
    "f-eggersmann.de", "terraselect.com", "zerma.com", "forrec.it",
    "pallmann.eu", "genoxtech.com", "cesaro.it", "arjes.de", "ecostar.eu",
    "redwave.com", "steinert.de", "pellencst.com", "tomra.com", "sesotec.com",
    "bollegraaf.com", "backhus.com", "lindner.com", "lindner-recyclingtech.com",
    "tana.fi", "stadlerselec.com", "bano.it", "hartner.at", "willibald-gmbh.de",
]

# --- (b) SUPPLIERS to Lindner: build/sell machinery, components or engineering
SUPPLIER = [
    "maschinenbau", "maschinenfabrik", "sondermaschinen", "anlagenbau",
    "apparatebau", "fördertechnik", "foerdertechnik", "antriebstechnik",
    "hydraulik", "hydraulics", "hydraulic ", "getriebe", "gearbox",
    "automatisierung", "steuerungstechnik", "schaltanlagen", "sensorik",
    "wälzlager", "stahlbau", "metallbau", "schweißtechnik", "schweisstechnik",
    "blechbearbeitung", "engineering", "engineers", "ingenieur", "ingénierie", "ingenjörs",
    "gebrauchtmaschinen", "maschinenhandel", "used machinery", "machinery trade",
    "conveyor", "conveying", "screening technology", "separation technology",
    "verschleißtechnik", "hartmetall", "hardfacing", "schneidwerkzeug",
    "antriebe", "elektromotoren", "elektrotechnik", "prozessleittechnik",
    "waagen", "wägetechnik", "wiegetechnik",
]
# --- (c) NON-OPERATORS (only if NOT operator-exempt)
NON_OPERATOR = [
    "verband", "verein", " e.v", "e. v.", "gewerkschaft", "association",
    "federation", "kammer", "chamber", " ihk", "ahk ", "cluster",
    "institut", "institute", "fraunhofer", "universit", "hochschule",
    "fachhochschule", "akademie", "academy", "forschung", "ministerium",
    "ministry", "consult", "beratung", "software", "informatik", "verlag",
    "messe", "exhibition", "sparkasse", "versicherung", "insurance",
    "immobilien", "steuerberat", "rechtsanwalt", "kanzlei",
]
# Operator-positive keywords -> exempt from NON_OPERATOR rule (protect real
# waste/wood/energy operators such as Abfallzweckverbände).
OPERATOR_POS = [
    "abfall", "entsorg", "recycl", "wertstoff", "kompost", "kompogas",
    "waste", "renov", "avfall", "affald", "jäte", "jate", "komun", "cistoca",
    "čistoča", "čistoća", "cistoća", "umwelt", "environ", "biomasse", "biomass",
    "pellet", "holz", "wood", "timber", "säge", "sawmill", "sågverk", "span",
    "spanplatte", "particle", "mdf", "osb", "zement", "cement", "ciment",
    "kalk", "lime", "kraftwerk", "power", "energie", "energy", "wärme", "varme",
    "värme", "heat", "fernwärme", "rdf", "srf", "ebs", "brennstoff", "fuel",
    "incinerat", "verbrennung", "schrott", "scrap", "metallrecycl", "metall-recycl",
    "kunststoff", "plastic", "papier", "paper", "kartonage", "altpapier",
    "altholz", "stadtwerke", "forsyning", "technische dienste", "technické služby",
    "reinigung", "recovery", "resource", "circular",
    # waste-operator keywords (protect genuine waste Zweckverbände / plants)
    "müll", "muell", "kva", "kehricht", "abfuhr", "deponie", "reststoff",
    "sonderabfall", "wertstoffhof", "verwertung", "sammel", "sammlung",
    "bauschutt", "grünschnitt", "gruenschnitt", "biogas", "klärschlamm",
]


def norm(s):
    return (s or "").lower()


def classify(name, domain):
    n, d = norm(name), norm(domain)
    hay = n + " " + d
    # competitor by domain (exact/suffix)
    for cd in COMPETITOR_DOMAINS:
        if d == cd or d.endswith("." + cd):
            return "competitor", f"domain:{cd}"
    for t in COMPETITOR:
        if t in hay:
            return "competitor", t
    for t in SUPPLIER:
        if t in hay:
            return "supplier_to_lindner", t
    op_exempt = any(k in hay for k in OPERATOR_POS)
    if not op_exempt:
        for t in NON_OPERATOR:
            if t in hay:
                return "non_operator", t.strip()
    return "keep", ""


def read_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        r = list(csv.reader(f))
    if not r:
        return []
    body = r[1:] if r and r[0] and r[0][0].strip().lower() in {"company_name", "company", "name"} else r
    out = []
    for row in body:
        if len(row) >= 2 and row[0].strip():
            out.append((row[0].strip(), row[1].strip()))
    return out


def main():
    flagged = []
    combined_keep = []
    stats = {}
    for fname, label in PLAYBOOKS:
        rows = read_rows(os.path.join(CLEAN, fname))
        keep, cat_counts = [], Counter()
        for name, domain in rows:
            cat, term = classify(name, domain)
            if cat == "keep":
                keep.append((name, domain))
            else:
                cat_counts[cat] += 1
                flagged.append((name, domain, label, cat, term))
        stats[label] = (len(rows), len(keep), cat_counts)
        with open(os.path.join(VER, fname), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["company_name", "domain"])
            for name, domain in sorted(keep, key=lambda x: x[0].lower()):
                w.writerow([name, domain]); combined_keep.append((name, domain, label))

    with open(os.path.join(BASE, "lindner_target_companies_verified.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["company_name", "domain", "playbook"])
        for name, domain, label in sorted(combined_keep, key=lambda x: (x[2], x[0].lower())):
            w.writerow([name, domain, label])

    with open(os.path.join(REVIEW, "flagged_suspects.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["company_name", "domain", "playbook", "category", "matched_term"])
        for row in sorted(flagged, key=lambda x: (x[3], x[2], x[0].lower())):
            w.writerow(row)

    sys.stderr.write("=== Verification screen ===\n")
    tot_in = tot_keep = 0
    for _, label in PLAYBOOKS:
        n_in, n_keep, cc = stats[label]
        tot_in += n_in; tot_keep += n_keep
        detail = ", ".join(f"{k}:{v}" for k, v in cc.items()) or "none"
        sys.stderr.write(f"  {label}\n    in={n_in}  keep={n_keep}  removed={n_in-n_keep}  ({detail})\n")
    all_cat = Counter(x[3] for x in flagged)
    sys.stderr.write(f"  -----\n  TOTAL in={tot_in}  keep={tot_keep}  removed={len(flagged)}  {dict(all_cat)}\n")


if __name__ == "__main__":
    main()
