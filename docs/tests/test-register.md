# Registro de testes

`planejado` significa que o caso foi especificado, mas ainda não executado. Nenhum caso UWP/Xbox pode ser marcado como aprovado sem hardware ou ambiente compatível e evidência anexada.

| ID | Tipo | Caso | Método | Evidência | Estado | Bloqueio |
|---|---|---|---|---|---|---|
| T-UWP-001 | integração | shell UWP hospeda WebView local | build e execução em Windows | log, versão e captura | planejado | shell UWP inexistente |
| T-WEB-001 | integração | Flutter Web carrega do pacote | inspeção do bundle e hash | hash e log | planejado | shell UWP inexistente |
| T-OFF-001 | sistema | inicializa sem rede | bloquear rede e executar fluxo | log de execução | planejado | shell UWP inexistente |
| T-GAME-001 | aceitação | tarefa crítica por gamepad | matriz de controles em hardware | matriz e vídeo | planejado | Xbox real necessário |
| T-ACC-001 | aceitação | foco e ordem previsíveis | checklist orientado a tarefas | checklist | planejado | interface ainda não implementada |
| T-SEC-001 | segurança | rejeita mensagens inválidas | testes negativos e fuzzing limitado | relatório | planejado | ponte inexistente |
| T-SEC-002 | segurança | bloqueia origem não permitida | URLs permitidas, bloqueadas e redirecionadas | relatório | planejado | ponte inexistente |
| T-STORE-001 | conformidade | bloqueia download indevido | tentativa de download | log e decisão | planejado | shell inexistente |
| T-PERF-001 | desempenho | mede startup, FPS, memória e latência | benchmark repetível | dataset e relatório | planejado | hardware-alvo necessário |
| T-SEC-003 | segurança | threat model sem risco crítico aberto | revisão e testes de abuso | threat model | planejado | implementação necessária |
| T-PRIV-001 | privacidade | logs não expõem PII | inspeção de bundle e logs | inventário e relatório | planejado | telemetria ainda não definida |
| T-PKG-001 | pacote | instala, atualiza e remove MSIX UWP | ciclo de pacote em Windows/Xbox | logs e hashes | planejado | pacote UWP inexistente |
| T-CI-001 | CI | PR executa validações | execução GitHub Actions | URL do workflow | parcialmente executado | suíte completa ainda pendente |
| T-CI-002 | segurança CI | segredos não chegam a forks | revisão de permissões e logs | auditoria | parcialmente executado | revisão de configuração |
| T-CI-003 | release | release exige aprovação e artefato | revisão de ambiente protegido | aprovação e hash | planejado | ambiente de release |

## Evidência automatizada

O executor `tools/run_traceability_tests.py` gera `artifacts/traceability/report.json` e `artifacts/traceability/traceability.log`. O workflow publica esses arquivos como `traceability-evidence`. `blocked` não significa aprovado; indica dependência de shell, hardware, ambiente protegido ou execução manual.

## Critério de transição

`planejado` -> `em execução` exige implementação e ambiente definido. `em execução` -> `aprovado` exige evidência reproduzível, resultado, versão, data e vínculo com commit ou PR. Falha cria risco ou issue; não é convertida em aprovação.
