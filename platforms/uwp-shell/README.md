# UWP WebView spike

Estado: scaffold implementado; execução e empacotamento ainda não aprovados.

O shell carrega `ms-appx-web:///Assets/index.html` e cancela navegação que não use o esquema local `ms-appx-web`. O HTML é fixture mínimo; ainda não contém o build Flutter Web.

## Validação pendente

- compilar com Visual Studio e Windows SDK UWP;
- fornecer os assets gráficos exigidos pelo manifesto;
- instalar e executar em Windows compatível;
- testar em Xbox Developer Mode;
- anexar logs, versão, hash e evidência de execução.

A ausência de MSBuild/.NET UWP neste ambiente impede declarar T-UWP-001 como aprovado.
