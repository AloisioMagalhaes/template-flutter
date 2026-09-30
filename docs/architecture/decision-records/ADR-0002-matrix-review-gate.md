# ADR-0002: Gate de revisão conjunta da matriz

- Status: bloqueado
- Data: 2026-09-30
- Revisores: Product Owner, Arquiteto Flutter/UWP/Xbox, QA/TDD e Segurança/Privacidade
- Issue: #12

## Contexto

A matriz requisito-risco-teste contém risco, teste e fundamentação para os itens listados. O campo de evidência, porém, descreve evidência esperada e não comprova execução. Os casos UWP, Xbox, gamepad, desempenho, ponte, privacidade e MSIX UWP ainda estão planejados ou bloqueados.

## Conflitos registrados

1. A matriz pode ser interpretada como aprovada porque possui referências, embora os testes de hardware não tenham sido executados.
2. O pipeline GREEN valida documentação e Flutter básico, mas não valida shell UWP, Xbox ou MSIX UWP.
3. A literatura acadêmica sustenta hipóteses e controles, mas não substitui evidência específica do produto.
4. `planejado` e `blocked` não podem ser convertidos em `aprovado` por revisão documental.

## Decisão

Não aprovar a matriz neste ciclo. A aprovação fica condicionada a evidência reproduzível para cada requisito, risco, teste e fonte, com vínculo a commit, PR, log, hash ou evidência de hardware quando aplicável.

## Ações

- Product Owner: revisar critérios e aceitar somente evidência suficiente.
- Arquiteto: executar o spike UWP e atualizar ADR-0001.
- QA: transformar os casos planejados em testes executáveis e revisar resultados.
- Segurança: executar threat model, testes negativos e inspeção de privacidade.
- DevSecOps: publicar logs, hashes e artefatos sem expor segredos.

## Consequências

O spike UWP permanece bloqueado até o fechamento deste gate. A decisão evita declarar compatibilidade Xbox sem ensaio específico.
