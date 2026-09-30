from hashlib import sha256
from json import dumps
from pathlib import Path
from re import findall
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
out = root / "artifacts" / "traceability"
out.mkdir(parents=True, exist_ok=True)
matrix = (root / "docs/traceability/requirements-risk-tests.md").read_text(encoding="utf-8")
ids = findall(r"\| (T-[A-Z0-9-]+) \|", matrix)
results = [{"id": i, "status": "blocked", "evidence": None} for i in dict.fromkeys(ids)]
for i in ("T-CI-001", "T-CI-002"):
    for x in results:
        if x["id"] == i:
            x["status"] = "planned-executable"
            x["evidence"] = "GitHub Actions check"
if (root / "test/widget_test.dart").is_file():
    results.append({"id": "TDD-GREEN-WIDGET", "status": "executable", "evidence": "flutter test test/widget_test.dart"})
files = [root / "docs/traceability/requirements-risk-tests.md", root / "docs/tests/test-register.md"]
hashes = {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in files}
report = {"generated_at": datetime.now(timezone.utc).isoformat(), "results": results, "hashes": hashes, "limitations": ["UWP/Xbox hardware evidence requires the target environment", "No video was generated without hardware execution"]}
(out / "report.json").write_text(dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
(out / "traceability.log").write_text("\n".join(f"{x['id']}={x['status']} evidence={x['evidence'] or 'blocked'}" for x in results), encoding="utf-8")
print(dumps(report, ensure_ascii=False))
