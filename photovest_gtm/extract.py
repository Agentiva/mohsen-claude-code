import json, glob, re, sys, csv

TR = "/root/.claude/projects/-home-user-mohsen-claude-code/5cdebf3a-5e31-5815-b10d-533d4e134841/tool-results/"

def norm_domain(url):
    if not url: return ""
    u = url.strip().lower()
    u = re.sub(r'^https?://', '', u)
    u = re.sub(r'^www\.', '', u)
    u = u.split('/')[0].split('?')[0].strip()
    return u

seen = {}
files = sorted(glob.glob(TR + "*apollo_mixed_companies_search*.txt"))
for fp in files:
    try:
        d = json.load(open(fp))
    except Exception:
        continue
    for key in ("accounts", "organizations"):
        for it in d.get(key, []) or []:
            name = (it.get("name") or "").strip()
            dom = norm_domain(it.get("website_url") or it.get("primary_domain") or "")
            if not name or not dom: 
                continue
            if dom not in seen:
                seen[dom] = name

out = sys.argv[1] if len(sys.argv) > 1 else "/home/user/mohsen-claude-code/photovest_gtm/raw.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["company_name", "domain"])
    for dom, name in seen.items():
        w.writerow([name, dom])
print(f"files={len(files)} unique_companies={len(seen)}")
