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

- **Nomes significativos:** use nomes do domínio em português, `snake_case` para funções, parâmetros e variáveis e `UPPER_SNAKE_CASE` para constantes. Prefira intenção explícita (`total_produtos`) a abreviações vagas ou nomes genéricos.
- **Responsabilidade única e coesão:** mantenha cada função responsável por uma operação coesa. A função pública coordena validação e cálculo; extraia auxiliares somente para nomear uma regra, reduzir complexidade ou reutilizar lógica, não para fragmentar operações triviais.
- **Simplicidade (KISS) e evitar excesso (YAGNI):** prefira fluxo direto e regras evidentes. Não adicione classes, dependências, camadas ou configurações sem requisito concreto.
- **Guard clauses / fail fast:** valide no início. Rejeite valores bruto e peso não finitos ou fora dos limites, e categoria inválida, com `ValueError` e as mensagens documentadas no README.
- **Erros explícitos:** não capture exceções para ocultar falhas, não substitua entradas inválidas por valores padrão e não use `except Exception`. Cupons desconhecidos ou repetidos são exceções apenas à regra comercial: ignore-os conforme especificado, sem interromper o cálculo.
- **DRY com parcimônia:** mantenha valores de negócio nomeados em constantes e evite duplicar fórmulas, mas não crie abstrações sem reutilização ou benefício claro.
- **Comentários intencionais:** escreva docstrings curtas que expliquem o propósito. Use comentários apenas para esclarecer uma decisão ou regra não óbvia; não narre código que já é legível.
- **Testes por comportamento:** mantenha produção em `src/`, testes em `tests/` e use `unittest`. Nomeie testes `test_<comportamento>` e cubra resultados, cupons, limites (inclusive `NaN` e infinitos) e mensagens de erro. Use `subTest` para entradas variadas que validem a mesma regra.
- **Consistência e verificação:** ao mudar uma regra, atualize implementação, testes, README, este guia e o prompt relacionados. Execute `python -m unittest discover -s tests -v` e informe o resultado real; não declare testes aprovados sem executá-los.
