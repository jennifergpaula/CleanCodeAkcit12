# Clean Code aplicado ao cálculo de pedidos

## Contexto

O projeto calcula o total de um pedido a partir do valor dos produtos, da categoria de fidelidade, dos cupons promocionais e do peso do pacote. Além do cálculo, a função valida os dados de entrada e informa erros com mensagens definidas.

Este documento registra princípios de Clean Code que já podem ser observados na implementação e convenções a preservar em alterações futuras. Não é uma afirmação de conformidade formal com uma metodologia ou certificação.

## Princípios usados e evidências

| Princípio | Como é aplicado neste projeto | Evidência |
|---|---|---|
| Nomes significativos | A API e as variáveis usam termos do domínio em português; constantes têm nomes em `UPPER_SNAKE_CASE`. | `calcular_total_pedido`, `valor_bruto`, `DESCONTOS_FIDELIDADE`, `FRETE_BASE` em [src/calcular_total_pedido.py](src/calcular_total_pedido.py). |
| Responsabilidade única e coesão | A função pública representa uma operação coesa: validar os dados e calcular um total final. As etapas do cálculo são explicitadas em variáveis distintas. | `calcular_total_pedido` e `total_produtos` em [src/calcular_total_pedido.py](src/calcular_total_pedido.py). |
| Simplicidade (KISS) | O fluxo usa operações diretas e condicionais simples; não introduz classes, dependências ou camadas sem necessidade. | Aplicação do desconto promocional e cálculo do frete em [src/calcular_total_pedido.py](src/calcular_total_pedido.py). |
| Guard clauses e fail fast | Entradas inválidas são rejeitadas no início, antes do cálculo, com exceções explícitas. Valores monetários e peso também devem ser finitos. | Validações com `isfinite` e `ValueError` em [src/calcular_total_pedido.py](src/calcular_total_pedido.py). |
| Constantes para regras de negócio | Percentuais de fidelidade e valores do frete ficam nomeados em vez de espalhados pelo fluxo. | `DESCONTOS_FIDELIDADE`, `FRETE_BASE` e `CUSTO_POR_QUILO` em [src/calcular_total_pedido.py](src/calcular_total_pedido.py). |
| Tratamento explícito de regras opcionais | O desconto promocional e o frete grátis são aplicados somente quando seus cupons estão presentes. Cupons desconhecidos não causam falha. | Verificações `if "DESC10" in cupons` e `if "FRETE_GRATIS" in cupons`. |
| Testes por comportamento | Os testes nomeiam o comportamento esperado e cobrem o caminho normal, os limites e as exceções. | Casos `test_aplica_desconto_vip_cupom_e_frete`, `test_rejeita_valor_bruto_nao_finito` e demais casos em [tests/test_calcular_total_pedido.py](tests/test_calcular_total_pedido.py). |
| Documentação alinhada ao contrato | README, instruções do agente e testes descrevem as mesmas regras e mensagens de validação. | [README.md](README.md), [SKILL.md](.github/skills/calcular-total-pedido/SKILL.md) e [prompt](.github/prompts/calcular-total-pedido.prompt.md). |
| Comentários com propósito | A função usa uma docstring curta; não há comentários redundantes dentro do cálculo, que já é expresso por nomes e operações diretas. | Docstring de `calcular_total_pedido` em [src/calcular_total_pedido.py](src/calcular_total_pedido.py). |

## Regras para futuras alterações

1. **Nomes:** mantenha nomes do domínio em português. Use `snake_case` para funções, parâmetros e variáveis; `UPPER_SNAKE_CASE` para constantes. Evite abreviações vagas e nomes genéricos quando um nome específico for possível.
2. **Responsabilidades:** mantenha cada função coesa e com propósito claro. Extraia uma função auxiliar somente se ela nomear uma regra, reduzir complexidade ou permitir reutilização; não divida operações triviais só para reduzir o tamanho de uma função.
3. **Fluxo:** valide primeiro com guard clauses e mantenha a ordem do contrato: validação, desconto de fidelidade, cupom de desconto, frete e total arredondado.
4. **Erros:** preserve as mensagens documentadas para entradas inválidas. Não converta erros inesperados em resultados padrão, não use `except Exception` e não silencie falhas.
5. **Cupons:** cada cupom suportado deve afetar o cálculo no máximo uma vez; cupons desconhecidos devem seguir a regra documentada e não interromper o fluxo.
6. **Comentários:** escreva docstrings curtas sobre o propósito das funções. Adicione comentários apenas para explicar uma decisão ou regra que não esteja clara no código.
7. **Duplicação e abstrações:** mantenha regras reutilizáveis em constantes e evite repetir fórmulas. Não adicione dependências, classes ou camadas sem uma necessidade concreta.
8. **Testes:** nomeie testes como `test_<comportamento>`. Cubra resultados, cupons, limites e mensagens de erro; use `subTest` quando entradas diferentes verificarem a mesma regra.
9. **Consistência:** quando uma regra mudar, atualize implementação, testes, README e instruções do agente na mesma alteração.
10. **Verificação:** execute `python -m unittest discover -s tests -v` e relate o resultado real, inclusive falhas.

## Exemplos do código

As guard clauses rejeitam valores não finitos e entradas fora do contrato antes de calcular:

```python
if not isfinite(valor_bruto):
    raise ValueError("O valor bruto do pedido deve ser um número finito.")
if valor_bruto <= 0:
    raise ValueError("O valor bruto do pedido deve ser maior que zero.")
```

Os nomes separam o subtotal dos produtos do custo de envio:

```python
total_produtos = valor_bruto * (1 - DESCONTOS_FIDELIDADE[categoria_cliente])
if "DESC10" in cupons:
    total_produtos *= 0.90

frete = FRETE_BASE + (peso_kg * CUSTO_POR_QUILO)
if "FRETE_GRATIS" in cupons:
    frete = 0.0
```

## Verificações registradas

A suíte foi executada após as alterações de validação de valores não finitos:

```powershell
python -m unittest discover -s tests -v
```

Resultado registrado: 8 testes aprovados. Alterações exclusivamente documentais não mudam o comportamento testado; ainda assim, a suíte deve ser executada quando essas alterações forem entregues junto com mudanças de código.
