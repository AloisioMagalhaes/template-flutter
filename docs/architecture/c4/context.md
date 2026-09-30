# C4 nível 1: contexto

Estado: vigente para prototipação; Xbox não validado.

```mermaid
C4Context
    Person(windows, "Usuário Windows", "Usa mouse ou teclado")
    Person(xbox, "Usuário Xbox", "Usa gamepad ou controle remoto")
    System(app, "Template Flutter", "Flutter Web hospedado em shell UWP WebView")
    System_Ext(store, "Microsoft Store", "Distribuição e certificação")
    System_Ext(network, "Rede externa", "Somente origens permitidas")
    Rel(windows, app, "Usa")
    Rel(xbox, app, "Usa")
    Rel(app, store, "Envia pacote para avaliação")
    Rel(app, network, "Acessa HTTPS permitido")
```

O diagrama mostra o objetivo do sistema e suas fronteiras. Compatibilidade Xbox depende de evidência em dispositivo real.
