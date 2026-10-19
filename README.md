# Cálculo do total de pedido

Projeto em Python que calcula o total de um pedido de e-commerce combinando descontos por fidelidade, cupons promocionais e frete por peso.

## Requisitos

- Python 3.9 ou superior.
- Não há dependências externas; os testes usam `unittest`, da biblioteca padrão.

## Estrutura do projeto

```text
.
|-- .github/
|   |-- prompts/
|   |   `-- calcular-total-pedido.prompt.md
|   `-- skills/
|       `-- calcular-total-pedido/
|           `-- SKILL.md
|-- execucoes/
|   `-- 2026-10-19-ajustes-projeto.md
|-- src/
|   |-- __init__.py
|   `-- calcular_total_pedido.py
|-- tests/
|   `-- test_calcular_total_pedido.py
|-- .gitignore
|-- cleancodeForum.md
|-- LICENSE
`-- README.md
```

## Regras de negócio

1. O valor bruto dos produtos deve ser finito e maior que zero.
2. O peso total deve ser finito e maior ou igual a zero.
3. Categorias e descontos de fidelidade:

   | Categoria | Desconto |
   |---|---:|
   | `REGULAR` | 0% |
   | `VIP` | 5% |
   | `PREMIUM` | 10% |

4. O cupom `DESC10` concede 10% de desconto sobre o subtotal após o desconto de fidelidade.
5. O frete é composto por uma taxa base de R$ 15,00 mais R$ 5,00 por quilo.
6. O cupom `FRETE_GRATIS` zera o frete.
7. Cupons desconhecidos são ignorados, e cada cupom válido é aplicado no máximo uma vez.
8. O valor final é arredondado para duas casas decimais.

## Clean Code aplicado

As convenções abaixo descrevem práticas presentes na implementação, não uma certificação formal:

| Prática | Aplicação no projeto |
|---|---|
| Nomes significativos | Termos do domínio em português, `snake_case` para funções/variáveis e `UPPER_SNAKE_CASE` para constantes. |
| Responsabilidade e coesão | A função pública executa uma operação coesa de validar entradas e calcular o total; cada parte do cálculo tem uma variável nomeada. |
| Simplicidade (KISS) | Fluxo direto, sem classes, dependências ou camadas desnecessárias. |
| Guard clauses / fail fast | Entradas inválidas são rejeitadas antes do cálculo, com `ValueError` explícito. |
| Regras nomeadas | Percentuais e custos do frete ficam em constantes e em um mapeamento por categoria. |
| Testes por comportamento | Testes cobrem cálculo normal, cupons, entradas-limite e mensagens de erro. |
| Comentários úteis | Docstring breve para a função; comentários inline não são adicionados quando o próprio código já é claro. |

O guia [cleancodeForum.md](cleancodeForum.md) detalha esses princípios com exemplos e critérios para futuras alterações. As instruções correspondentes para o agente estão em [SKILL.md](.github/skills/calcular-total-pedido/SKILL.md) e no [prompt](.github/prompts/calcular-total-pedido.prompt.md).

## Como usar

Na raiz do projeto, importe a função e informe o valor bruto, a categoria, a lista de cupons e o peso:

```python
from src.calcular_total_pedido import calcular_total_pedido

total = calcular_total_pedido(
    valor_bruto=200.00,
    categoria_cliente="VIP",
    cupons=["DESC10"],
    peso_kg=2.0,
)

print(total)  # 196.0
```

O exemplo aplica 5% de desconto VIP (R$ 190,00), depois 10% pelo cupom `DESC10` (R$ 171,00) e soma R$ 25,00 de frete, resultando em R$ 196,00.

### Parâmetros

| Parâmetro | Tipo esperado | Descrição |
|---|---|---|
| `valor_bruto` | `float` | Valor dos produtos; precisa ser finito e maior que zero. |
| `categoria_cliente` | `str` | Categoria: `REGULAR`, `VIP` ou `PREMIUM`. |
| `cupons` | `list[str]` | Códigos promocionais; cupons inválidos e repetidos não são aplicados novamente. |
| `peso_kg` | `float` | Peso total do pacote; precisa ser finito e não negativo. |

## Erros de validação

A função lança `ValueError` nos seguintes casos:

| Condição | Mensagem |
|---|---|
| Valor bruto não finito (`NaN` ou infinito) | `O valor bruto do pedido deve ser um número finito.` |
| Valor bruto menor ou igual a zero | `O valor bruto do pedido deve ser maior que zero.` |
| Peso não finito (`NaN` ou infinito) | `O peso do pacote deve ser um número finito.` |
| Peso negativo | `O peso do pacote não pode ser negativo.` |
| Categoria fora dos valores aceitos | `Categoria de cliente inválida.` |

## Executar os testes

Na raiz do projeto, execute:

```powershell
python -m unittest discover -s tests -v
```

Os testes cobrem os descontos e o frete, cupons duplicados ou inválidos e as validações de entrada.
