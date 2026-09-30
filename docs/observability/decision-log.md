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
