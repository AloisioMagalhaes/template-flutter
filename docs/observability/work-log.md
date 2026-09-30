# Work log

## WORK-0001

- Data: 2026-09-30
- Branch: develop
- Objetivo: executar governança inicial autorizada.
- Entrada: `main` sincronizada com `origin/main` no commit `98a9728`.
- Ações: `fetch`, auditoria Git, criação de `develop`, criação de documentos e teste RED.
- Resultado: governança preparada; spike UWP não iniciado.
- Evidência: commit desta execução e branch remota `develop`.
- Issues: #1 a #7 no GitHub.
- Sub-issues de pesquisa: #8 a #12.
- Artefatos: `docs/traceability/requirements-risk-tests.md` e `docs/research/research-log.md`.
- Próximo passo: revisar o teste RED e decidir a implementação do shell UWP no próximo ciclo.

## WORK-0002

- Data: 2026-09-30
- Branch: feature/research-traceability
- Objetivo: implementar documentation-first com C4 e UML 2.x.
- Ações: criar registro documental, log de mudanças, diagramas como código e gates de validação.
- Resultado: documentação obrigatória e validação de links integrada ao CI.
- Evidência: commit desta execução e workflow `ci-cd`.
- Limitação: shell UWP e compatibilidade Xbox continuam não implementados.

## WORK-0003

- Data: 2026-09-30
- Branch: feature/traceability-abnt
- Objetivo: corrigir fundamentação explícita da matriz conforme política ABNT.
- Ações: adicionar coluna de fundamentação, citações autor-data, distinção entre fonte acadêmica, oficial, normativa e inferência, referências ABNT e limitações.
- Resultado: matriz apta para revisão; estados permanecem `planejado`.
- Evidência: pull request desta branch.

## WORK-0004

- Data: 2026-09-30
- Branch: feature/traceability-abnt
- Objetivo: registrar todos os casos de teste citados na matriz.
- Ações: criar `docs/tests/test-register.md` e validar IDs automaticamente no CI.
- Resultado: todos os IDs possuem especificação e estado explícito; nenhum teste de Xbox foi declarado executado.
- Evidência: workflow CI e registro de testes.

## WORK-0005

- Data: 2026-09-30
- Branch: feature/traceability-abnt
- Objetivo: gerar evidências automatizadas sem simular hardware.
- Ações: criar executor de rastreabilidade, relatório JSON, log e hashes; publicar artefato no CI.
- Resultado: testes disponíveis são classificados como executáveis ou planejados/bloqueados.
- Limitação: vídeo, UWP, Xbox e MSIX UWP continuam dependentes de ambiente real.

## WORK-0006

- Data: 2026-09-30
- Branch: feature/matrix-review-gate
- Objetivo: executar revisão conjunta Product Owner, Arquiteto, QA e Segurança.
- Resultado: gate bloqueado; requisitos possuem fontes e testes planejados, mas não evidências executadas suficientes.
- Conflito: evidência esperada não equivale a resultado reproduzível.
- Evidência: ADR-0002, Issue #12 e risco R-008.

## WORK-0007

- Data: 2026-09-30
- Branch: feature/uwp-webview-spike
- Objetivo: iniciar o shell UWP WebView mínimo da Issue #3.
- Ações: criar projeto UWP, manifesto, WebView, HTML local e bloqueio de navegação externa.
- Resultado: scaffold criado; T-UWP-001 em execução.
- Limitação: MSBuild/.NET UWP e assets finais não estão disponíveis neste ambiente; Xbox não testado.
