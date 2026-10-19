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
- Use nomes do domínio em português, com `snake_case` para funções, parâmetros e variáveis e `UPPER_SNAKE_CASE` para constantes. Prefira nomes que expressem intenção, como `total_produtos`, e evite abreviações vagas.
- Mantenha cada função coesa e com responsabilidade clara. A função pública coordena validação e cálculo; extraia auxiliares somente para nomear uma regra, reduzir complexidade ou reutilizar lógica, sem fragmentar operações triviais (SRP).
- Prefira fluxo simples, direto e suficiente para o requisito (KISS/YAGNI); não introduza classes, dependências ou camadas sem benefício concreto.
- Valide primeiro com guard clauses. Para valor bruto, peso e categoria inválidos, lance `ValueError` com as mensagens exatas do README; não oculte exceções nem use valores padrão para entradas inválidas (fail fast).
- Rejeite `NaN` e infinitos para valor bruto e peso, usando `math.isfinite` e as mensagens documentadas no README.
- Ignore cupons inválidos ou duplicados conforme a regra de negócio, sem transformar esse caso em erro. Não use `except Exception`, não masque erros e evite padrões e fórmulas duplicados (DRY com parcimônia).
- Use docstrings curtas para explicar o propósito das funções. Comente apenas decisões ou regras não óbvias; não repita em comentários o que os nomes e o código já deixam claro.
- Preserve o arredondamento final e mantenha README, implementação, testes, skill e prompt coerentes. Consulte [cleancodeForum.md](../../cleancodeForum.md) para exemplos dos princípios aplicados.

Atualize ou adicione testes `unittest` nomeados por comportamento para validar resultados, limites (inclusive `NaN` e infinitos) e erros relevantes; use `subTest` para validar entradas diferentes sob a mesma regra. Execute `python -m unittest discover -s tests -v` e informe claramente o resultado, sem declarar sucesso se não executou a suíte.
