---
description: "Implementar ou revisar o cálculo do total de um pedido e-commerce em Python."
name: "Calcular total do pedido"
argument-hint: "Descreva a alteração ou cenário desejado para o cálculo do pedido."
---

Implemente ou revise o cálculo do total de um pedido de e-commerce em Python, seguindo as convenções abaixo e os padrões existentes do projeto.

Regras de negócio:
- Validar valor bruto finito e maior que zero, peso finito e não negativo e categoria entre `REGULAR`, `VIP` e `PREMIUM`.
- Aplicar 0% de desconto para `REGULAR`, 5% para `VIP` e 10% para `PREMIUM`.
- Aplicar `DESC10` uma única vez sobre o subtotal já descontado por fidelidade.
- Calcular frete como R$ 15,00 mais R$ 5,00 por quilo; `FRETE_GRATIS` zera o frete.
- Ignorar cupons inválidos e duplicados.
- Retornar o total arredondado para duas casas decimais.

Convenções de implementação:
- Mantenha código de produção em `src/` e testes em `tests/`; use `unittest` e preserve `python -m unittest discover -s tests -v`.
- Use nomes do domínio em português, com `snake_case` para funções, parâmetros e variáveis e `UPPER_SNAKE_CASE` para constantes. Prefira nomes que revelem significado e intenção, sem abreviações vagas.
- Dê a cada função uma responsabilidade clara. A função pública coordena o cálculo; extraia auxiliares somente quando reduzirem complexidade ou possibilitarem reutilização, sem fragmentar operações triviais.
- Valide primeiro com guard clauses. Para valor bruto, peso e categoria inválidos, lance `ValueError` com as mensagens exatas definidas no contrato; não oculte erros com capturas ou valores padrão.
- Rejeite `NaN` e infinitos para valor bruto e peso, usando `math.isfinite` e as mensagens documentadas no README.
- Ignore cupons inválidos ou duplicados conforme a regra de negócio, sem transformar esse caso em erro. Não use `except Exception` nem silencie erros inesperados.
- Use docstrings curtas para explicar o propósito das funções. Comente apenas decisões ou regras não óbvias; não repita em comentários o que os nomes e o código já deixam claro.
- Evite duplicação e abstrações desnecessárias, preserve o arredondamento final e mantenha README, implementação e testes coerentes.

Atualize ou adicione testes nomeados por comportamento para validar resultados, limites (inclusive `NaN` e infinitos) e erros relevantes. Execute `python -m unittest discover -s tests -v` e informe claramente qualquer falha.
