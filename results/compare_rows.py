"""Compare an engine's rows with the reference rows, field by field, at every shared 10,000-block mark.
  python3 compare_rows.py ROWS_JSONL REFERENCE_JSON
Fields only one implementation reports (digest, memory, timing) are skipped."""
import json
import sys

ref = {r["block"]: r for r in json.load(open(sys.argv[2]))["rows"]}
n = bad = 0
for line in open(sys.argv[1]):
    if not line.startswith("{"):
        continue
    r = json.loads(line)
    if r["block"] not in ref:
        continue
    n += 1
    for k, v in ref[r["block"]].items():
        if r.get(k) != v:
            bad += 1
            print(f"block {r['block']} {k}: rows {r.get(k)} reference {v}")
print(f"{n} rows compared, {bad} field differences")
sys.exit(1 if bad or not n else 0)
