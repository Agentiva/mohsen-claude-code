#!/bin/bash
# Usage: batch_extract.sh <segment_csv> <marker_file>
# Processes all apollo search result files newer than marker into the segment CSV, then dedupes.
SEG="$1"; MARK="$2"
TR=/root/.claude/projects/-home-user-mohsen-claude-code/402a6a9f-06fb-5272-840b-3b28f466da2e/tool-results
DIR=/home/user/mohsen-claude-code/koenig-mtm-market-intelligence/listen
[ -f "$SEG" ] || echo "company_name,domain" > "$SEG"
n=0
for f in $(find "$TR" -name 'mcp-Apollo_io-apollo_mixed_companies_search-*.txt' -newer "$MARK" 2>/dev/null); do
  python3 "$DIR/extract_apollo.py" "$f" "$SEG"
  n=$((n+1))
done
echo "processed_files=$n"
# dedupe in place by normalized domain, keep header
python3 - "$SEG" <<'PY'
import sys
p=sys.argv[1]
seen=set(); out=["company_name,domain"]
for i,line in enumerate(open(p,encoding='utf-8')):
    line=line.rstrip('\n')
    if i==0 or not line: continue
    # split on last comma
    idx=line.rfind(',')
    if idx<0: continue
    name,dom=line[:idx],line[idx+1:].strip().lower()
    if not dom or dom in seen: continue
    seen.add(dom); out.append(f"{name},{dom}")
open(p,'w',encoding='utf-8').write("\n".join(out)+"\n")
print(f"unique_rows={len(out)-1}")
PY
