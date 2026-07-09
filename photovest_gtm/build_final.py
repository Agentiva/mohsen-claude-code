import json, glob, re, csv, collections

TR="/root/.claude/projects/-home-user-mohsen-claude-code/5cdebf3a-5e31-5815-b10d-533d4e134841/tool-results/"
PLAYBOOK="Photovoltaik-Investment ohne Eigenkapital"

SEG={"6211":"Arztpraxen","6212":"Zahnarztpraxen","5411":"Rechtsanwalts-Kanzleien",
     "5412":"Steuerberater/WP","5413":"Architektur-/Ingenieurbüros","5416":"Unternehmensberatung",
     "5415":"IT-Dienstleister","333":"Maschinenbau/Fertigung","423":"Großhandel",
     "238":"Bau-/Handwerk (Elektro/SHK)","4411":"Autohäuser"}

def norm(url):
    if not url: return ""
    u=url.strip().lower()
    u=re.sub(r'^https?://','',u); u=re.sub(r'^www\.','',u)
    return u.split('/')[0].split('?')[0].strip()

# exclusion: institutional / non-personal-income-tax entities
EXC_NAME=re.compile(r'\b(e\.?\s?v\.?|verein|ggmbh|gemeinnützig|klinikum|krankenhaus|uniklinik|universitätsklinik|'
    r'universität|hochschule|stadtwerke|stadtverwaltung|landkreis|kreisverwaltung|ministerium|landesbetrieb|'
    r'sparkasse|volksbank|raiffeisenbank|genossenschaft|kassenärztliche|ärztekammer|handwerkskammer|'
    r'diakonie|caritas|rotes kreuz|malteser|johanniter|lebenshilfe|bundesagentur|jobcenter|finanzamt|'
    r'\bstiftung\b|gemeinde\b|\bag$|\bse$|\beg$|\bkgaa$)',re.I)
EXC_DOM=re.compile(r'(jameda|gelbeseiten|dasoertliche|11880|facebook|linkedin|instagram|xing|wikipedia|'
    r'google|\.gov|bund\.de|\.edu)',re.I)

seen={}; segcount=collections.Counter()
for fp in sorted(glob.glob(TR+"*apollo_mixed_companies_search*.txt")):
    try: d=json.load(open(fp))
    except: continue
    naics=[b['value'] for b in d.get('breadcrumbs',[]) if b.get('signal_field_name')=='organization_naics_codes']
    seg=SEG.get(naics[0],"Sonstige") if naics else "Sonstige"
    for key in ("accounts","organizations"):
        for it in d.get(key,[]) or []:
            name=(it.get("name") or "").strip()
            dom=norm(it.get("website_url") or it.get("primary_domain") or "")
            if not name or not dom or '.' not in dom: continue
            if dom in seen: continue
            if EXC_NAME.search(name) or EXC_DOM.search(dom): continue
            seen[dom]=(name,seg)
            segcount[seg]+=1

rows=[(n,d,s) for d,(n,s) in seen.items()]
print("Total nach Dedupe+Cleanup:",len(rows))
for s,c in segcount.most_common(): print(f"  {s:35} {c}")

# cap at 5000, keep natural mix (already balanced)
final=rows[:5000]
with open("/home/user/mohsen-claude-code/photovest_gtm/photovest_prospects.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["company_name","domain","playbook_name"])
    for n,d,s in final: w.writerow([n,d,PLAYBOOK])
print("Final CSV rows:",len(final))
