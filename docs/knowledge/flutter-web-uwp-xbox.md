# Flutter Web em UWP WebView para Windows e Xbox

> As citações seguem a ABNT NBR 10520:2023 e as referências seguem a ABNT NBR 6023:2018. A política vinculante está em [abnt-citation-policy.md](abnt-citation-policy.md).

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

## Citações ABNT das afirmações centrais

O controle `WebView` UWP é indicado pela Microsoft para aplicativos Xbox, enquanto `WebView2` não deve ser assumido como disponível no console (Microsoft, [s.d.-a]; Microsoft, [s.d.-b]).

O Flutter documenta compilação Web e um runner Windows tradicional, mas não oferece atualmente um shell UWP/Xbox oficial; a necessidade de um shell nativo é, portanto, uma inferência arquitetural deste projeto (Flutter, [s.d.-a]; Flutter, [s.d.-b]; Flutter, 2023).

A navegação Xbox deve considerar gamepad, foco visual, foco engajado, navegação XY e testes em experiência de 10 pés (Microsoft, [s.d.-c]).

Estudos de WebView indicam riscos de fluxo de dados entre código Web e nativo, injeção e abuso de interfaces expostas (Tiwari et al., 2020; Rizzo, Cavallaro e Kinder, 2017; Tiwari, Prakash e Hammer, 2023).

Estudos de aplicações Web para TV indicam que acessibilidade automática não substitui testes orientados a tarefas e usuários, e que limitações de hardware e comportamento alteram o projeto Web (Fernandes et al., 2013; Costa e Duarte, 2017; Lee e Zhong, 2005).

As afirmações acima são evidência ou síntese das fontes. Compatibilidade efetiva com o Xbox continua resultado experimental a ser obtido pelo projeto.

## Referências em formato ABNT

COSTA, Daniel; DUARTE, Carlos. Visually impaired people and the emerging connected TV: a comparative study of TV and Web applications' accessibility. Universal Access in the Information Society, 2017. DOI: 10.1007/S10209-016-0451-6. Disponível em: https://doi.org/10.1007/S10209-016-0451-6. Acesso em: 30 set. 2026.

FERNANDES, Nádia et al. Evaluating the accessibility of adaptive TV based Web applications. 2013. DOI: 10.1007/978-1-4471-5082-4_9. Disponível em: https://doi.org/10.1007/978-1-4471-5082-4_9. Acesso em: 30 set. 2026.

FLUTTER. Build and release a web app. [S. l.]: Flutter, [s.d.-a]. Disponível em: https://docs.flutter.dev/deployment/web. Acesso em: 30 set. 2026.

FLUTTER. Building Windows apps with Flutter. [S. l.]: Flutter, [s.d.-b]. Disponível em: https://docs.flutter.dev/platform-integration/windows/building. Acesso em: 30 set. 2026.

FLUTTER. [Windows][UWP] Re-enable UWP support for Xbox app development. GitHub, 2023. Disponível em: https://github.com/flutter/flutter/issues/137045. Acesso em: 30 set. 2026.

LEE, Meng-Huang; ZHONG, He-Rong. Design considerations for web-based interactive TV services. International Conference on Web Engineering, 2005. DOI: 10.1007/11531371_75. Disponível em: https://doi.org/10.1007/11531371_75. Acesso em: 30 set. 2026.

MICROSOFT. Gamepad and remote control interactions. [S. l.]: Microsoft Learn, [s.d.-c]. Disponível em: https://learn.microsoft.com/en-us/windows/apps/design/input/gamepad-and-remote-interactions. Acesso em: 30 set. 2026.

MICROSOFT. WebView class. [S. l.]: Microsoft Learn, [s.d.-a]. Disponível em: https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.webview. Acesso em: 30 set. 2026.

MICROSOFT. WebView2 and Xbox application architecture. [S. l.]: MicrosoftDocs, [s.d.-b]. Disponível em: https://github.com/MicrosoftDocs/windows-dev-docs/blob/docs/uwp/apps-for-xbox/application-architecture.md. Acesso em: 30 set. 2026.

RIZZO, Claudio; CAVALLARO, Lorenzo; KINDER, Johannes. BabelView: evaluating the impact of code injection attacks in mobile WebViews. arXiv, 2017. Disponível em: https://arxiv.org/abs/1709.05690. Acesso em: 30 set. 2026.

TIWARI, Abhishek et al. A large scale analysis of Android-Web hybridization. Journal of Systems and Software, v. 170, 110775, 2020. DOI: 10.1016/j.jss.2020.110775. Disponível em: https://doi.org/10.1016/j.jss.2020.110775. Acesso em: 30 set. 2026.

TIWARI, Abhishek; PRAKASH, Jyoti; HAMMER, Christian. Demand-driven information flow analysis of WebView in Android hybrid apps. In: IEEE INTERNATIONAL SYMPOSIUM ON SOFTWARE RELIABILITY ENGINEERING, 34., 2023. Anais [...]. 2023. p. 415-426. Disponível em: https://consensus.app/papers/demanddriven-information-flow-analysis-of-webview-in-tiwari-prakash/0e2682f2b4b45de6b72ef97a4fab3528/. Acesso em: 30 set. 2026.

## Nota sobre Context7

Esta revisão usou fontes oficiais e bibliografia acadêmica acessíveis na web. O conector Context7 não estava disponível nesta execução; quando estiver disponível, consultar suas versões de documentação Flutter, UWP/WebView e dependências antes de decisões que dependam de APIs versionadas.

## Plataformas permanentes de pesquisa

As plataformas abaixo passam a fazer parte do protocolo de pesquisa do projeto. Todo achado usado em decisão técnica deve ser registrado nesta lista ou em uma seção correlacionada, com consulta, data, identificador, fonte original, síntese, limitações e decisão impactada.

| Plataforma | Uso obrigatório | Regra de evidência |
|---|---|---|
| Context7 | Consultar documentação versionada de Flutter, Dart, UWP, WebView e dependências | Registrar versão, página consultada e data; não tratar snippet como prova suficiente |
| SciSpace | Descobrir artigos, teses, capítulos e revisões sobre WebView, TV, acessibilidade, desempenho e segurança | Preferir artigo revisado por pares; registrar DOI, autores, ano e limitações |
| Scite | Verificar contexto de citação, trabalhos que apoiam ou contrastam um achado e metadados DOI | Registrar tipo de citação e consultar texto primário antes de concluir |
| Consensus | Busca semântica inicial de literatura científica e recuperação de registros | Fazer `fetch` do resultado antes de citar; registrar URL canônica e metadados |

### Protocolo obrigatório antes de executar

1. Formular uma pergunta de pesquisa completa.
2. Pesquisar Context7 para a API e versão que será implementada.
3. Pesquisar SciSpace, Scite e Consensus para evidência acadêmica.
4. Priorizar fonte primária, documentação do fabricante e artigo revisado por pares.
5. Registrar resultados incluídos e excluídos, motivo da exclusão e limitações.
6. Transformar achado relevante em risco, requisito, teste ou decisão arquitetural.
7. Só então alterar código, workflow, manifesto ou configuração de release.

## Achados adicionados nesta revisão

### Acessibilidade em interfaces de TV

Estudos indexados no SciSpace indicam que aplicações Web para TV apresentam desafios específicos de acessibilidade e que avaliação automática não representa necessariamente a capacidade do usuário de concluir tarefas. Isso justifica testes presenciais ou remotos com controle, foco, distância de visualização e tarefas reais, além de auditoria WCAG.

- FERNANDES, Nádia et al. Evaluating the Accessibility of Adaptive TV Based Web Applications. 2013. DOI: 10.1007/978-1-4471-5082-4_9. SciSpace: https://scispace.com/search?q=Evaluating%20the%20Accessibility%20of%20Adaptive%20TV%20Based%20Web%20Applications
- COSTA, Daniel; DIAS, Ricardo; DUARTE, Carlos. A comparison of the accessibility of Web applications in TV and Desktop. 2014. Registro SciSpace: https://scispace.com/search?q=A%20comparison%20of%20the%20accessibility%20of%20Web%20applications%20in%20TV%20and%20Desktop
- COSTA, Daniel; DUARTE, Carlos. Visually impaired people and the emerging connected TV: a comparative study of TV and Web applications' accessibility. Universal Access in the Information Society, 2017. DOI: 10.1007/S10209-016-0451-6. SciSpace: https://scispace.com/search?q=Visually%20impaired%20people%20and%20the%20emerging%20connected%20TV

### Segurança de WebView e ponte híbrida

Consensus confirmou registros acadêmicos para três linhas de risco: personalização do WebView pode enfraquecer defesas esperadas do navegador; a comunicação bidirecional Web-JavaScript-nativo complica o rastreamento de fluxo; e análises em larga escala encontraram fluxos de dados potencialmente sensíveis. Esses achados são transferidos para requisitos de allowlist, CSP, ausência de ponte por padrão, validação de origem e testes negativos.

- YANG, Guangliang. When Web Meets Mobile: Novel Security Threats and Defenses in Web/Mobile Hybrid Apps. 2019. Consensus: https://consensus.app/papers/when-web-meets-mobile-novel-security-threats-and-defenses-yang/81551e894dbf5a649f7c8162e65b3143/
- TIWARI, Abhishek; PRAKASH, Jyoti; HAMMER, Christian. Demand-driven Information Flow Analysis of WebView in Android Hybrid Apps. 2023 IEEE ISSRE, p. 415-426. Consensus: https://consensus.app/papers/demanddriven-information-flow-analysis-of-webview-in-tiwari-prakash/0e2682f2b4b45de6b72ef97a4fab3528/
- TIWARI, Abhishek et al. A Large Scale Analysis of Android-Web Hybridization. Journal of Systems and Software, v. 170, 110775, 2020. DOI: 10.1016/j.jss.2020.110775. Consensus: https://consensus.app/papers/a-large-scale-analysis-of-androidweb-hybridization-tiwari-prakash/c0baa632e82351c4bf2c5a86e93ec682/
- NEUGSCHWANDTNER, Matthias; LINDORFER, Martina; PLATZER, Christian. A View to a Kill: WebView Exploitation. 2013. Consensus: https://consensus.app/papers/details/4f22f033d52857a9a229f4d5d08ec9c2/
- CHIN, Erika; WAGNER, D. Bifocals: Analyzing WebView Vulnerabilities in Android Applications. 2013. Consensus: https://consensus.app/papers/details/bd19c6e1aab9592da469aca03cd1a11f/

### Desempenho e projeto para televisão

SciSpace encontrou evidência de que limitações de hardware e comportamento de usuários de TV alteram as decisões de projeto em relação à Web convencional. Isso fundamenta benchmarks em hardware Xbox, limites de animação, tamanho de bundle, tempo de inicialização, uso de memória e latência de interação.

- LEE, Meng-Huang; ZHONG, He-Rong. Design considerations for web-based interactive TV services. International Conference on Web Engineering, 2005. DOI: 10.1007/11531371_75. SciSpace: https://scispace.com/search?q=Design%20considerations%20for%20web-based%20interactive%20TV%20services
- ALAM, Iftikhar; KHUSRO, Shah; KHAN, Mumtaz Ali. Usability Barriers in Smart TV User Interfaces: A Review and Recommendations. 2019. DOI: 10.1109/FIT47737.2019.00069. SciSpace: https://scispace.com/search?q=Usability%20Barriers%20in%20Smart%20TV%20User%20Interfaces

### Limitação de generalização

Grande parte da literatura acadêmica encontrada estuda Android WebView ou TV conectada, não o `Windows.UI.Xaml.Controls.WebView` em Xbox atual. Portanto, os resultados sustentam hipóteses e controles de risco, mas não substituem medição no Xbox. Toda decisão final deve distinguir evidência transferida, evidência Microsoft específica e evidência experimental do próprio projeto.

## Regras de atualização da base

- Achado que alterar requisito, arquitetura, risco, teste, pipeline ou release deve ser adicionado antes do merge.
- Cada referência deve informar plataforma de descoberta: Context7, SciSpace, Scite, Consensus, Microsoft Learn ou outra.
- Artigos não revisados por pares devem ser marcados como preprint, dissertação, relatório ou patente.
- Resultados de Consensus devem ser conferidos no registro completo antes da citação.
- Resultados de Scite devem registrar DOI e, quando usado, se a citação foi supporting, contrasting ou mentioning.
- Nenhuma conclusão sobre aceitação na Store deve ser baseada somente em artigo acadêmico.
