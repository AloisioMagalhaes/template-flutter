# Flutter Web em UWP WebView para Windows e Xbox

## Status

- Data da revisão: 2026-09-30
- Estado: hipótese de arquitetura; não aprovado para publicação
- Objeto de estudo: viabilidade técnica, desempenho, segurança, privacidade, acessibilidade, entrada por controle e certificação de um aplicativo Flutter Web hospedado em `Windows.UI.Xaml.Controls.WebView` dentro de um aplicativo UWP.
- Hipótese: um shell UWP nativo hospeda um build Flutter Web local e distribui um único MSIX para Windows e Xbox.
- Critério de decisão: somente avançar para publicação após testes em dispositivo Xbox e validação da documentação e certificação vigentes.

## Conclusão atual

O `WebView` UWP é o caminho tecnicamente mais plausível para hospedar conteúdo web no Xbox. A documentação da Microsoft afirma que aplicativos para Xbox devem usar o controle `WebView`; `WebView2` não deve ser assumido como disponível no Xbox. O Flutter atual suporta compilação Web, mas não fornece um shell UWP/Xbox oficial. Portanto, a arquitetura exige um shell UWP nativo em C#, C++/WinRT ou C++/CX e o Flutter Web como conteúdo hospedado.

O resultado ainda é uma hipótese, não uma garantia de aceitação. O mesmo MSIX somente será considerado candidato multiplataforma se o manifesto, as APIs, o conteúdo local, a navegação por gamepad, o desempenho e os testes de certificação forem aprovados para cada família de dispositivo.

## Limitações técnicas

### Runtime e renderização

- O `WebView` UWP usa o mecanismo Edge disponível na plataforma; comportamento e APIs não devem ser inferidos a partir de Chrome desktop.
- O Flutter Web pode ser compilado com JavaScript ou WebAssembly. O modo `--wasm` precisa ser medido no runtime efetivamente disponível no Xbox; fallback JavaScript deve permanecer possível até validação.
- Canvas, WebGL, codecs, fontes, armazenamento local, Service Worker e APIs web devem ser testados no dispositivo-alvo.
- Build remoto introduz dependência de rede, disponibilidade, cache, atualização e integridade. O primeiro experimento deve empacotar o conteúdo web localmente.
- Código JavaScript carregado dinamicamente aumenta o risco de alteração de comportamento e deve ser evitado para funções críticas.

### Entrada e experiência Xbox

- A experiência deve funcionar sem mouse e teclado.
- A Microsoft recomenda navegação XY, foco visual claro, foco engajado e teste com gamepad e controle remoto.
- `WebView` pode exigir mouse mode; a aplicação deve solicitar esse modo somente quando necessário e priorizar navegação XY.
- Devem ser testados foco inicial, ordem de foco, A, B, X, Y, gatilhos, bumpers, D-pad, menu, voltar, rolagem, teclado virtual e perda de foco.
- A API Gamepad do navegador não substitui a política de entrada UWP; o shell deve validar eventos e comportamento do controle.

### Segurança e privacidade

- Conteúdo remoto não deve ser tratado como confiável.
- Usar HTTPS, Content Security Policy, Subresource Integrity quando aplicável, origem controlada e lista explícita de domínios.
- Não expor ponte nativa JavaScript desnecessária. Qualquer `ScriptNotify`, `InvokeScriptAsync` ou canal equivalente deve validar origem, esquema, tamanho, tipo e autorização.
- Não inserir tokens, credenciais, dados pessoais ou segredos no JavaScript, URL, localStorage ou logs.
- Desabilitar navegação externa por padrão e tratar redirecionamentos, downloads, pop-ups e esquemas personalizados explicitamente.
- Os estudos acadêmicos sobre WebView mostram que a ponte web-nativa pode ampliar fluxo de dados sensíveis e a superfície de ataque; os resultados devem ser usados como hipótese de risco, não como medição direta do Xbox.

### Distribuição e certificação

- Desktop Bridge/MSIX não converte automaticamente um executável Flutter Win32 em aplicativo executável no Xbox.
- O pacote precisa ser UWP, ter manifesto adequado para a família Xbox e obedecer às políticas da Store.
- Aplicativos que navegam na web no Xbox possuem restrições específicas, inclusive sobre download e cópia de arquivos.
- A certificação deve ser tratada como gate externo; aprovação em Windows não prova aprovação em Xbox.

## Método de investigação

1. Criar um shell UWP mínimo com `WebView` e página local estática.
2. Executar smoke test em Windows e em Xbox Developer Mode.
3. Substituir a página estática por build Flutter Web JavaScript.
4. Medir tempo de inicialização, FPS, latência de entrada, memória, tamanho do pacote, uso de CPU/GPU, falhas de navegação e recuperação offline.
5. Comparar JavaScript e Wasm quando o runtime do Xbox permitir.
6. Adicionar navegação completa por gamepad antes de integrar APIs nativas.
7. Aplicar threat model, CSP, revisão da ponte e testes de abuso.
8. Automatizar lint, testes Dart, build web, verificação de integridade, empacotamento MSIX e relatório.
9. Executar testes manuais em Xbox real; o CI não deve declarar compatibilidade Xbox sem essa evidência.
10. Registrar cada decisão, risco, medição e exceção em Issues vinculadas ao commit.

## Critérios de aceitação do experimento

- O aplicativo inicia offline com conteúdo empacotado.
- Todas as telas principais são navegáveis apenas com gamepad.
- Não há foco invisível, armadilha de foco ou ação dependente de hover.
- O shell rejeita origem, navegação, download e mensagem não autorizados.
- Não existem segredos nem PII no bundle, logs ou artefatos públicos.
- O build reproduzível gera MSIX com manifesto e arquitetura documentados.
- O relatório contém medições separadas para Windows e Xbox.
- Falha em requisito crítico bloqueia a hipótese de publicação.

## Riscos iniciais

| ID | Risco | Tratamento | Evidência de encerramento |
|---|---|---|---|
| R1 | WebView/engine divergente do navegador de desenvolvimento | Matriz de APIs e testes no Xbox | Relatório sem API não suportada |
| R2 | Desempenho insuficiente do Flutter Web | Benchmark JavaScript/Wasm e redução de animações | Metas de FPS, memória e startup atingidas |
| R3 | Navegação inadequada por controle | Modelo de foco e testes de gamepad | Todas as tarefas críticas concluídas sem mouse |
| R4 | Ponte web-nativa explorável | CSP, validação de origem e testes negativos | Threat model sem risco crítico aberto |
| R5 | MSIX aceito no Windows e rejeitado no Xbox | Manifesto, sandbox e certificação preliminar | Evidência de instalação e execução no Xbox |
| R6 | Dependência de rede impede uso | Conteúdo local, cache controlado e tela offline | Inicialização offline funcional |
| R7 | Política da Store bloqueia o produto | Revisão de políticas antes do release | Checklist de certificação aprovado |

## Issues propostas

### #1 Shell UWP WebView mínimo

Entregar um host UWP nativo com `WebView`, conteúdo local, navegação bloqueada por padrão e diagnóstico de runtime.

### #2 Flutter Web empacotado localmente

Adicionar `flutter build web`, copiar `build/web` para o pacote UWP e validar carregamento sem rede.

### #3 Compatibilidade de gamepad

Implementar foco, XY navigation, foco visual, retorno, rolagem e testes de tarefas no Xbox.

### #4 Benchmark Windows versus Xbox

Medir startup, FPS, memória, CPU/GPU, latência de input, tamanho e falhas em versões JavaScript e Wasm.

### #5 Hardening WebView

Aplicar CSP, HTTPS, allowlist de origem, bloqueio de downloads, validação de mensagens e testes de XSS/injeção.

### #6 MSIX UWP e validação de Store

Gerar pacote neutral ou x64, validar manifesto, capabilities, identidade, versão e checklist de certificação.

### #7 Gate de release Xbox

Impedir que o CI marque compatibilidade Xbox sem evidência anexada de execução em dispositivo Xbox e revisão humana.

## Referências oficiais

1. Microsoft, WebView Class. https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.webview
2. Microsoft, Gamepad and remote control interactions. https://learn.microsoft.com/en-us/windows/apps/design/input/gamepad-and-remote-interactions
3. Microsoft, Gamepad and remote control interactions for UWP. https://learn.microsoft.com/en-us/windows/uwp/ui-input/gamepad-and-remote-interactions
4. Microsoft, Store policies for web-browsing products on Xbox. https://learn.microsoft.com/en-us/windows/apps/publish/store-policy-archive/store-policy-7-16-1
5. Microsoft, WebView2 and Xbox application architecture note. https://github.com/MicrosoftDocs/windows-dev-docs/blob/docs/uwp/apps-for-xbox/application-architecture.md
6. Flutter, Build and release a web app. https://docs.flutter.dev/deployment/web
7. Flutter, Building Windows apps. https://docs.flutter.dev/platform-integration/windows/building
8. Flutter, issue: re-enable UWP support for Xbox app development. https://github.com/flutter/flutter/issues/137045
9. Microsoft, UWP application platform guide. https://github.com/MicrosoftDocs/windows-dev-docs/blob/docs/uwp/get-started/universal-application-platform-guide.md

## Bibliografia acadêmica

1. TIWARI, Abhishek et al. A Large Scale Analysis of Android-Web Hybridization. Journal of Systems and Software, v. 170, 110775, 2020. DOI: https://doi.org/10.1016/j.jss.2020.110775. Evidência: pontes WebView-nativas podem permitir fluxos de dados sensíveis e ampliar a superfície de ataque.
2. RIZZO, Claudio; CAVALLARO, Lorenzo; KINDER, Johannes. BabelView: Evaluating the Impact of Code Injection Attacks in Mobile Webviews. arXiv:1709.05690, 2017. https://arxiv.org/abs/1709.05690. Evidência: JavaScript injetado pode explorar interfaces expostas pelo host.
3. TONGBO, Luo. Attacks and Countermeasures for WebView on Mobile Systems. Syracuse University, 2014. https://surface.syr.edu/etd/81/. Evidência: a comunicação bidirecional WebView-aplicativo exige modelo de ameaça próprio.
4. FERNANDES, Earl et al. Breaking and Fixing Origin-Based Access Control in Hybrid Web/Mobile Application Frameworks. Proceedings of NDSS, 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4254737/. Evidência: pontes e confusão de origem podem enfraquecer isolamento.
5. BEER, Christopher et al. Plain Text, Plain Risks: Measuring HTTP Inclusion in Android WebViews at Scale. USENIX Security Symposium, 2026. https://www.usenix.org/conference/usenixsecurity26/presentation/beer. Evidência: inclusão HTTP em WebViews continua risco de interceptação e tomada de controle.

## Normas e métodos relacionados

- ISO/IEC/IEEE 12207:2026: processos do ciclo de vida de software.
- ISO/IEC/IEEE 29119-1:2022 e 29119-2:2021: conceitos, processos e testes baseados em risco.
- ISO/IEC 29100:2024: terminologia, atores e salvaguardas de privacidade.
- ISO/IEC 27001:2022: sistema de gestão de segurança da informação.
- ISO 31000:2018: identificação, análise, tratamento e monitoramento de riscos.
- NIST SP 800-218 SSDF: práticas de desenvolvimento seguro.
- NIST SP 800-207: princípios de Zero Trust aplicáveis ao shell, pipeline e ponte web-nativa.

## Nota sobre Context7

Esta revisão usou fontes oficiais e bibliografia acadêmica acessíveis na web. O conector Context7 não estava disponível nesta execução; quando estiver disponível, consultar suas versões de documentação Flutter, UWP/WebView e dependências antes de decisões que dependam de APIs versionadas.
