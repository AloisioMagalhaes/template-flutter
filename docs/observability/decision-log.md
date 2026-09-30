# Decision log

## DEC-0001

- Data: 2026-09-30
- Branch: develop
- Objetivo: iniciar governança antes do spike UWP.
- Decisão: usar `develop` para integração e preservar `main` para releases aprovadas.
- Evidência: `git fetch`, `main` sincronizada com `origin/main`, criação de `develop`.
- Riscos: CI ainda não possui todos os gates automatizados.
- Próximo passo: criar backlog, ADR e teste RED.
- Referência: [CONTRIBUTING.md](../../CONTRIBUTING.md).

## DEC-0002

- Data: 2026-09-30
- Branch: feature/research-traceability
- Objetivo: impedir obsolescência documental durante novas tarefas.
- Decisão: manter documentação, diagramas C4/UML, código, testes e rastreabilidade na mesma pull request.
- Evidência: `docs/governance/documentation-register.md` e validação no workflow.
- Riscos: diagramas planejados podem ser confundidos com implementação; cada arquivo declara seu estado.
- Próximo passo: preencher relatórios dos agentes e revisar os diagramas contra o shell real quando implementado.
