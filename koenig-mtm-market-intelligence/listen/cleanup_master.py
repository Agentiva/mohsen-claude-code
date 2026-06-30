#!/usr/bin/env python3
import csv, re, os

SEGMENTS = [
    ("Luft- & Raumfahrt / Defense", "aerospace.csv"),
    ("Antrieb & E-Mobilität", "antrieb_emobilitaet.csv"),
    ("Medizintechnik", "medizintechnik.csv"),
    ("Maschinen- & Werkzeugbau", "robotik_placeholder"),  # fixed below
]
# explicit order (priority for cross-dedupe)
ORDER = [
    ("Luft- & Raumfahrt / Defense", "aerospace.csv"),
    ("Antrieb & E-Mobilität", "antrieb_emobilitaet.csv"),
    ("Medizintechnik", "medizintechnik.csv"),
    ("Maschinen- & Werkzeugbau", "maschinenbau.csv"),
    ("Robotik & Antriebstechnik", "robotik_antriebstechnik.csv"),
    ("Windkraft & Schwerindustrie", "windkraft_schwerindustrie.csv"),
]

# cheap firmographic exclusion (clear non-fitters by name/domain)
BLOCK = re.compile(r'\b(consulting|consultant|berat(?:ung|er)|software|saas|saas|it[- ]services|digital agency|agentur|agency|marketing|werbung|recruit|staffing|personal(?:dienst|berat)|zeitarbeit|university|universit|hochschule|klinik|hospital|insurance|versicherung|\bbank\b|immobil|real estate|kanzlei|law firm|rechtsanwalt|notar|hotel|reise|travel|airline|airways|airport|flughafen|verein|verband|e\.?v\.?|foundation|stiftung|ngo|\bmedia\b|verlag|publishing|e-?commerce|webshop|online shop)\b', re.I)

def load(path):
    if not os.path.exists(path): return []
    out=[]
    with open(path, encoding='utf-8') as f:
        r=csv.reader(f)
        for i,row in enumerate(r):
            if i==0 or len(row)<2: continue
            name=row[0].strip(); dom=row[1].strip().lower()
            if name and dom: out.append((name,dom))
    return out

seen=set()
master=[]
seg_counts={}
for seg, path in ORDER:
    rows=load(path)
    kept=[]
    for name,dom in rows:
        if BLOCK.search(name) or BLOCK.search(dom):
            continue
        if dom in seen:
            continue
        seen.add(dom); kept.append((name,dom))
        master.append((name,dom,seg))
    seg_counts[seg]=len(kept)
    # rewrite cleaned per-segment file (kept rows only, but per-segment we want ALL its fits even if dup elsewhere)
# write per-segment cleaned (independent: include a row even if it appears in earlier segment, for per-playbook completeness)
for seg, path in ORDER:
    rows=load(path)
    outp=path.replace('.csv','_clean.csv')
    with open(outp,'w',encoding='utf-8') as f:
        f.write("company_name,domain\n")
        s2=set()
        c=0
        for name,dom in rows:
            if BLOCK.search(name) or BLOCK.search(dom): continue
            if dom in s2: continue
            s2.add(dom)
            n2='"'+name.replace('"','""')+'"' if (',' in name or '"' in name) else name
            f.write(f"{n2},{dom}\n"); c+=1
        print(f"{seg}: clean={c}")

with open('master_alle_segmente.csv','w',encoding='utf-8') as f:
    f.write("company_name,domain,playbook\n")
    for name,dom,seg in master:
        n2='"'+name.replace('"','""')+'"' if (',' in name or '"' in name) else name
        f.write(f"{n2},{dom},{seg}\n")
print("MASTER unique (cross-dedupe):", len(master))
