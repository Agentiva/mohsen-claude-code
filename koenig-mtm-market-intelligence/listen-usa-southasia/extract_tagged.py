#!/usr/bin/env python3
import json, sys, re, glob, os
TR="/root/.claude/projects/-home-user-mohsen-claude-code/402a6a9f-06fb-5272-840b-3b28f466da2e/tool-results"
def host(u):
    if not u: return ""
    u=re.sub(r'^https?://','',u.strip()).lower().split('/')[0].split('?')[0]
    return u[4:] if u.startswith('www.') else u
def main():
    marker, append_csv, playbook, location = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    files=[f for f in glob.glob(TR+"/mcp-Apollo_io-apollo_mixed_companies_search-*.txt") if os.path.getmtime(f)>os.path.getmtime(marker)]
    rows=[]
    for f in files:
        try: d=json.load(open(f,encoding='utf-8',errors='ignore'))
        except: continue
        for o in (d.get('organizations') or [])+(d.get('accounts') or []):
            name=(o.get('name') or '').strip()
            dom=(o.get('primary_domain') or o.get('domain') or host(o.get('website_url')) or '').strip().lower()
            if name and dom: rows.append((name,dom))
    with open(append_csv,'a',encoding='utf-8') as fh:
        for n,d in rows:
            n2='"'+n.replace('"','""')+'"' if (',' in n or '"' in n) else n
            fh.write(f"{n2},{d},{playbook},{location}\n")
    print(f"files={len(files)} rows_appended={len(rows)}")
if __name__=='__main__': main()
