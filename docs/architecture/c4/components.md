# C4 nível 3: componentes da ponte

Estado: planejado; não representa implementação concluída.

```mermaid
flowchart LR
    W[Flutter Web] --> V[Validador de origem]
    V --> S[Validador de esquema]
    S --> A[Autorizador de método]
    A --> H[Dispatcher nativo]
    H --> R[Redactor de logs]
    R --> O[Observabilidade]
```

Nenhum componente deve executar método nativo antes de origem, esquema, tamanho, estado e autorização serem validados.
