import csv, re, glob, os, collections, sys
UP="/root/.claude/uploads/0e85c987-05dc-5739-b5cf-0940a6f93e4d/"
OUT="/home/user/mohsen-claude-code/outputs/proform/leads/"
TIER="/home/user/mohsen-claude-code/outputs/proform/proform_companies_playbooks_792_793_794_mit_fit_tier.csv"
tier={r["Company Domain"].lower():r["Fit Tier"] for r in csv.DictReader(open(TIER,encoding="utf-8"))}
FILES={"Asia":"2dfb9481","Africa":"a74bbee6","Latin America":"bfe4cefc"}

EXCL=re.compile(r"(sales|satış|venta|vendas|comercial|commercial|marketing|pazarlama|mercadeo|brand (owner|manager|director|equity)|brand director|category|finan|account|contab|contador|cfo|tax|audit|treasur|\bhr\b|human capital|human resource|people|recursos humanos|insan kaynak|legal|lawyer|jur[ií]dic|secretar|\bit\b|\bti\b|information|technology|digital|erp|\bsap\b|software|data|e-commerce|ecommerce|art director|creative|design director|assistant to|asistan|executive assistant|personal assistant|assistance|administration|office manager|regulatory|medical|clinical|pharmacovig|microbio|analytical|patent|procure|purchas|compras|sourcing|supply chain|tedarik|logistic|export|import|international|business development|desenvolvimento de neg|desarrollo de neg|strategy|strategic|corporate communication|communication|investor|independent|independant|non[- ]executive|franchise|franquia|internship|warehouse|restaurant|hotel|mobile|accessor|customer|patient|national account|regional director|area director|area general|cluster director|translator|^ehs|safety director|compliance|training|scientist|product owner|planning|planlama|e-?business|credit|treasury|retail|perakende|branch|store|research associate|consultant|consultor|intern|trainee|student|teacher|professor|\bvet\b|real estate|security)", re.I)
NONCORE=re.compile(r"(facilit|\bmis\b|ppic|\bscm\b|materials|rewards|call center|govt|government|public|policy|\bipr\b|ndds|\bdba\b|clinics|hospitality|program management|corporate affairs|distribut|learning|relations|market development|ethnic|business excellence|human energy|transformation|eye care|\bemd\b|scientific business|portfolio|mercado|suministro|agroneg|ceo office|office of|mali i|lead generation|outlet|board advisor|babycare|culinary|condiments|food service|corporate growth|cis countries|europe|middle east|meaca|north america|f&a|supporting functions|\bex\b|bikanervala haldwani)",re.I)
EXCL_AR=re.compile(r"(مدير مُساعد|مدير حسابات|مدير اقليمي)")
RULES=[ # (score, category, regex)
 (100,"exec",r"^(owner|business owner|company owner|founder|co-founder|cofounder|fundador|propietari[oa]|propriet[aá]ri[oa]|s[oó]ci[oa]|مدير عام|dono|due[nñ]o|ceo|chief executive|group ceo|managing director|joint managing director|deputy managing director|chairman and managing director|director general|diretor geral|presidente?|president director|president|genel m[uü]d[uü]r|general manager|gerente general|chief operating officer|coo|director general adjunto)\b"),
 (100,"exec",r"\b(founder|co-founder|owner|ceo|managing director|propriet[aá]rio|s[oó]cio[- ]diretor|director general)\b"),
 (96,"plant",r"(مدير مصنع|plant manager|plant head|plant director|factory manager|factory director|fabrika m[uü]d[uü]r|fabrika direkt|gerente de planta|gerente industrial|diretor industrial|director industrial|site director|site manager|works manager|director of plant|general manager.*(plant|factory|operations|production|manufactur|technical|engineering))"),
 (94,"production",r"(jef[ea] de producci|administrador[a]? de (la )?producci|gerente executivo (de )?produ|مدير انتاج|مدير إنتاج|head of production|production head|production director|director of production|manufacturing director|director of manufacturing|manufacturing manager|production manager|gerente de produ[cç][aã]o|gerente de producci[oó]n|gerente de produccion|gerente superior de producci|jefe de producci|[uü]retim m[uü]d[uü]r|kepala produksi|unit head (of )?produ|section head of produ|operations director|director of operations|director de operaciones|gerente de operaciones|diretor de opera|head of operations|operational director|technical operations director|operations manager)"),
 (92,"engineering",r"(jef[ea] de ingenier|jef[ea] de mantenimiento|gerente (global )?de engenharia|head of engineering|director of engineering|engineering director|engineering manager|technical director|technical manager|director t[eé]cnico|diretor t[eé]cnico|teknik m[uü]d[uü]r|teknik direkt|maintenance manager|gerente de manuten|gerente de mantenimiento|gerente de engenharia|gerente de ingenier|jefe de mantenimiento|bak[iı]m m[uü]d[uü]r|process engineering manager|unit head of engineering|section head of engineering|plant engineering)"),
 (88,"project",r"(مدير مشروع|project manager|project director|projects head|head of projects|gerente de projetos|gerente de proyectos|jefe de proyectos|proje y[oö]netici|proje m[uü]d[uü]r|capex)"),
 (88,"rnd",r"(r ?& ?d|research (and|&) development|research development|new product development|desarrollo de nuevos productos|novos produtos|npd|innovation|gerente de p&d|p&d|investigaci[oó]n y desarrollo|ar-?ge|desenvolvimento de produto)"),
 (80,"exec",r"^(executive director|whole time director|joint general manager|chief general manager|senior general manager|sr\.? general manager|director|directeur|diretor|group director|business unit director|bu director|director business unit|business director|vice[- ]?presidente?|vice president|deputy director|associate director|chairman|vice chairman|genel m[uü]d[uü]r yard[iı]mc)"),
 (75,"production",r"(deputy|assistant|asst\.?|associate|senior|sr\.?|dy\.?) (general manager|production manager|manufacturing manager|plant manager|factory manager|engineering manager|maintenance manager|project manager)"),
 (65,"quality",r"(quality|qa|qms|qualidade|calidad|kalite)"),
 (55,"exec",r"^(assistant general manager|deputy general manager|associate general manager|asst\.? general manager|assitant general manager|assisstant general manager|general manager assistant)$"),
]
def score(t):
    tl=re.sub(r"\s+"," ",t.strip().lower())
    if not tl or EXCL_AR.search(tl): return 0,"x"
    if EXCL.search(tl):
        return 0,"x"
    best=(0,"x")
    for s,c,rx in RULES:
        if re.search(rx,tl) and s>best[0]: best=(s,c)
    # functional deputy/assistant GM (e.g. "deputy general manager operations") -> boost
    if re.match(r"(deputy|assistant|asst\.?|associate|dy\.?) general manager",tl) and re.search(r"(operation|production|manufactur|plant|factory|engineering|project|technical|r&d)",tl):
        best=(max(best[0],82), best[1] if best[1]!="x" else "production")
    if re.match(r"(deputy|assistant|associate|junior|asst\.?) ",tl) and best[0]>=88 and not tl.startswith(("deputy general","assistant general","associate general")):
        best=(78,best[1])
    if re.match(r"(deputy|assistant|asst\.?|associate|dy\.?|assitant|assisstant) general manager",tl) or "yardımc" in tl or "yardimc" in tl:
        if best[0]>82: best=(82,best[1])
    # plain AGM/DGM without function = unclear -> drop; AGM/DGM QA/QC -> quality level
    core=re.sub(r"\(.*?\)","",tl).strip(" -")
    if re.fullmatch(r"(agm|(deputy|assistant|asst\.?|associate|dy\.?|assitant|assisstant)\s+general manager)",core): return 0,"x"
    if re.match(r"(deputy|assistant|asst\.?|associate|dy\.?) general manager",tl) and best[0]==75:
        best=(65,"quality") if re.search(r"(qa|qc|quality|cqa)",tl) else (0,"x")
    if NONCORE.search(tl): return 0,"x"
    return best
TR={"A":3,"B":2,"C":1}
allstats={}
for pb,pref in FILES.items():
    f=glob.glob(UP+pref+"*.csv")[0]
    rows=list(csv.DictReader(open(f,encoding="utf-8-sig")))
    seen=set(); cands=[]; dropped=collections.Counter()
    for r in rows:
        r={k:(v or "").strip() for k,v in r.items()}
        r["Full Name"]=re.sub(r"\s+"," ",r["Full Name"])
        key=(r["LinkedIn Profile"].lower().rstrip("/")) or (r["Full Name"].lower()+"|"+r["Company Domain"].lower())
        if key in seen: dropped["duplicate"]+=1; continue
        seen.add(key)
        s,c=score(r["Job Title"])
        if s<60: dropped[r["Job Title"]]+=1; continue
        t=TR.get(tier.get(r["Company Domain"].lower(),""),1)
        cands.append((s,t,c,r))
    # top 50: score>=88, tier A/B first, distinct company + distinct title, round-robin categories
    order=["exec","plant","production","engineering","exec","production","project","rnd"]
    TOPNEG=re.compile(r"(civil|stability|pipeline|logist|cultural|log[ií]st|parenteral|quality|qualidade|calidad|kalite|luggage|bag|footwear|dairy|beverage|juice|milk|tetra|injection|blow|mould|mold|packing|packaging|embalag|conselho|talento|cephalospor|sterile|oncolog|\bit\b|mobile|warehouse|utilidades|obras|pharmacist|formulation|analytical|biosimilar|api\b|peptide)",re.I)
    pool=sorted([x for x in cands if x[0]>=88 and not TOPNEG.search(x[3]["Job Title"])],key=lambda x:(-x[1],-x[0]))
    top=[];usedc=set();usedt=set();ci=0;stall=0
    while len(top)<50 and stall<len(order):
        cat=order[ci%len(order)];ci+=1
        pick=next((x for x in pool if x[2]==cat and x[3]["Company Domain"].lower() not in usedc and x[3]["Job Title"].lower() not in usedt and x[3]["Company Name"].lower() not in usedc),None)
        if pick is None: stall+=1; continue
        stall=0; top.append(pick); usedc.add(pick[3]["Company Domain"].lower()); usedc.add(pick[3]["Company Name"].lower()); usedt.add(pick[3]["Job Title"].lower())
    topids={id(x) for x in top}
    rest=sorted([x for x in cands if id(x) not in topids],key=lambda x:(-x[0],-x[1],x[3]["Company Name"].lower()))
    cols=["First Name","Last Name","Full Name","Job Title","Location","Company Name","Company Domain","LinkedIn Profile"]
    fn=OUT+f"proform_leads_{pb.lower().replace(' ','_')}.csv"
    with open(fn,"w",newline="",encoding="utf-8") as fh:
        w=csv.writer(fh); w.writerow(cols)
        for x in top+rest: w.writerow([x[3][c] for c in cols])
    allstats[pb]=(len(rows),len(top)+len(rest),len(top),sum(dropped.values()),dropped)
    if "-v" in sys.argv:
        print("=====",pb); [print(i+1,x[0],x[2],"|",x[3]["Job Title"],"|",x[3]["Company Name"]) for i,x in enumerate(top)]
for pb,(n,k,t,d,dr) in allstats.items():
    print(pb,"input",n,"kept",k,"top",t,"removed",d)
    if "-d" in sys.argv: print(dr.most_common(60))
