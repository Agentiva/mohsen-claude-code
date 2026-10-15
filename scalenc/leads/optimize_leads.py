import csv, re, sys, os, unicodedata, collections
UP="/root/.claude/uploads/bb95c6e3-ca30-506b-8a78-30b49e11d619/"
OUTD="/home/user/mohsen-claude-code/scalenc/leads/"
W="/tmp/claude-0/-home-user-mohsen-claude-code/bb95c6e3-ca30-506b-8a78-30b49e11d619/scratchpad/work/"
FILES={"789":"bacde3e3-Fassadenbau-und-Baukomponenten_-NC-Programmierkapazitat-fur-TRUMPF-Maschinen-Default-view-export-1792057981932.csv",
       "790":"3b0eb1e3-Lohnfertigung-Blech_-NC-Programmierkapazitat-fur-TRUMPF-Maschinen-Default-view-export-1792058018435.csv",
       "791":"eb6d1fc0-Industrieunternehmen-mit-eigener-Blechfertigung_-NC-Programmierkapazitat-fur-TRUMPF-Maschinen-Default-view-export-1792058031054.csv"}
OUTN={"789":"789_Fassadenbau_Baukomponenten_leads_optimiert.csv","790":"790_Lohnfertigung_Blech_leads_optimiert.csv","791":"791_Industrie_eigene_Blechfertigung_leads_optimiert.csv"}
COLS=["First Name","Last Name","Full Name","Job Title","Location","Company Name","Company Domain","LinkedIn Profile"]
def norm(s):
    s=unicodedata.normalize("NFKD",s or "").encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+"," ",s).strip()
bl=[norm(x) for x in open(W+"blacklist_names.txt",encoding="utf-8") if x.strip()]
def blacklisted(n):
    n=" "+norm(n)+" "
    return any(len(b)>=4 and (" "+b+" ") in n for b in bl)
NON_DACH=re.compile(r"(?i)\b(hungary|ungarn|kft|poland|polska|czech|france|italy|italia|united states|usa|china|india|netherlands|spain|romania|slovakia|uk|united kingdom|asia|amea|liechtenstein)\b")
# hard exclusions (title clearly irrelevant)
EXCL=re.compile(r"(?i)(personal|human resources|\bhr\b|recruit|buchhalt|accountant|accounting|finanz|controlling|\bcfo\b|marketing|\bcmo\b|assist|\bpa to\b|\bpmo\b|kundendienst|after sales|service-center|\bservice\b|reklamation|qualit|logistik(?!.*produktion)|warehouse|lager\b|kran|elektrotechnik|elektronik|m&a|ehemalig|betriebsrat|kunststoff|plastics|galvanik|beschichtung|korrosion|oberfl|gie(ss|ß)erei|zerspanung|cnc-fr|erodier|business development|\bholz|bauleiter|schornstein|innendienst|onlinevertrieb|kaufm(ä|a)nn|kfm|invest\b|\bit\b ?/|krantechnik|ausbilder|instandhaltung|unterhalt|facility|reinraum|trennw|camper|labeling|rotogravure|turbo|futterteile|drivetrain|robotik|elektronikfertigung|steuerungstechnik)")
HARD=re.compile(r"(?i)(elektrotechnik|elektronikfertigung|kunststoff|plastics|galvanik|beschichtung|korrosion|oberfl)")
DEMOTE=re.compile(r"(?i)(zerspanung|gie(ss|ß)erei|mechanische fertigung)")
SALES=re.compile(r"(?i)(vertrieb|vertieb|sales|verkauf|absatz)")
def has(p,t): return re.search(p,t,re.I) is not None
AV=r"(arbeitsvorbereitung|\bav[ -]?leiter|\bavor\b|technisches? b(ü|u)ro|technical office|work preparation|produktionsplanung|production planning|fertigungsplanung|industrial engineering|manufacturing engineering|production programming|production engineering)"
LEAD=r"(leiter|leitung|head|director|manager|chef|lead)"
BLECH=r"(blech|fassade|alu\b|aluminium|stahl|metallbau|balkon|stanz|sheet)"
PROD=r"(produktionsleit|fertigungsleit|betriebsleit|werkstattleit|werk(s)?leit|plant manager|head of production|leiter produktion|leiterin produktion|leitung produktion|produktionsleitung|production manager|manufacturing manager|produktionsbereichsleiter|teamleiter fertigung|leiter metallbau|bereichsleiter produktion)"
TECH=r"(technischer? (leiter|leitung|betriebsleiter|director)|technische leitung|technical director|\bcto\b|head of engineering)"
GF=r"(gesch(ä|a)ftsf(ü|u)hr|inhaber|eigent(ü|u)mer|\bceo\b|managing director|managing partner|owner|gesellschafter|gesch(ä|a)ftsleitung|gesch(ä|a)ftsleiter|general manager|\bvrp\b|president|vorstand|mitinhaber|founder)"
TGF=r"(technischer gesch(ä|a)ftsf(ü|u)hrer|gesch(ä|a)ftsf(ü|u)hrer (technik|produktion)|technische gesch(ä|a)ftsf|gesch(ä|a)ftsf(ü|u)hrer.*technische leitung|gesch(ä|a)ftsf(ü|u)hrer operatives)"
COO=r"(\bcoo\b|chief operating|director operations|head of operations|managing director operations|operativer leiter|operations director)"
BUY=r"(eink(ä|a)uf|purchas|procurement|beschaffung|buyer)"
STV=r"(stellv|stv\.|deputy|\bdep\.|junior|vice\b)"
def score(pb,t):
    tl=t.lower()
    if not t.strip() or HARD.search(t): return 0,"x"
    ex=EXCL.search(t)
    if ex and re.match(r"(?i)(logistik|lager)",ex.group(0)) and has(BUY,t): ex=None
    if ex and not has(AV,t) and not has(PROD,t): return 0,"x"
    # sales-only titles out (sales combined with GF/tech/AV/production stays, but lower)
    sales=bool(SALES.search(t))
    s,cat=0,"x"
    if pb=="791":
        if has(AV,t) and (has(LEAD,t) or has(r"leiter",t)): s,cat=100,"av"
        elif has(r"leiter blech|blechbearbeitung",t): s,cat=100,"av"
        elif has(r"(werk(s)?leit|plant manager)",t): s,cat=95,"prod"
        elif has(PROD,t) or has(r"head of production|leiter produktion",t): s,cat=92,"prod"
        elif has(TGF,t) or has(COO,t): s,cat=85,"gf"
        elif has(TECH,t): s,cat=80,"tech"
        elif has(r"teamleiter.*arbeitsvorbereitung|arbeitsvorbereitung",t): s,cat=75,"av"
        elif has(r"leiter eink|head of (procurement|purchasing)|leiter einkauf|purchasing manager|head purchasing|global procurement",t): s,cat=65,"buy"
        elif has(r"technisch.*eink|technical buyer",t): s,cat=60,"buy"
        elif has(BUY,t): s,cat=50,"buy"
        elif has(GF,t): s,cat=55,"gf"
    else:
        if has(AV,t) and has(r"(leiter|leitung|head|lead)",t): s,cat=100,"av"
        elif has(r"leiter blech|blechbearbeitung|blechverarbeitung",t) and has(LEAD,t): s,cat=98,"prod"
        elif has(TGF,t): s,cat=97,"gf"
        elif has(PROD,t) and has(BLECH,t): s,cat=96,"prod"
        elif has(PROD,t): s,cat=92,"prod"
        elif has(TECH,t): s,cat=90,"tech"
        elif has(GF,t) or has(COO,t): s,cat=(95 if pb=="790" else 88),"gf"
        elif has(r"teamleiter.*arbeitsvorbereitung|arbeitsvorbereiter",t): s,cat=65,"av"
        elif has(r"leiter eink|head of purchasing|leiter einkauf",t): s,cat=62,"buy"
        elif has(BUY,t): s,cat=58,"buy"
        elif has(r"prokurist",t) and (pb=="790" or has(r"standortleit",t)): s,cat=55,"other"
    if s==0: return 0,"x"
    if sales: s-=20
    if DEMOTE.search(t): s-=30
    if has(STV,t) and cat!="gf": s-=20
    elif has(STV,t): s-=15
    if has(r"\bco-",t): s-=5
    return s,cat
stats={}
for pb,fn in FILES.items():
    rows=list(csv.DictReader(open(UP+fn,encoding="utf-8-sig")))
    seen=set(); cand=[]; drop=collections.Counter()
    for r in rows:
        r={k:(r.get(k) or "").strip() for k in COLS}
        key=r["LinkedIn Profile"].lower().rstrip("/") or (r["Full Name"]+r["Company Domain"]).lower()
        if key in seen: drop["duplikat"]+=1; continue
        seen.add(key)
        if blacklisted(r["Company Name"]): drop["blacklist"]+=1; continue
        if NON_DACH.search(r["Location"]) or NON_DACH.search(r["Job Title"]): drop["nicht DACH"]+=1; continue
        s,cat=score(pb,r["Job Title"])
        if s<50: drop["irrelevanter Jobtitel"]+=1; continue
        cand.append((s,cat,r))
    # max 3 per company, diverse angles
    byco=collections.defaultdict(list)
    for c in cand: byco[c[2]["Company Domain"].lower() or c[2]["Company Name"].lower()].append(c)
    kept=[]
    for co,lst in byco.items():
        lst.sort(key=lambda x:-x[0]); pick=[]; cats=set()
        for c in lst:
            if len(pick)<3 and c[1] not in cats: pick.append(c); cats.add(c[1])
        for c in lst:
            if len(pick)<3 and c not in pick: pick.append(c)
        drop["über 3 Kontakte/Firma"]+=len(lst)-len(pick)
        kept+=pick
    kept.sort(key=lambda x:(-x[0],x[2]["Company Name"].lower()))
    # top 50: distinct company + distinct title, only very relevant
    top=[]; usedco=set(); usedt=collections.Counter()
    for limit in (1,2,3):
        for c in kept:
            if len(top)>=50: break
            co=c[2]["Company Domain"].lower(); tn=norm(c[2]["Job Title"])
            if c[0]<85 or co in usedco or usedt[tn]>=limit or c in top: continue
            top.append(c); usedco.add(co); usedt[tn]+=1
    rest=[c for c in kept if c not in top]
    out=top+rest
    with open(OUTD+OUTN[pb],"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(COLS)
        for c in out: w.writerow([c[2][k] for k in COLS])
    stats[pb]=(len(rows),len(out),len(set(c[2]["Company Domain"] for c in out)),len(top),len(set(norm(c[2]["Job Title"]) for c in top)),dict(drop))
for pb,v in stats.items(): print(pb,"input",v[0],"output",v[1],"firmen",v[2],"top50",v[3],"versch. titel top50",v[4],v[5])
