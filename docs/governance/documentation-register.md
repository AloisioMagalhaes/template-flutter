# Registro documental

| Documento | Proprietário | Estado | Atualizar quando | Validação |
|---|---|---|---|---|
| `docs/requirements/software-product-requirements.md` | Product Owner | vigente | requisito, critério ou escopo mudar | revisão e referências |
| `docs/architecture/decision-records/ADR-0001-uwp-webview.md` | Arquiteto | vigente | decisão arquitetural mudar | ADR e revisão |
| `docs/architecture/c4/context.md` | Arquiteto | vigente | ator ou sistema externo mudar | CI e revisão |
| `docs/architecture/c4/containers.md` | Arquiteto | vigente | container, protocolo ou artefato mudar | CI e revisão |
| `docs/architecture/c4/components.md` | Arquiteto | planejado | componente ou ponte mudar | revisão |
| `docs/architecture/uml/use-cases.md` | Product Owner | vigente | objetivo de ator mudar | CI e revisão |
| `docs/architecture/uml/activity-ci-cd.md` | DevSecOps | vigente | etapa ou gate mudar | CI e revisão |
| `docs/architecture/uml/sequence-webview.md` | Arquiteto | vigente | mensagem ou fluxo mudar | CI e revisão |
| `docs/architecture/uml/state-lifecycle.md` | QA | vigente | estado ou transição mudar | CI e revisão |
| `docs/architecture/uml/deployment.md` | DevSecOps | vigente | ambiente ou artefato mudar | CI e revisão |
| `docs/traceability/requirements-risk-tests.md` | QA | vigente | requisito, risco ou teste mudar | CI e revisão |
| `docs/observability/work-log.md` | DevSecOps | vigente | tarefa executada | commit e PR |
| `docs/observability/decision-log.md` | Arquiteto | vigente | decisão tomada | ADR |

Estados permitidos: `vigente`, `planejado`, `obsoleto`, `bloqueado`.

Toda alteração de código, workflow, requisito, risco ou interface deve atualizar este registro e os documentos afetados na mesma pull request.
