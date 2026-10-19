---
name: calcular-total-pedido
description: "Use ao implementar, revisar ou testar o cálculo do total de pedidos e-commerce em Python, incluindo descontos de fidelidade, cupons, frete e validações."
---

# Cálculo de total de pedido

## Quando usar

- Alterar as regras de preço, desconto promocional ou frete.
- Corrigir validações de entradas do pedido.
- Adicionar cenários ou revisar testes do cálculo do total.

## Procedimento

1. Leia a implementação em `src/calcular_total_pedido.py`, os testes em `tests/test_calcular_total_pedido.py` e o contrato documentado no `README.md`.
2. Preserve as mensagens de `ValueError` especificadas para valor bruto inválido, peso inválido e categoria inválida. Rejeite também valores não finitos (`NaN` e infinito) para valor bruto e peso.
3. Mantenha independentes as regras de desconto por fidelidade, cupom `DESC10` e frete, respeitando sua ordem de aplicação.
4. Garanta que cada cupom válido afete o pedido no máximo uma vez; cupons desconhecidos não devem interromper o cálculo.
5. Atualize os testes para cobrir o comportamento alterado, incluindo limites e erros relevantes.
6. Execute `python -m unittest discover -s tests -v` e informe claramente qualquer falha.

## Convenções e critérios de Clean Code

- Mantenha a lógica de produção em `src/` e os testes em `tests/`. Use a biblioteca padrão `unittest` e preserve o comando de descoberta documentado no README.
- Use português nos nomes do domínio e siga `snake_case` para funções, parâmetros e variáveis (`calcular_total_pedido`, `valor_bruto`). Use `UPPER_SNAKE_CASE` para constantes (`FRETE_BASE`). Escolha nomes que expliquem o papel ou significado do valor; evite abreviações vagas e nomes genéricos como `x`, `dados` ou `resultado` quando houver um nome mais específico.
- Dê a cada função uma responsabilidade clara. A função pública coordena validação e cálculo; extraia uma regra para uma função auxiliar apenas quando isso tornar a lógica mais clara ou reutilizável, sem fragmentar operações triviais.
- Mantenha a validação no início da função com guard clauses. Para valor bruto e peso não finitos ou fora dos limites, e categoria inválida, lance `ValueError` com as mensagens definidas no README. Não capture essas exceções para ocultar o erro nem substitua entradas inválidas por valores padrão.
- Ignore cupons desconhecidos ou repetidos como regra de negócio explícita; não trate esse caso como exceção. Não introduza capturas amplas (`except Exception`) nem falhas silenciosas para outros erros inesperados.
- Escreva docstrings curtas que descrevam o propósito da função e comentários somente quando explicarem uma decisão ou regra não óbvia. Não use comentários para repetir o que o código já expressa.
- Mantenha o fluxo e as regras de negócio fáceis de seguir, sem duplicar cálculos ou adicionar abstrações que não sejam necessárias. Preserve o arredondamento final para duas casas decimais.
- Nomeie testes como `test_<comportamento>` e cubra resultados esperados, cupons, limites (incluindo `NaN` e infinito) e mensagens de erro relevantes. Ao alterar uma regra, atualize os testes e o README para manter implementação, especificação e documentação consistentes.
