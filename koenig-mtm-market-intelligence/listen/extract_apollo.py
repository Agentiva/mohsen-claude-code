#!/usr/bin/env python3
import json, sys, re

def host(u):
    if not u: return ""
    u = re.sub(r'^https?://', '', u.strip()).lower()
    u = u.split('/')[0].split('?')[0]
    return u[4:] if u.startswith('www.') else u

def main():
    res_file, out_csv = sys.argv[1], sys.argv[2]
    data = json.load(open(res_file, encoding='utf-8', errors='ignore'))
    orgs = (data.get('organizations') or []) + (data.get('accounts') or [])
    pag = data.get('pagination', {})
    rows = []
    for o in orgs:
        name = (o.get('name') or '').strip()
        dom = (o.get('primary_domain') or host(o.get('website_url')) or '').strip().lower()
        if name and dom:
            rows.append((name, dom))
    # append
    with open(out_csv, 'a', encoding='utf-8') as f:
        for n, d in rows:
            n2 = '"' + n.replace('"', '""') + '"' if (',' in n or '"' in n) else n
            f.write(f"{n2},{d}\n")
    print(f"orgs_in_page={len(orgs)} written={len(rows)} "
          f"page={pag.get('page')} per_page={pag.get('per_page')} "
          f"total_entries={pag.get('total_entries')} total_pages={pag.get('total_pages')}")

if __name__ == '__main__':
    main()
