# ADR-0003: Reavaliar o engine WebView antes da validação Xbox

- Status: aberto
- Data: 2026-09-30
- Origem: revisão dos agentes no PR #17

## Contexto

O spike usa `Windows.UI.Xaml.Controls.WebView` conforme o escopo original. A revisão técnica identificou documentação Microsoft mais recente sobre WebView2/UWP e depreciação do WebView clássico. Isso cria uma decisão arquitetural que não deve ser resolvida por inferência.

## Decisão provisória

Manter o WebView clássico somente como experimento comparativo do spike. Não declarar que WebView2 é disponível ou aceito no Xbox sem fonte oficial aplicável, build e teste no ambiente-alvo.

## Gate

Antes de integrar Flutter Web ou declarar compatibilidade Xbox, comparar oficialmente WebView clássico e WebView2 para o alvo, registrar disponibilidade, ciclo de vida, entrada, política da Store e resultado experimental.

## Conflito

Fontes oficiais podem evoluir; a decisão deve registrar versão, URL, data de acesso e aplicabilidade à plataforma. Literatura acadêmica não resolve disponibilidade de API ou certificação.
