# Fluxo autônomo de agentes

## Objetivo

Organizar análises independentes de modelos LLM sem permitir alterações autônomas no código, nos requisitos ou na publicação.

## Papéis

| Papel | Escopo | Saída |
|---|---|---|
| Product Owner / Requisitos | valor, escopo, critérios e conflitos | relatório de requisitos |
| Arquiteto Flutter/UWP/Xbox | APIs, shell, compatibilidade e ADRs | relatório arquitetural |
| Segurança, Privacidade e Zero Trust | ameaças, dados, controles e evidências | relatório de segurança |
| QA, TDD e Acessibilidade | testes, critérios, gamepad e acessibilidade | relatório de qualidade |
| DevSecOps e Release | pipeline, artefatos, gates e rastreabilidade | relatório operacional |

## Autonomia controlada

1. Cada agente trabalha somente no seu escopo e lê o contrato comum.
2. Cada agente registra uma issue ou sub-issue e produz um relatório em `docs/agents/reports/`.
3. Agentes não alteram código, requisitos, workflow, branches, releases ou configurações externas.
4. Cada achado deve conter evidência, risco, impacto, recomendação, teste e referência ABNT quando aplicável.
5. O coordenador consolida relatórios, elimina duplicidade e registra conflitos.
6. Product Owner decide prioridade e aceitação.
7. Arquiteto registra decisões aceitas em ADR.
8. QA converte decisões aceitas em testes RED e GREEN.
9. DevSecOps implementa somente itens aceitos por issue e pull request.
10. Merge e publicação exigem revisão humana.

## Contrato de relatório

Cada relatório deve conter exatamente as seções do template. A ausência de evidência ou referência deve ser explicitada como `N/A` com justificativa.

## Consolidação

O coordenador deve relacionar `requisito -> achado -> risco -> decisão -> teste -> evidência -> commit/PR`. Conflitos não resolvidos bloqueiam implementação e release.

As atribuições vigentes e os identificadores das conversas estão em `docs/agents/assignments.json`. O estado `assigned` significa que a análise foi delegada; somente `reported`, `reviewed` e `accepted` autorizam as etapas seguintes.

## Limites

O pipeline valida estrutura e rastreabilidade dos relatórios, mas não considera texto LLM como prova de compatibilidade Xbox, segurança, privacidade ou certificação.
