# Documento de Requisitos de Software e Produto

> As citações seguem a ABNT NBR 10520:2023 e as referências seguem a ABNT NBR 6023:2018. A política vinculante está em [../knowledge/abnt-citation-policy.md](../knowledge/abnt-citation-policy.md).

## 1. Identificação

- Produto: aplicativo Flutter Web hospedado em UWP WebView
- Repositório: `template-flutter`
- Plataformas-alvo: Windows e Xbox
- Artefato pretendido: um pacote MSIX UWP neutral ou x64
- Versão do documento: 1.0.0
- Data: 2026-09-30
- Estado: proposta para prototipação; não autoriza publicação

## 2. Objetivo do produto

Demonstrar, por meio de evidência experimental reproduzível, se um aplicativo Flutter Web empacotado localmente em um shell UWP com `Windows.UI.Xaml.Controls.WebView` pode ser instalado, executado e utilizado em Windows e Xbox com desempenho, segurança, privacidade, acessibilidade e navegação por controle suficientes para uma futura certificação da Microsoft Store. A escolha do WebView UWP é apoiada pela documentação da Microsoft para Xbox (Microsoft, [s.d.-a]), enquanto os requisitos de segurança da ponte decorrem de estudos de WebView híbrido (Tiwari et al., 2020; Rizzo, Cavallaro e Kinder, 2017).

O produto não deve declarar compatibilidade Xbox até que exista evidência de execução em dispositivo Xbox real e revisão dos requisitos da Store.

## 3. Escopo

### Incluído

- Shell UWP nativo.
- Conteúdo Flutter Web empacotado localmente.
- Pacote MSIX UWP.
- Execução offline do conteúdo essencial.
- Interface operável por teclado, mouse, gamepad e controle remoto.
- Navegação por foco e XY navigation.
- Pipeline CI/CD com testes, análise, segurança e empacotamento.
- Benchmark separado para Windows e Xbox.
- Threat model da ponte WebView-nativa.
- Evidências de teste, riscos e decisões versionadas.

### Excluído

- Conversão automática do Flutter Windows Win32 para UWP.
- Uso de WebView2 como requisito do Xbox.
- Garantia de certificação antes da avaliação da Microsoft.
- Download arbitrário de arquivos pelo usuário.
- Execução de código JavaScript remoto não auditado.
- Dependência obrigatória de servidor remoto para inicialização.

## 4. Usuários e partes interessadas

| Parte | Necessidade |
|---|---|
| Usuário Windows | Usar o aplicativo com mouse, teclado ou tela compatível |
| Usuário Xbox | Completar tarefas usando apenas gamepad ou controle remoto |
| Desenvolvedor Flutter | Reutilizar interface e lógica Web |
| Desenvolvedor UWP | Controlar manifesto, ciclo de vida, WebView e APIs nativas |
| Equipe DevSecOps | Produzir artefatos reproduzíveis e rastreáveis |
| Responsável por segurança | Reduzir riscos da ponte Web-JavaScript-nativa |
| Responsável por produto | Decidir avanço, pausa ou rejeição da arquitetura |
| Microsoft Store | Receber pacote conforme requisitos técnicos e políticas |

## 5. Base científica e normativa

Os estudos acadêmicos usados abaixo investigam principalmente WebView móvel ou aplicações Web para TV. Eles fundamentam hipóteses de risco e desenho de testes, mas não substituem ensaio no Xbox (Fernandes et al., 2013; Costa e Duarte, 2017; Lee e Zhong, 2005).

- Tiwari et al. (2020), *A Large Scale Analysis of Android-Web Hybridization*, DOI `10.1016/j.jss.2020.110775`: fundamenta controle de fluxos de dados e risco da comunicação WebView-nativa.
- Rizzo, Cavallaro e Kinder (2017), *BabelView*, arXiv `1709.05690`: fundamenta testes contra injeção e abuso de interfaces JavaScript.
- Fernandes et al. (2013), *Evaluating the Accessibility of Adaptive TV Based Web Applications*, DOI `10.1007/978-1-4471-5082-4_9`: fundamenta avaliação específica de aplicações Web para TV.
- Costa e Duarte (2017), *Visually impaired people and the emerging connected TV*, DOI `10.1007/S10209-016-0451-6`: fundamenta testes com usuários e insuficiência de avaliação automática.
- Lee e Zhong (2005), *Design considerations for web-based interactive TV services*, DOI `10.1007/11531371_75`: fundamenta restrições de desempenho e comportamento de usuários de TV.
- Alam, Khusro e Khan (2019), *Usability Barriers in Smart TV User Interfaces*, DOI `10.1109/FIT47737.2019.00069`: fundamenta riscos de navegação, usabilidade e acessibilidade em interfaces de TV.
- Tiwari, Prakash e Hammer (2023), *Demand-driven Information Flow Analysis of WebView in Android Hybrid Apps*, ISSRE, p. 415-426: fundamenta rastreamento bidirecional de fluxo entre Web e código nativo.
- Neugschwandtner, Lindorfer e Platzer (2013), *A View to a Kill: WebView Exploitation*: fundamenta avaliação de vulnerabilidades em WebView.
- Chin e Wagner (2013), *Bifocals: Analyzing WebView Vulnerabilities in Android Applications*: fundamenta testes de excesso de autorização e acesso indevido.

Normas e referências técnicas:

- ISO/IEC/IEEE 12207:2026: ciclo de vida e rastreabilidade.
- ISO/IEC/IEEE 29119-1:2022 e 29119-2:2021: processos e testes baseados em risco.
- ISO/IEC 29100:2024: privacidade.
- ISO/IEC 27001:2022: gestão de segurança.
- ISO 31000:2018: gestão de riscos.
- NIST SP 800-218: desenvolvimento seguro.
- NIST SP 800-207: Zero Trust.

## 6. Requisitos funcionais

### RF-001 Shell UWP

O sistema deve fornecer um shell UWP nativo que hospede o conteúdo Flutter Web em `Windows.UI.Xaml.Controls.WebView`.

Verificação: inspeção do projeto, manifesto e execução em Windows e Xbox Developer Mode.

### RF-002 Conteúdo local

O sistema deve carregar o build Flutter Web a partir do conteúdo empacotado no MSIX.

Verificação: iniciar sem rede e concluir o fluxo principal.

### RF-003 Inicialização offline

O sistema deve iniciar e exibir a tela principal sem conexão de rede.

Verificação: bloquear rede antes da execução e registrar resultado.

### RF-004 Estado de rede

O sistema deve informar indisponibilidade de rede sem travar a interface ou perder o estado local permitido.

Verificação: interromper conexão durante tarefas e executar teste de recuperação.

### RF-005 Navegação Windows

O sistema deve aceitar teclado e mouse nas tarefas definidas pelo produto.

Verificação: testes de widget, integração e execução manual.

### RF-006 Navegação Xbox

O sistema deve permitir concluir todas as tarefas críticas usando somente gamepad ou controle remoto.

Verificação: matriz de botões e execução em Xbox real.

### RF-007 Foco

O sistema deve definir foco inicial, ordem de foco, foco visual e retorno previsível em todas as telas interativas.

Verificação: testes automatizados quando possível e checklist manual de foco.

### RF-008 Navegação XY

O sistema deve permitir navegação para cima, baixo, esquerda e direita sem depender de hover ou precisão de ponteiro.

Verificação: tarefas críticas com D-pad e analógico.

### RF-009 Retorno e cancelamento

O sistema deve mapear o botão de retorno para cancelar, fechar ou retornar sem encerrar indevidamente o aplicativo.

Verificação: testes de fluxo e ciclo de vida.

### RF-010 Ponte nativa mínima

O sistema deve expor somente os métodos nativos indispensáveis ao produto.

Verificação: inventário de mensagens, métodos e capabilities.

### RF-011 Validação de mensagens

O shell deve validar origem, esquema, tipo, tamanho, estado e autorização de cada mensagem Web-JavaScript-nativa.

Verificação: testes positivos, negativos, fuzzing limitado e revisão de código.

### RF-012 Navegação externa

O sistema deve bloquear navegação externa por padrão e permitir somente domínios explicitamente aprovados.

Verificação: testes com URL permitida, não permitida, redirecionamento e esquema personalizado.

### RF-013 Downloads

O sistema não deve permitir downloads ou cópias de arquivos que não sejam necessários para a função declarada do produto.

Verificação: teste de tentativa de download e revisão de política da Store.

### RF-014 Atualização

O sistema deve permitir atualização do pacote sem perder dados locais autorizados e sem aceitar downgrade não autorizado.

Verificação: instalar versão N, atualizar para N+1 e verificar estado permitido.

### RF-015 Telemetria

O sistema deve manter telemetria desativada por padrão quando não for necessária à função principal.

Verificação: inspeção de rede, bundle, configurações e logs.

## 7. Requisitos não funcionais

### RNF-001 Desempenho

O protótipo deve medir e registrar tempo de inicialização, FPS, latência de entrada, CPU, GPU, memória e tamanho do pacote separadamente para Windows e Xbox.

Critério inicial: nenhum limite será considerado aprovado sem medição de baseline, justificativa do limite e teste no hardware-alvo.

### RNF-002 Estabilidade

O sistema não deve travar durante as tarefas críticas definidas no plano de teste.

Critério: executar a suíte de tarefas em ciclos repetidos e registrar falhas, reinícios e perda de estado.

### RNF-003 Compatibilidade

O sistema deve usar somente APIs documentadas e disponíveis no conjunto de dispositivos aprovado.

Critério: matriz de APIs com plataforma, versão, evidência e fallback.

### RNF-004 Segurança

O sistema deve aplicar HTTPS, CSP, allowlist de origem, validação de mensagens e ausência de segredos no conteúdo Web.

Critério: nenhum risco crítico aberto no threat model e nenhum teste de abuso crítico falhando.

### RNF-005 Privacidade

O sistema não deve registrar, empacotar ou transmitir PII sem finalidade, base legal, controle e documentação.

Critério: inventário de dados, inspeção do bundle e teste de logs.

### RNF-006 Acessibilidade

O sistema deve permitir tarefas críticas com foco visível, contraste adequado, textos escaláveis quando aplicável e operação por controle.

Critério: auditoria automatizada complementada por teste manual orientado a tarefas.

### RNF-007 Empacotamento

O sistema deve gerar MSIX UWP com identidade, publisher, versão, arquitetura e capabilities documentados.

Critério: instalação, inicialização, atualização e desinstalação aprovadas em cada plataforma.

### RNF-008 Reprodutibilidade

O mesmo commit deve produzir artefato equivalente, sujeito às versões registradas do SDK, dependências e ferramentas.

Critério: manifestos, lockfiles, hashes e logs de build preservados.

### RNF-009 Observabilidade

O pipeline deve produzir relatórios de testes, análise, dependências, SBOM, integridade e empacotamento sem expor segredos.

Critério: artefatos vinculados ao commit e retenção definida.

### RNF-010 Manutenibilidade

O shell nativo, a aplicação Flutter Web e a ponte devem permanecer modularizados e testáveis separadamente.

Critério: cada módulo possui responsabilidade, teste e proprietário definidos.

## 8. Requisitos de CI/CD

### CI-001 Validação de pull request

O pipeline deve executar formatação, análise estática, testes Dart/Flutter, auditoria de dependências e validação do build Web em toda pull request.

### CI-002 Build Windows

O pipeline deve gerar o build Web e o shell UWP em runner Windows com versões fixadas.

### CI-003 Build Xbox candidato

O pipeline deve gerar o mesmo MSIX candidato às duas plataformas, mas não pode declarar compatibilidade Xbox sem evidência externa anexada.

### CI-004 Proteção de segredos

Pull requests de forks não devem receber certificados, tokens, credenciais ou segredos de publicação.

### CI-005 Menor privilégio

Tokens e permissões do workflow devem ser somente leitura, exceto no job de release protegido.

### CI-006 Integridade

O pipeline deve calcular hash do bundle Web, do MSIX e dos relatórios de validação.

### CI-007 Release controlado

A publicação deve exigir merge em `main`, tag versionada, aprovação humana e ambiente protegido.

## 9. Dados e privacidade

O produto deve manter um inventário contendo dado, origem, finalidade, armazenamento, retenção, compartilhamento e descarte. Dados de teste devem ser sintéticos. Logs devem excluir tokens, identificadores pessoais, URLs sensíveis e conteúdo de formulário.

## 10. Modelo de ameaças

| Ameaça | Ativo | Controle obrigatório |
|---|---|---|
| XSS no conteúdo Web | Sessão e dados locais | CSP, sanitização e dependências fixadas |
| Página não confiável | Ponte nativa | Allowlist e validação de origem |
| Script de terceiro comprometido | Bundle Web | SRI quando aplicável, lockfile e revisão |
| Download malicioso | Armazenamento e execução | Bloqueio por padrão |
| Vazamento de PII | Logs e telemetria | Minimização, redaction e testes |
| Falsificação de release | Artefato MSIX | Ambiente protegido, assinatura e hashes |
| Regressão de input | Tarefas do usuário | Testes de gamepad e matriz de foco |

## 11. Plano de verificação e validação

### V-001 Testes unitários

Devem cobrir regras de domínio, estado, validação, roteamento e tratamento de erro.

### V-002 Testes de widget/Web

Devem cobrir renderização, foco, estados vazios, erro, loading, acessibilidade e navegação por teclado.

### V-003 Testes de integração

Devem cobrir comunicação shell-WebView, ciclo de vida, mensagens, rede e armazenamento permitido.

### V-004 Testes de segurança

Devem cobrir XSS, origem não permitida, redirecionamento, esquemas, mensagens inválidas, downloads e exposição de dados.

### V-005 Testes de gamepad

Devem cobrir D-pad, analógico, A, B, X, Y, bumpers, gatilhos, menu, voltar, foco, rolagem e recuperação após suspensão.

### V-006 Testes de desempenho

Devem comparar JavaScript e Wasm quando possível, com dataset e tarefas repetíveis.

### V-007 Testes de pacote

Devem validar identidade, assinatura, arquitetura, capabilities, instalação, atualização, desinstalação e inicialização.

### V-008 Validação de campo

Deve ocorrer em Windows suportado e Xbox real. O resultado deve conter versão do sistema, versão do pacote, hardware, passos, logs, vídeo ou evidência equivalente e decisão.

## 12. Critérios de passagem

O protótipo poderá avançar para avaliação de Store somente se:

1. Todas as tarefas críticas forem concluídas com gamepad no Xbox.
2. O aplicativo iniciar offline com o conteúdo empacotado.
3. Não houver risco crítico de segurança ou privacidade aberto.
4. O MSIX instalar, atualizar, iniciar e desinstalar nas plataformas-alvo.
5. O pipeline reproduzir o artefato e preservar evidências.
6. O manifesto e as capabilities forem revisados.
7. A política da Store for revisada para o caso de uso.
8. A revisão humana aprovar a matriz de riscos.

## 13. Critérios de rejeição ou pausa

O projeto deve ser pausado ou redirecionado para shell nativo quando:

- o Flutter Web não alcançar a meta de desempenho acordada;
- uma tarefa crítica exigir mouse ou teclado no Xbox;
- WebView, Canvas, WebGL ou armazenamento necessários não funcionarem;
- a ponte nativa não puder ser reduzida e protegida;
- o MSIX não executar no Xbox;
- houver bloqueio de certificação sem mitigação aceitável;
- o custo de manter o fork ou shell UWP superar o benefício de reutilização.

## 14. Rastreabilidade inicial

| Requisito | Risco | Teste | Evidência |
|---|---|---|---|
| RF-002 | R6 | V-008 | execução offline |
| RF-006 | R3 | V-005 | matriz de gamepad |
| RF-011 | R4 | V-004 | relatório de abuso |
| RF-013 | R7 | V-004 | teste de download |
| RNF-001 | R2 | V-006 | benchmark |
| RNF-004 | R4 | V-004 | threat model |
| RNF-007 | R5 | V-007 | validação MSIX |
| CI-004 | R4 | auditoria de workflow | logs sem segredo |
| CI-007 | R5/R7 | revisão de release | aprovação protegida |

## 15. Decisão metodológica

O desenvolvimento deve seguir TDD e desenvolvimento incremental orientado por risco: escrever o teste da capacidade, implementar o mínimo, medir no ambiente relevante, registrar o resultado e somente então ampliar o escopo. A literatura de WebView será usada para formular controles e testes; a decisão de compatibilidade Xbox dependerá da evidência experimental específica do produto.

## 15.1 Operação autônoma dos agentes

A divisão de trabalho, o contrato de relatório, os limites de autonomia e a consolidação devem seguir [docs/agents/autonomous-workflow.md](../agents/autonomous-workflow.md). Relatórios LLM são entradas de análise e não substituem evidência experimental, revisão humana, teste ou aprovação de release.

## 16. Referências

- https://doi.org/10.1016/j.jss.2020.110775
- https://arxiv.org/abs/1709.05690
- https://doi.org/10.1007/978-1-4471-5082-4_9
- https://doi.org/10.1007/S10209-016-0451-6
- https://doi.org/10.1007/11531371_75
- https://doi.org/10.1109/FIT47737.2019.00069
- https://consensus.app/papers/demanddriven-information-flow-analysis-of-webview-in-tiwari-prakash/0e2682f2b4b45de6b72ef97a4fab3528/
- https://consensus.app/papers/when-web-meets-mobile-novel-security-threats-and-defenses-yang/81551e894dbf5a649f7c8162e65b3143/
- https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.webview
- https://learn.microsoft.com/en-us/windows/apps/design/input/gamepad-and-remote-interactions
- https://learn.microsoft.com/en-us/windows/apps/publish/store-policy-archive/store-policy-7-16-1
- https://docs.flutter.dev/deployment/web
- https://docs.flutter.dev/platform-integration/windows/building

## 17. Referências em formato ABNT

COSTA, Daniel; DUARTE, Carlos. Visually impaired people and the emerging connected TV: a comparative study of TV and Web applications' accessibility. Universal Access in the Information Society, 2017. DOI: 10.1007/S10209-016-0451-6. Disponível em: https://doi.org/10.1007/S10209-016-0451-6. Acesso em: 30 set. 2026.

FERNANDES, Nádia et al. Evaluating the accessibility of adaptive TV based Web applications. 2013. DOI: 10.1007/978-1-4471-5082-4_9. Disponível em: https://doi.org/10.1007/978-1-4471-5082-4_9. Acesso em: 30 set. 2026.

LEE, Meng-Huang; ZHONG, He-Rong. Design considerations for web-based interactive TV services. International Conference on Web Engineering, 2005. DOI: 10.1007/11531371_75. Disponível em: https://doi.org/10.1007/11531371_75. Acesso em: 30 set. 2026.

MICROSOFT. Gamepad and remote control interactions. [S. l.]: Microsoft Learn, [s.d.]. Disponível em: https://learn.microsoft.com/en-us/windows/apps/design/input/gamepad-and-remote-interactions. Acesso em: 30 set. 2026.

MICROSOFT. WebView class. [S. l.]: Microsoft Learn, [s.d.]. Disponível em: https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.webview. Acesso em: 30 set. 2026.

RIZZO, Claudio; CAVALLARO, Lorenzo; KINDER, Johannes. BabelView: evaluating the impact of code injection attacks in mobile WebViews. arXiv, 2017. Disponível em: https://arxiv.org/abs/1709.05690. Acesso em: 30 set. 2026.

TIWARI, Abhishek et al. A large scale analysis of Android-Web hybridization. Journal of Systems and Software, v. 170, 110775, 2020. DOI: 10.1016/j.jss.2020.110775. Disponível em: https://doi.org/10.1016/j.jss.2020.110775. Acesso em: 30 set. 2026.

TIWARI, Abhishek; PRAKASH, Jyoti; HAMMER, Christian. Demand-driven information flow analysis of WebView in Android hybrid apps. In: IEEE INTERNATIONAL SYMPOSIUM ON SOFTWARE RELIABILITY ENGINEERING, 34., 2023. Anais [...]. 2023. p. 415-426. Disponível em: https://consensus.app/papers/demanddriven-information-flow-analysis-of-webview-in-tiwari-prakash/0e2682f2b4b45de6b72ef97a4fab3528/. Acesso em: 30 set. 2026.

FLUTTER. Build and release a web app. [S. l.]: Flutter, [s.d.]. Disponível em: https://docs.flutter.dev/deployment/web. Acesso em: 30 set. 2026.

FLUTTER. Building Windows apps with Flutter. [S. l.]: Flutter, [s.d.]. Disponível em: https://docs.flutter.dev/platform-integration/windows/building. Acesso em: 30 set. 2026.

## 18. Validação por revisão de literatura

### Método

Foi realizada busca temática nas plataformas SciSpace, Consensus e Scite, complementada por documentação oficial e DOI ou URL da fonte primária. A literatura foi usada para verificar se cada grupo de requisitos possui fundamento, identificar limitações e transformar achados em testes. A maior parte dos estudos de WebView usa Android e a maior parte dos estudos de TV usa plataformas conectadas genéricas; portanto, a validade externa para Xbox é limitada e exige experimento próprio.

### Matriz de validação

| Tópico dos requisitos | Achado da literatura | Requisitos sustentados | Situação |
|---|---|---|---|
| Shell UWP/WebView | A documentação Microsoft indica `WebView` UWP para Xbox; Flutter atual documenta Web e Windows, mas não shell UWP/Xbox oficial (Microsoft, [s.d.]; Flutter, [s.d.]; Flutter, 2023). | RF-001, RF-002, RNF-003, RNF-007 | Suportado tecnicamente; compatibilidade Xbox ainda não demonstrada |
| Flutter Web versus nativo | Estudo comparativo encontrou maior tempo de carregamento e reconstrução no Flutter Web que no ambiente nativo (Piskor e Badurowicz, 2023). | RNF-001, CI-002, V-006 | Suportado; requer benchmark no hardware-alvo |
| JavaScript/WebAssembly | A literatura sobre Web aponta que desempenho depende do runtime, carga e caminho de execução; não foi localizada evidência suficiente específica para Flutter Wasm no WebView Xbox. | RNF-001, RF-002, V-006 | Lacuna; JavaScript deve ser fallback até medição |
| WebView híbrido | Estudos identificam risco na comunicação bidirecional entre Web e nativo, incluindo fluxos de dados sensíveis, interfaces abusáveis e injeção (Tiwari et al., 2020; Rizzo, Cavallaro e Kinder, 2017; Tiwari, Prakash e Hammer, 2023). | RF-010, RF-011, RF-012, RNF-004, modelo de ameaças | Fortemente suportado; controles são obrigatórios |
| Gamepad e navegação | Microsoft recomenda navegação XY, foco visual, foco engajado e experiência de 10 pés; WebView pode exigir mouse mode (Microsoft, [s.d.]). | RF-006, RF-007, RF-008, RF-009, V-005 | Suportado oficialmente; precisa validação em Xbox |
| Acessibilidade TV | Estudos mostram desafios específicos em Web TV e que conformidade automática não garante conclusão de tarefas por usuários (Fernandes et al., 2013; Costa e Duarte, 2017). | RNF-006, RF-006, RF-007, V-005 | Suportado; exige teste baseado em tarefas |
| Desempenho TV | Estudos destacam limitações de hardware e comportamento de visualização diferentes da Web convencional (Lee e Zhong, 2005; Alam, Khusro e Khan, 2019). | RNF-001, RNF-002, V-006 | Suportado; limites devem ser definidos experimentalmente |
| Offline e cache | Flutter documenta build Web e geração de assets, mas a literatura consultada não valida o ciclo de vida offline no WebView Xbox. | RF-002, RF-003, RF-004, R6, V-008 | Parcial; validar conteúdo local, cache e retomada |
| Segurança de origem e downloads | Literatura de WebView demonstra riscos de origem, ponte e conteúdo não confiável; política Microsoft restringe navegação, download e cópia no Xbox (Tiwari et al., 2020; Microsoft, [s.d.]). | RF-012, RF-013, RNF-004, RNF-005, CI-004 | Suportado; validar contra política vigente |
| Privacidade | Estudos sobre híbridos mostram fluxos de dados entre Web e nativo; a literatura não substitui inventário e avaliação de impacto específica do produto (Tiwari et al., 2020; Tiwari, Prakash e Hammer, 2023). | RF-015, RNF-005, modelo de ameaças | Suportado como risco; controles do produto ainda devem ser implementados |
| MSIX e Store | A documentação Microsoft define requisitos de pacote, manifesto e família de dispositivo; a literatura acadêmica não determina aceitação da Store. | RF-014, RNF-007, CI-003, CI-007, V-007 | Fonte oficial necessária; certificação continua gate externo |
| TDD | Estudos empíricos encontram benefícios em alguns contextos, mas meta-análise mostra que resultado depende de tarefa, experiência e ambiente (Santos et al., 2021; Tosun, Dieste e Fucci, 2017; Bakhtiary, Gandomani e Salajegheh, 2020). | V-001, V-002, CI-001, seção 15 | Suportado com ressalvas; medir qualidade e custo no projeto |
| CI/CD e DevSecOps | A literatura encontrada não fornece evidência suficiente específica deste produto para definir limiares de segurança ou desempenho; práticas SSDF e pipeline devem ser tratadas como controles de engenharia e avaliadas por evidência interna. | CI-001 a CI-007, RNF-008, RNF-009 | Requisito metodológico; validar eficácia por métricas do pipeline |

### Síntese da revisão

1. A literatura sustenta a decisão de tratar a ponte WebView-nativa como superfície de ataque e não como simples integração técnica (Tiwari et al., 2020; Rizzo, Cavallaro e Kinder, 2017).
2. A literatura sustenta testes de acessibilidade orientados a tarefas, pois auditoria automática isolada não representa a experiência de TV (Fernandes et al., 2013; Costa e Duarte, 2017).
3. A literatura sustenta benchmarks comparativos, pois Flutter Web pode apresentar custos superiores ao ambiente nativo em carregamento e reconstrução (Piskor e Badurowicz, 2023).
4. A literatura não prova que o mesmo Flutter Web MSIX funcionará no Xbox; essa é a principal lacuna e deve ser respondida por protótipo, teste em dispositivo e certificação.
5. TDD deve ser adotado como hipótese de melhoria de qualidade, não como garantia; o projeto deve acompanhar defeitos, cobertura, tempo de desenvolvimento e retrabalho (Santos et al., 2021; Tosun, Dieste e Fucci, 2017).

### Novas referências em formato ABNT

ALAM, Iftikhar; KHUSRO, Shah; KHAN, Mumtaz Ali. Usability barriers in smart TV user interfaces: a review and recommendations. In: FRONTIERS OF INFORMATION TECHNOLOGY, 2019. Anais [...]. 2019. DOI: 10.1109/FIT47737.2019.00069. Disponível em: https://doi.org/10.1109/FIT47737.2019.00069. Acesso em: 30 set. 2026.

BAKHTIARY, Vahid; GANDOMANI, Taghi Javdani; SALAJEGHEH, Afshin. The effectiveness of test-driven development approach on software projects: a multi-case study. Bulletin of Electrical Engineering and Informatics, v. 9, n. 5, 2020. DOI: 10.11591/eei.v9i5.2533. Disponível em: https://doi.org/10.11591/eei.v9i5.2533. Acesso em: 30 set. 2026.

PISKOR, Juliusz; BADUROWICZ, Marcin. Performance comparison of Flutter platform GUI in web and native environments. Journal of Computer Sciences Institute, 2023. DOI: 10.35784/jcsi.3677. Disponível em: https://doi.org/10.35784/jcsi.3677. Acesso em: 30 set. 2026.

SANTOS, Adrián et al. A family of experiments on test-driven development. Empirical Software Engineering, v. 26, 2021. DOI: 10.1007/S10664-020-09895-8. Disponível em: https://doi.org/10.1007/S10664-020-09895-8. Acesso em: 30 set. 2026.

TOSUN, Ayse; DIESTE, Oscar; FUCCI, Davide. An industry experiment on the effects of test-driven development on external quality and productivity. Empirical Software Engineering, 2017. DOI: 10.1007/S10664-016-9490-0. Disponível em: https://doi.org/10.1007/S10664-016-9490-0. Acesso em: 30 set. 2026.
