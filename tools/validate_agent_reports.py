from pathlib import Path
import sys

r = Path("docs/agents/reports")
h = ["## Papel", "## Escopo", "## Achados", "## Evidências", "## Riscos", "## Decisões propostas", "## Testes", "## Referências ABNT", "## Conflitos", "## Recomendação"]
e = []
required = [
    "docs/governance/documentation-register.md",
    "docs/governance/documentation-change-log.md",
    "docs/architecture/c4/context.md",
    "docs/architecture/c4/containers.md",
    "docs/architecture/c4/components.md",
    "docs/architecture/uml/use-cases.md",
    "docs/architecture/uml/activity-ci-cd.md",
    "docs/architecture/uml/sequence-webview.md",
    "docs/architecture/uml/state-lifecycle.md",
    "docs/architecture/uml/deployment.md",
]
e += [f"documento ausente: {x}" for x in required if not Path(x).is_file()]
e += ["registro sem protocolo de atualização" for x in [0] if "mesma pull request" not in Path("docs/governance/documentation-register.md").read_text(encoding="utf-8")]
for p in sorted(r.glob("*.md")):
    if p.name == "TEMPLATE.md":
        continue
    s = p.read_text(encoding="utf-8")
    e += [f"{p}: seção ausente: {x}" for x in h if x not in s]
    e += [f"{p}: relatório vazio" for _ in [0] if len(s.strip()) < 120]
print("relatorios=", len(list(r.glob("*.md"))) - int((r / "TEMPLATE.md").exists()))
if e:
    print("\n".join(e))
    sys.exit(1)
