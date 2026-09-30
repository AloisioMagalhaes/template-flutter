# Registro de pesquisa

## RES-0001 — UWP WebView e Xbox

- Data: 2026-09-30
- Pergunta: qual host Web deve ser usado para um aplicativo UWP no Xbox?
- Fontes: Microsoft Learn, `WebView Class`; Microsoft Learn, `Gamepad and remote control interactions`; Flutter, `Building Windows apps`; Flutter issue #137045.
- Achado: a documentação Microsoft indica `Windows.UI.Xaml.Controls.WebView` para Xbox; WebView2 não deve ser assumido como disponível no Xbox; o Flutter Windows atual usa runner Win32 e não oferece shell UWP/Xbox oficial (Microsoft, [s.d.]; Flutter, [s.d.]; Flutter, 2023).
- Decisão: testar primeiro um shell UWP mínimo com HTML local.
- Limitação: ainda não existe execução no Xbox real.
- Requisitos afetados: RF-001, RF-002, RNF-003, RNF-007.
- Riscos afetados: R-001, R-005, R-006.
- Testes afetados: T-UWP-001, T-PKG-001.

## RES-0002 — Desempenho Flutter Web

- Data: 2026-09-30
- Pergunta: Flutter Web pode ter desempenho suficiente em dispositivo de TV/console?
- Fonte: Piskor e Badurowicz (2023), DOI 10.35784/jcsi.3677.
- Achado: o estudo encontrou tempos maiores de carregamento e reconstrução no Flutter Web em comparação ao ambiente nativo no mesmo dispositivo (Piskor e Badurowicz, 2023).
- Decisão: exigir benchmark separado para JavaScript e Wasm quando disponível.
- Limitação: estudo não foi executado em Xbox nem em UWP WebView.
- Requisitos afetados: RNF-001.
- Riscos afetados: R-002.
- Testes afetados: T-PERF-001.

## RES-0003 — Segurança de WebView híbrido

- Data: 2026-09-30
- Pergunta: quais controles devem proteger a ponte Web-JavaScript-nativa?
- Fontes: Tiwari et al. (2020), Rizzo, Cavallaro e Kinder (2017), Tiwari, Prakash e Hammer (2023).
- Achado: a literatura identifica fluxos sensíveis, interfaces abusáveis e complexidade de rastreamento entre Web e código nativo (Tiwari et al., 2020; Rizzo, Cavallaro e Kinder, 2017; Tiwari, Prakash e Hammer, 2023).
- Decisão: usar CSP, allowlist, validação de origem e ponte mínima.
- Limitação: evidência principal vem de Android WebView, não do Xbox.
- Requisitos afetados: RF-010, RF-011, RF-012, RNF-004, RNF-005.
- Riscos afetados: R-004, R-006.
- Testes afetados: T-SEC-001, T-SEC-002, T-SEC-003.

## RES-0004 — Acessibilidade e TDD

- Data: 2026-09-30
- Pergunta: como validar acessibilidade e qualidade de desenvolvimento?
- Fontes: Fernandes et al. (2013), Costa e Duarte (2017), Santos et al. (2021), Tosun, Dieste e Fucci (2017).
- Achado: avaliação automática não substitui tarefas reais em TV; efeitos de TDD variam conforme tarefa, experiência e ambiente (Fernandes et al., 2013; Costa e Duarte, 2017; Santos et al., 2021; Tosun, Dieste e Fucci, 2017).
- Decisão: combinar auditoria automática, teste orientado a tarefas e métricas de qualidade.
- Limitação: não usar TDD ou conformidade automática como garantia universal.
- Requisitos afetados: RNF-006, V-001, V-005.
- Riscos afetados: R-003, R-006.
- Testes afetados: T-ACC-001, T-GAME-001.

## Referências ABNT

COSTA, Daniel; DUARTE, Carlos. Visually impaired people and the emerging connected TV: a comparative study of TV and Web applications' accessibility. Universal Access in the Information Society, 2017. DOI: 10.1007/S10209-016-0451-6. Disponível em: https://doi.org/10.1007/S10209-016-0451-6. Acesso em: 30 set. 2026.

FERNANDES, Nádia et al. Evaluating the accessibility of adaptive TV based Web applications. 2013. DOI: 10.1007/978-1-4471-5082-4_9. Disponível em: https://doi.org/10.1007/978-1-4471-5082-4_9. Acesso em: 30 set. 2026.

FLUTTER. Building Windows apps with Flutter. [S. l.]: Flutter, [s.d.]. Disponível em: https://docs.flutter.dev/platform-integration/windows/building. Acesso em: 30 set. 2026.

FLUTTER. [Windows][UWP] Re-enable UWP support for Xbox app development. GitHub, 2023. Disponível em: https://github.com/flutter/flutter/issues/137045. Acesso em: 30 set. 2026.

PISKOR, Juliusz; BADUROWICZ, Marcin. Performance comparison of Flutter platform GUI in web and native environments. Journal of Computer Sciences Institute, 2023. DOI: 10.35784/jcsi.3677. Disponível em: https://doi.org/10.35784/jcsi.3677. Acesso em: 30 set. 2026.

RIZZO, Claudio; CAVALLARO, Lorenzo; KINDER, Johannes. BabelView: evaluating the impact of code injection attacks in mobile WebViews. arXiv, 2017. Disponível em: https://arxiv.org/abs/1709.05690. Acesso em: 30 set. 2026.

SANTOS, Adrián et al. A family of experiments on test-driven development. Empirical Software Engineering, v. 26, 2021. DOI: 10.1007/S10664-020-09895-8. Disponível em: https://doi.org/10.1007/S10664-020-09895-8. Acesso em: 30 set. 2026.

TIWARI, Abhishek et al. A large scale analysis of Android-Web hybridization. Journal of Systems and Software, v. 170, 110775, 2020. DOI: 10.1016/j.jss.2020.110775. Disponível em: https://doi.org/10.1016/j.jss.2020.110775. Acesso em: 30 set. 2026.

TIWARI, Abhishek; PRAKASH, Jyoti; HAMMER, Christian. Demand-driven information flow analysis of WebView in Android hybrid apps. In: IEEE INTERNATIONAL SYMPOSIUM ON SOFTWARE RELIABILITY ENGINEERING, 34., 2023. Anais [...]. 2023. p. 415-426. Disponível em: https://consensus.app/papers/demanddriven-information-flow-analysis-of-webview-in-tiwari-prakash/0e2682f2b4b45de6b72ef97a4fab3528/. Acesso em: 30 set. 2026.

TOSUN, Ayse; DIESTE, Oscar; FUCCI, Davide. An industry experiment on the effects of test-driven development on external quality and productivity. Empirical Software Engineering, 2017. DOI: 10.1007/S10664-016-9490-0. Disponível em: https://doi.org/10.1007/S10664-016-9490-0. Acesso em: 30 set. 2026.
