from pathlib import Path
import sys

r = Path("docs/agents/reports")
h = ["## Papel", "## Escopo", "## Achados", "## Evidências", "## Riscos", "## Decisões propostas", "## Testes", "## Referências ABNT", "## Conflitos", "## Recomendação"]
e = []
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
