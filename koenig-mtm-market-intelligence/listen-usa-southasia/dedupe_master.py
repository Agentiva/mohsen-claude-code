#!/usr/bin/env python3
import sys
p=sys.argv[1]
seen=set(); out=["company_name,company_domain,playbook_name,location"]
from collections import Counter
pc=Counter()
for i,line in enumerate(open(p,encoding='utf-8')):
    line=line.rstrip('\n')
    if i==0 or not line.strip(): continue
    parts=line.rsplit(',',3)  # name may contain quoted commas; split from right into 4
    if len(parts)!=4: continue
    name,dom,pb,loc=parts
    dom=dom.strip().lower()
    if not dom or dom in seen: continue
    seen.add(dom); out.append(f"{name},{dom},{pb},{loc}"); pc[pb]+=1
open(p,'w',encoding='utf-8').write("\n".join(out)+"\n")
print("TOTAL unique:",len(out)-1)
for k,v in sorted(pc.items(), key=lambda x:-x[1]): print(f"  {v:5d}  {k}")
