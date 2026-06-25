import json,glob,csv,re
from collections import Counter
TR="/root/.claude/projects/-home-user-mohsen-claude-code/148a4ed2-11a6-5a47-a7f1-b2067f27a0ce/tool-results"
WORK="/home/user/mohsen-claude-code/amplifa_lists"

NMAP={
 ('3331','3332','3335'):"Allgemeine Industrie",
 ('236','237','238'):"Bau",
 ('321','322'):"Holz & Papier",
 ('33311','42382'):"Agrar & Landmaschinen",
 ('311','312'):"Lebensmittel & Getraenke",
 ('3261','3262'):"Kunststoff",
 ('3364',):"Luft- & Raumfahrt",
 ('3254','33911','33912'):"Pharma",
 ('32221','32611','32613'):"Verpackung",
}
KMAP={
 'agricultural machinery':"Agrar & Landmaschinen",
 'injection molding':"Kunststoff",
 'aerospace':"Luft- & Raumfahrt",
 'packaging':"Verpackung",
 'woodworking':"Holz & Papier",
}
# dedupe priority: specialised first, general last
PRIO=["Agrar & Landmaschinen","Luft- & Raumfahrt","Pharma","Kunststoff","Verpackung",
      "Holz & Papier","Lebensmittel & Getraenke","Bau","Allgemeine Industrie"]
PR={b:i for i,b in enumerate(PRIO)}

BAD=re.compile(r'\b(consulting|beratung|software|saas|agentur|agency|versicherung|insurance|immobilien|kanzlei|hotel|verein|e\.?v\.?|hochschule|university|universit|klinik|clinic|recruiting|personalvermittl|steuerberat)\b',re.I)
# aerospace noise (airlines/airports/travel/MRO-as-airline)
AERO_NOISE=re.compile(r'\b(airline|airlines|airways|airport|flughafen|travel|reise|charter|fluggesellschaft|touris)\b',re.I)

def nd(d):
    if not d: return ""
    d=d.strip().lower(); d=re.sub(r'^https?://','',d); d=re.sub(r'^www\.','',d)
    return d.split('/')[0].strip()

rows=[]
for f in glob.glob(TR+'/mcp-Apollo*companies*.txt'):
    try: d=json.load(open(f))
    except: continue
    sig={}
    for b in d.get('breadcrumbs',[]):
        sig.setdefault(b.get('signal_field_name'),[]).append(b.get('value'))
    naics=tuple(sig.get('organization_naics_codes',[]))
    kws=sig.get('q_organization_keyword_tags',[])
    br=NMAP.get(naics)
    if not br and kws:
        br=KMAP.get(kws[0])
    if not br: 
        continue
    items=d.get('accounts') or d.get('organizations') or []
    for it in items:
        name=(it.get('name') or '').strip(); dom=nd(it.get('primary_domain') or it.get('website_url'))
        if not name or not dom or BAD.search(name): continue
        if br=="Luft- & Raumfahrt" and AERO_NOISE.search(name): continue
        rows.append((br,name,dom))

# manual wood/paper inline tail
rows += [("Holz & Papier","Fischer Papier AG","fischerpapier.ch"),
 ("Holz & Papier","Eduard Ehemann GmbH","ehemann-verpackungen.de"),
 ("Holz & Papier","Seyfert GmbH","seyfert.de"),
 ("Holz & Papier","H.O.Persiehl (GmbH & Co.) KG","persiehl.de")]

# priority dedupe by domain
best={}
for br,name,dom in rows:
    if dom not in best or PR[br]<PR[best[dom][0]]:
        best[dom]=(br,name,dom)
final=list(best.values())
# sort by branche then name
final.sort(key=lambda r:(PR[r[0]], r[1].lower()))
with open(WORK+'/amplifa_unternehmen.csv','w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['branche','company_name','domain'])
    for r in final: w.writerow(r)
c=Counter(b for b,_,_ in final)
print("RAW rows:",len(rows)," UNIQUE:",len(final))
for b in PRIO: print(f"  {b}: {c.get(b,0)}")
