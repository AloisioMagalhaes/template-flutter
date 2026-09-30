# Registro de riscos

| ID | Risco | Probabilidade | Impacto | Tratamento | Estado |
|---|---|---:|---:|---|---|
| R-001 | Flutter Web não executar no WebView UWP do Xbox | média | crítico | Spike UWP com HTML local e teste em Xbox real | aberto |
| R-002 | Desempenho insuficiente no Xbox | média | alto | Benchmark JavaScript/Wasm no hardware-alvo | aberto |
| R-003 | Navegação por gamepad incompleta | alta | alto | TDD de foco, XY navigation e teste orientado a tarefas | aberto |
| R-004 | Ponte WebView-nativa vulnerável | média | crítico | CSP, allowlist, validação de mensagens e testes negativos | aberto |
| R-005 | MSIX aceito no Windows e rejeitado no Xbox | média | crítico | Manifesto, instalação no Xbox e revisão da Store | aberto |
| R-006 | Falta de evidência acadêmica específica para Xbox | alta | médio | Registrar lacuna e separar literatura transferida de experimento próprio | aberto |
| R-007 | Divergência entre repositório local e remoto | baixa | alto | Fetch antes/depois e gate de sincronização | controlado |
| R-008 | Evidência esperada confundida com evidência executada | média | crítico | Gate conjunto, relatório de execução e vínculo de artefato | aberto |
