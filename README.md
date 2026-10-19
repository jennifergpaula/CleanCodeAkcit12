# Cálculo do total de pedido

Função Python para calcular o valor final de um pedido de e-commerce com descontos de fidelidade, cupons promocionais e frete por peso.

## Estrutura

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
`-- README.md
```

## Regras

- `valor_bruto` deve ser maior que zero.
- `peso_kg` deve ser maior ou igual a zero.
- `valor_bruto` e `peso_kg` devem ser números finitos; `NaN` e infinitos são rejeitados.
- As categorias aceitas são `REGULAR` (sem desconto), `VIP` (5%) e `PREMIUM` (10%).
- O cupom `DESC10` concede 10% sobre o subtotal após o desconto de fidelidade.
- O frete custa R$ 15,00 mais R$ 5,00 por quilo.
- O cupom `FRETE_GRATIS` zera o frete.
- Cupons inválidos e duplicados são ignorados; o total é arredondado para duas casas decimais.

## Uso

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

As entradas inválidas lançam `ValueError` com mensagens específicas:

- `O valor bruto do pedido deve ser maior que zero.`
- `O valor bruto do pedido deve ser um número finito.`
- `O peso do pacote não pode ser negativo.`
- `O peso do pacote deve ser um número finito.`
- `Categoria de cliente inválida.`

## Testes

Na raiz do projeto, execute:

```powershell
python -m unittest discover -s tests -v
```
