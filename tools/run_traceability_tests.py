from hashlib import sha256
from json import dumps
from pathlib import Path
from re import findall
from datetime import datetime, timezone
from subprocess import run
from shutil import which

root = Path(__file__).resolve().parents[1]
out = root / "artifacts" / "traceability"
out.mkdir(parents=True, exist_ok=True)
matrix = (root / "docs/traceability/requirements-risk-tests.md").read_text(encoding="utf-8")
ids = findall(r"\| (T-[A-Z0-9-]+) \|", matrix)
results = [{"id": i, "status": "blocked", "evidence": None} for i in dict.fromkeys(ids)]
commands = {}
flutter = which("flutter") or which("flutter.bat") or "flutter.bat"
for name, command in {"flutter_test": [flutter, "test", "test/widget_test.dart"], "flutter_analyze": [flutter, "analyze"]}.items():
    x = run(command, cwd=root, capture_output=True, text=True)
    commands[name] = {"returncode": x.returncode, "output": (x.stdout + x.stderr)[-4000:]}
passed = commands["flutter_test"]["returncode"] == 0 and commands["flutter_analyze"]["returncode"] == 0
for i in ("T-CI-001", "T-CI-002"):
    for x in results:
        if x["id"] == i:
            x["status"] = "passed" if passed and i == "T-CI-001" else "planned-executable"
            x["evidence"] = "GitHub Actions check and local Flutter validation" if passed and i == "T-CI-001" else "GitHub Actions check"
if (root / "test/widget_test.dart").is_file():
    results.append({"id": "TDD-GREEN-WIDGET", "status": "passed" if commands["flutter_test"]["returncode"] == 0 else "failed", "evidence": "flutter test test/widget_test.dart"})
files = [root / "docs/traceability/requirements-risk-tests.md", root / "docs/tests/test-register.md"]
hashes = {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in files}
commit = run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True).stdout.strip()
report = {"generated_at": datetime.now(timezone.utc).isoformat(), "commit": commit, "commands": commands, "results": results, "hashes": hashes, "limitations": ["UWP/Xbox hardware evidence requires the target environment", "No video was generated without hardware execution"]}
(out / "report.json").write_text(dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
(out / "traceability.log").write_text("\n".join(f"{x['id']}={x['status']} evidence={x['evidence'] or 'blocked'}" for x in results), encoding="utf-8")
print(dumps(report, ensure_ascii=False))
