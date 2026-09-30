# Matriz de rastreabilidade requisito-risco-teste-evidência

As citações seguem ABNT NBR 10520:2023 e as referências seguem ABNT NBR 6023:2018. `acadêmica` identifica literatura científica; `oficial` identifica documentação técnica; `normativa` identifica norma; `inferência` identifica decisão do projeto.

| ID | Requisito | Risco | Teste | Evidência | Fundamentação explícita | Estado |
|---|---|---|---|---|---|---|
| RF-001 | Shell UWP com WebView | R-001 | T-UWP-001 | build e execução UWP | oficial: Microsoft ([s.d.-a]); inferência arquitetural baseada na lacuna Flutter UWP/Xbox (Flutter, 2023) | planejado |
| RF-002 | Conteúdo Flutter Web local | R-001/R-006 | T-WEB-001 | bundle local e hash | oficial: Flutter ([s.d.]); inferência: reduz dependência de rede | planejado |
| RF-003 | Inicialização offline | R-006 | T-OFF-001 | execução sem rede | hipótese do projeto; sem evidência acadêmica específica para Xbox | planejado |
| RF-006 | Operação por gamepad | R-003 | T-GAME-001 | matriz de controles | oficial: Microsoft ([s.d.-c]); acadêmica: Fernandes et al. (2013) e Alam, Khusro e Khan (2019) | planejado |
| RF-007 | Foco visual e ordem de foco | R-003 | T-ACC-001 | checklist orientado a tarefas | oficial: Microsoft ([s.d.-c]); acadêmica: Costa e Duarte (2017) | planejado |
| RF-011 | Validação da ponte nativa | R-004 | T-SEC-001 | testes negativos | acadêmica: Tiwari et al. (2020), Rizzo, Cavallaro e Kinder (2017) e Tiwari, Prakash e Hammer (2023) | planejado |
| RF-012 | Allowlist de origens | R-004 | T-SEC-002 | URLs permitidas e bloqueadas | acadêmica: Tiwari et al. (2020); inferência de hardening | planejado |
| RF-013 | Bloqueio de downloads | R-005 | T-STORE-001 | teste de política | oficial: Microsoft ([s.d.-d]); inferência de menor privilégio | planejado |
| RNF-001 | Desempenho mensurável | R-002 | T-PERF-001 | startup, FPS, memória e latência | acadêmica: Piskor e Badurowicz (2023), Lee e Zhong (2005) e Alam, Khusro e Khan (2019) | planejado |
| RNF-004 | Segurança WebView | R-004 | T-SEC-003 | threat model e relatório | acadêmica: Tiwari et al. (2020), Rizzo, Cavallaro e Kinder (2017) e Neugschwandtner, Lindorfer e Platzer (2013) | planejado |
| RNF-005 | Privacidade | R-004/R-006 | T-PRIV-001 | inventário e logs | normativa: ISO/IEC 29100:2024; acadêmica: Tiwari, Prakash e Hammer (2023); minimização é inferência | planejado |
| RNF-007 | MSIX UWP | R-005 | T-PKG-001 | instalar, atualizar e remover | oficial: Microsoft ([s.d.-e]); certificação é gate externo | planejado |
| CI-001 | Testes em pull request | R-007 | T-CI-001 | GitHub Actions | normativa: NIST (2022); acadêmica: Santos et al. (2021) e Tosun, Dieste e Fucci (2017) | planejado |
| CI-004 | Segredos isolados | R-004 | T-CI-002 | auditoria de permissões | normativa: NIST (2022); Zero Trust é decisão de controle | planejado |
| CI-007 | Release protegida | R-005 | T-CI-003 | aprovação e artefato | normativa: ISO/IEC/IEEE 12207:2026 e NIST (2022); governança é decisão do projeto | planejado |

## Limitações

Os estudos de WebView citados investigam principalmente Android, e os estudos de TV investigam plataformas conectadas genéricas. Eles sustentam hipóteses, controles e testes, mas não provam compatibilidade Xbox. Execução em Windows e Xbox real continua obrigatória.

## Regras

- `planejado` só muda para `aprovado` com evidência anexada.
- Testes Xbox recebem `hardware-required`.
- Nenhum requisito termina sem teste, risco e evidência.
- Toda alteração atualiza `docs/observability/work-log.md`.
- Toda citação possui referência identificável abaixo.
- Toda inferência é hipótese do projeto, não afirmação da fonte.

## Referências ABNT

ALAM, Iftikhar; KHUSRO, Shah; KHAN, Mumtaz Ali. Usability barriers in smart TV user interfaces. In: FRONTIERS OF INFORMATION TECHNOLOGY, 2019. DOI: 10.1109/FIT47737.2019.00069. Disponível em: https://doi.org/10.1109/FIT47737.2019.00069. Acesso em: 30 set. 2026.

COSTA, Daniel; DUARTE, Carlos. Visually impaired people and the emerging connected TV. Universal Access in the Information Society, 2017. DOI: 10.1007/S10209-016-0451-6. Disponível em: https://doi.org/10.1007/S10209-016-0451-6. Acesso em: 30 set. 2026.

FERNANDES, Nádia et al. Evaluating the accessibility of adaptive TV based Web applications. 2013. DOI: 10.1007/978-1-4471-5082-4_9. Disponível em: https://doi.org/10.1007/978-1-4471-5082-4_9. Acesso em: 30 set. 2026.

FLUTTER. Build and release a web app. [S. l.]: Flutter, [s.d.]. Disponível em: https://docs.flutter.dev/deployment/web. Acesso em: 30 set. 2026.

FLUTTER. [Windows][UWP] Re-enable UWP support for Xbox app development. GitHub, 2023. Disponível em: https://github.com/flutter/flutter/issues/137045. Acesso em: 30 set. 2026.

LEE, Meng-Huang; ZHONG, He-Rong. Design considerations for web-based interactive TV services. 2005. DOI: 10.1007/11531371_75. Disponível em: https://doi.org/10.1007/11531371_75. Acesso em: 30 set. 2026.

MICROSOFT. WebView class. [S. l.]: Microsoft Learn, [s.d.-a]. Disponível em: https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.webview. Acesso em: 30 set. 2026.

MICROSOFT. Gamepad and remote control interactions. [S. l.]: Microsoft Learn, [s.d.-c]. Disponível em: https://learn.microsoft.com/en-us/windows/apps/design/input/gamepad-and-remote-interactions. Acesso em: 30 set. 2026.

MICROSOFT. Store policy archive. [S. l.]: Microsoft Learn, [s.d.-d]. Disponível em: https://learn.microsoft.com/en-us/windows/apps/publish/store-policy-archive/store-policy-7-16-1. Acesso em: 30 set. 2026.

MICROSOFT. Windows app package and deployment documentation. [S. l.]: Microsoft Learn, [s.d.-e]. Disponível em: https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/. Acesso em: 30 set. 2026.

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. Secure software development framework version 1.1: NIST SP 800-218. Gaithersburg: NIST, 2022. DOI: 10.6028/NIST.SP.800-218. Disponível em: https://doi.org/10.6028/NIST.SP.800-218. Acesso em: 30 set. 2026.

NEUGSCHWANDTNER, Michael; LINDORFER, Martina; PLATZER, Christian. A view to a kill: WebView exploitation. 2013. DOI: 10.1007/978-3-642-41383-4_8. Disponível em: https://doi.org/10.1007/978-3-642-41383-4_8. Acesso em: 30 set. 2026.

PISKOR, Juliusz; BADUROWICZ, Marcin. Performance comparison of Flutter platform GUI in web and native environments. Journal of Computer Sciences Institute, 2023. DOI: 10.35784/jcsi.3677. Disponível em: https://doi.org/10.35784/jcsi.3677. Acesso em: 30 set. 2026.

RIZZO, Claudio; CAVALLARO, Lorenzo; KINDER, Johannes. BabelView: evaluating the impact of code injection attacks in mobile WebViews. arXiv, 2017. Disponível em: https://arxiv.org/abs/1709.05690. Acesso em: 30 set. 2026.

SANTOS, Adrián et al. A family of experiments on test-driven development. Empirical Software Engineering, v. 26, 2021. DOI: 10.1007/S10664-020-09895-8. Disponível em: https://doi.org/10.1007/S10664-020-09895-8. Acesso em: 30 set. 2026.

TIWARI, Abhishek et al. A large scale analysis of Android-Web hybridization. Journal of Systems and Software, v. 170, 110775, 2020. DOI: 10.1016/j.jss.2020.110775. Disponível em: https://doi.org/10.1016/j.jss.2020.110775. Acesso em: 30 set. 2026.

TIWARI, Abhishek; PRAKASH, Jyoti; HAMMER, Christian. Demand-driven information flow analysis of WebView in Android hybrid apps. In: IEEE INTERNATIONAL SYMPOSIUM ON SOFTWARE RELIABILITY ENGINEERING, 34., 2023. p. 415-426. Disponível em: https://consensus.app/papers/demanddriven-information-flow-analysis-of-webview-in-tiwari-prakash/0e2682f2b4b45de6b72ef97a4fab3528/. Acesso em: 30 set. 2026.

TOSUN, Ayse; DIESTE, Oscar; FUCCI, Davide. An industry experiment on the effects of test-driven development on external quality and productivity. Empirical Software Engineering, 2017. DOI: 10.1007/S10664-016-9490-0. Disponível em: https://doi.org/10.1007/S10664-016-9490-0. Acesso em: 30 set. 2026.
