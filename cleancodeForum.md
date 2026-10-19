# Análise de Clean Code — cálculo do total de pedido

## Descrição do problema

O projeto calcula o valor final de um pedido de e-commerce aplicando descontos por fidelidade, cupons promocionais e frete baseado no peso. Também valida o valor bruto, o peso do pacote e a categoria do cliente.

## Critérios de Clean Code

As instruções do projeto estabelecem os seguintes critérios:

- Usar nomes do domínio em português, com `snake_case` para funções, parâmetros e variáveis e `UPPER_SNAKE_CASE` para constantes.
- Dar uma responsabilidade clara a cada função e criar funções auxiliares somente quando reduzirem a complexidade ou permitirem reutilização.
- Validar entradas no início, com *guard clauses*, e lançar `ValueError` com as mensagens definidas no contrato.
- Não ocultar erros inesperados nem usar capturas amplas, como `except Exception`.
- Escrever docstrings que descrevam o propósito das funções e adicionar comentários apenas para explicar decisões ou regras não óbvias.
- Cobrir resultados, limites e erros com testes nomeados pelo comportamento.
- Manter README, implementação e testes coerentes quando as regras de negócio mudarem.

## Trechos de código

As validações antecipadas tornam os casos inválidos explícitos:

```python
if valor_bruto <= 0:
    raise ValueError("O valor bruto do pedido deve ser maior que zero.")
if peso_kg < 0:
    raise ValueError("O peso do pacote não pode ser negativo.")
if categoria_cliente not in DESCONTOS_FIDELIDADE:
    raise ValueError("Categoria de cliente inválida.")
```

O cálculo mantém separados o desconto por fidelidade, o cupom promocional e o frete:

```python
total_produtos = valor_bruto * (1 - DESCONTOS_FIDELIDADE[categoria_cliente])
if "DESC10" in cupons:
    total_produtos *= 0.90

frete = FRETE_BASE + (peso_kg * CUSTO_POR_QUILO)
if "FRETE_GRATIS" in cupons:
    frete = 0.0
```

## Ajustes nas instruções do agente

**Antes:** a orientação era genérica — “Use funções pequenas, nomes descritivos, guard clauses e exceções explícitas.”

**Depois:** as instruções especificam convenções de nomes, responsabilidades das funções, quando extrair funções auxiliares, como tratar entradas inválidas e erros inesperados, e quando usar docstrings e comentários. Também indicam como manter testes e documentação alinhados.

As instruções atualizadas estão no [SKILL.md](.github/skills/calcular-total-pedido/SKILL.md) e no [prompt do cálculo](.github/prompts/calcular-total-pedido.prompt.md).

## Verificações

Após reorganizar a estrutura do projeto, os 6 testes passaram com:

```powershell
python -m unittest discover -s tests -v
```

A alteração posterior nas instruções da skill e do prompt foi revisada; como não modificou código de produção ou testes, a suíte não foi executada novamente nessa etapa.
