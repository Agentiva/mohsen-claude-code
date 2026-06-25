import json,glob,sys,csv,os,re
TR="/root/.claude/projects/-home-user-mohsen-claude-code/148a4ed2-11a6-5a47-a7f1-b2067f27a0ce/tool-results"
WORK="/home/user/mohsen-claude-code/amplifa_lists"

# cheap exclusion keywords (clearly no-fit service/IT/etc.)
BAD=re.compile(r'\b(consulting|beratung|software|saas|agentur|agency|versicherung|insurance|immobilien|real estate|kanzlei|law|hotel|verein|e\.?v\.?|hochschule|university|universit|klinik|clinic|recruiting|personalvermittl|steuerberat|wirtschaftspr)\b', re.I)

def norm_domain(d):
    if not d: return ""
    d=d.strip().lower()
    d=re.sub(r'^https?://','',d)
    d=re.sub(r'^www\.','',d)
    d=d.split('/')[0].strip()
    return d

def extract(files):
    rows=[]
    for f in files:
        try:
            d=json.load(open(f))
        except Exception as e:
            print("ERR",f,e); continue
        items=[]
        for k in ('accounts','organizations'):
            if d.get(k): items+=d[k]
        for it in items:
            name=(it.get('name') or '').strip()
            dom=norm_domain(it.get('primary_domain') or it.get('website_url'))
            if not name or not dom: continue
            if BAD.search(name): continue
            rows.append((name,dom))
    return rows

if __name__=="__main__":
    branche=sys.argv[1]
    files=sys.argv[2:]
    rows=extract(files)
    out=os.path.join(WORK,"raw.csv")
    new=not os.path.exists(out)
    with open(out,'a',newline='') as fh:
        w=csv.writer(fh)
        if new: w.writerow(['branche','company_name','domain'])
        for n,dm in rows: w.writerow([branche,n,dm])
    print(f"{branche}: +{len(rows)} rows from {len(files)} files")
