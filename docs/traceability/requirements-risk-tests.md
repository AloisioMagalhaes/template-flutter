# Matriz de rastreabilidade

| ID requisito | Requisito | Risco | Teste | Evidência | Estado |
|---|---|---|---|---|---|
| RF-001 | Shell UWP com WebView | R-001 | T-UWP-001 | build e execução UWP | planejado |
| RF-002 | Conteúdo Flutter Web local | R-001/R-006 | T-WEB-001 | bundle local e hash | planejado |
| RF-003 | Inicialização offline | R-006 | T-OFF-001 | execução sem rede | planejado |
| RF-006 | Operação por gamepad | R-003 | T-GAME-001 | matriz de controles | planejado |
| RF-007 | Foco visual e ordem de foco | R-003 | T-ACC-001 | checklist orientado a tarefas | planejado |
| RF-011 | Validação da ponte nativa | R-004 | T-SEC-001 | testes negativos | planejado |
| RF-012 | Allowlist de origens | R-004 | T-SEC-002 | URLs permitidas e bloqueadas | planejado |
| RF-013 | Bloqueio de downloads | R-005 | T-STORE-001 | teste de política | planejado |
| RNF-001 | Desempenho mensurável | R-002 | T-PERF-001 | startup, FPS, memória e latência | planejado |
| RNF-004 | Segurança WebView | R-004 | T-SEC-003 | threat model e relatório | planejado |
| RNF-005 | Privacidade | R-004/R-006 | T-PRIV-001 | inventário e inspeção de logs | planejado |
| RNF-007 | MSIX UWP | R-005 | T-PKG-001 | instalação, atualização e remoção | planejado |
| CI-001 | Testes em pull request | R-007 | T-CI-001 | execução GitHub Actions | planejado |
| CI-004 | Segredos isolados | R-004 | T-CI-002 | auditoria de permissões | planejado |
| CI-007 | Release protegida | R-005 | T-CI-003 | aprovação e artefato | planejado |

## Regras

- `planejado` só muda para `aprovado` com evidência anexada.
- Testes Xbox recebem a marca `hardware-required`.
- Nenhum requisito pode ser encerrado sem teste, risco e evidência.
- Toda alteração nesta matriz deve atualizar o `work-log.md`.
- Fontes usadas nas decisões devem aparecer no documento e em referências ABNT.
