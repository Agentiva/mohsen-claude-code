import json, glob, re, csv, collections
TR="/root/.claude/projects/-home-user-mohsen-claude-code/5cdebf3a-5e31-5815-b10d-533d4e134841/tool-results/"
PLAYBOOK="Photovoltaik-Investment ohne Eigenkapital"
SEG={"6211":"Arztpraxen","6212":"Zahnarztpraxen","5411":"Rechtsanwalts-Kanzleien",
     "5412":"Steuerberater/WP","5413":"Architektur-/Ingenieurbüros","5416":"Unternehmensberatung",
     "5415":"IT-Dienstleister","333":"Maschinenbau/Fertigung","423":"Großhandel",
     "238":"Bau-/Handwerk (Elektro/SHK)","4411":"Autohäuser"}
def norm(u):
    if not u: return ""
    u=u.strip().lower(); u=re.sub(r'^https?://','',u); u=re.sub(r'^www\.','',u)
    return u.split('/')[0].split('?')[0].strip()
EXC_NAME=re.compile(r'\b(e\.?\s?v\.?|verein|ggmbh|gemeinnützig|klinikum|krankenhaus|uniklinik|universitätsklinik|'
    r'universität|hochschule|stadtwerke|stadtverwaltung|landkreis|kreisverwaltung|ministerium|landesbetrieb|'
    r'sparkasse|volksbank|raiffeisenbank|genossenschaft|kassenärztliche|ärztekammer|handwerkskammer|'
    r'diakonie|caritas|rotes kreuz|malteser|johanniter|lebenshilfe|bundesagentur|jobcenter|finanzamt|'
    r'\bstiftung\b|gemeinde\b|\bag$|\bse$|\beg$|\bkgaa$)',re.I)
EXC_DOM=re.compile(r'(jameda|gelbeseiten|dasoertliche|11880|facebook|linkedin|instagram|xing|wikipedia|google|\.gov|bund\.de|\.edu)',re.I)

comb=set(l.strip() for l in open("combined_exclude.txt") if l.strip())
# load kept 4005
final=[]
for r in list(csv.reader(open("kept_4005.csv")))[1:]:
    final.append((r[0],r[1]))
have=set(d for _,d in final)

new=[]; segc=collections.Counter()
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
            if dom in comb or dom in have: continue
            if EXC_NAME.search(name) or EXC_DOM.search(dom): continue
            have.add(dom); new.append((name,dom)); segc[seg]+=1
print("new net-new candidates from topup:",len(new))
for s,c in segc.most_common(): print(f"  {s:32} {c}")
# combine up to 5000
final += new
final = final[:5000]
with open("photovest_prospects_final.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["company_name","company_domain","playbook_name"])
    for n,dm in final: w.writerow([n,dm,PLAYBOOK])
print("FINAL rows:",len(final))
