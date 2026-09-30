# ADR-0001: Spike UWP WebView antes da integração Flutter Web

- Status: proposto
- Data: 2026-09-30
- Decisores: equipe do projeto

## Contexto

O Flutter Windows atual usa runner Win32 e não comprova compatibilidade UWP/Xbox. A documentação Microsoft indica `Windows.UI.Xaml.Controls.WebView` para aplicativos Xbox (Microsoft, [s.d.]).

## Decisão

Construir primeiro um shell UWP mínimo com HTML local. Somente após execução no Windows e Xbox Developer Mode integrar o build Flutter Web.

## Consequências

- reduz o espaço de investigação inicial;
- separa risco UWP de risco Flutter Web;
- exige código nativo UWP;
- não autoriza declarar compatibilidade final;
- exige teste em hardware Xbox real.

## Referências ABNT

MICROSOFT. WebView class. [S. l.]: Microsoft Learn, [s.d.]. Disponível em: https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.controls.webview. Acesso em: 30 set. 2026.

FLUTTER. [Windows][UWP] Re-enable UWP support for Xbox app development. GitHub, 2023. Disponível em: https://github.com/flutter/flutter/issues/137045. Acesso em: 30 set. 2026.
