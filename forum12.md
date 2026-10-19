# Cálculo de pedidos e aplicação de Clean Code

**Repositório:** [github.com/jennifergpaula/CleanCodeAkcit12](https://github.com/jennifergpaula/CleanCodeAkcit12)

## Problema

O projeto calcula o valor final de um pedido de e-commerce a partir do valor bruto dos produtos, da categoria de fidelidade, dos cupons promocionais e do peso do pacote. A função valida as entradas, aplica os descontos na ordem prevista, calcula o frete e retorna o total arredondado para duas casas.

## Critérios de Clean Code utilizados

- **Nomes significativos:** nomes do domínio em português e convenções Python (`snake_case` e `UPPER_SNAKE_CASE`).
- **Coesão e responsabilidade:** a função pública representa a operação de validar os dados e calcular o total; as etapas ficam visíveis em variáveis com significado.
- **Simplicidade (KISS/YAGNI):** fluxo direto, sem classes, dependências ou funções auxiliares adicionadas apenas para reduzir linhas.
- **Guard clauses / fail fast:** entradas inválidas são recusadas antes do cálculo, com exceções e mensagens específicas.
- **Regras nomeadas:** descontos e custos do frete ficam em constantes e em um mapeamento de categorias.
- **Erros explícitos:** `NaN` e infinitos são rejeitados; erros inesperados não devem ser ocultados.
- **Testes por comportamento:** casos de sucesso, cupons, limites e mensagens de erro têm nomes descritivos.
- **Comentários intencionais:** a docstring explica o propósito; comentários inline só são necessários para decisões que não estejam claras no código.
- **Consistência:** mudanças nas regras devem atualizar implementação, testes, README e instruções do agente.

## Trechos que ilustram a análise

As guard clauses rejeitam entradas não finitas antes de continuar:

```python
if not isfinite(valor_bruto):
    raise ValueError("O valor bruto do pedido deve ser um número finito.")
if valor_bruto <= 0:
    raise ValueError("O valor bruto do pedido deve ser maior que zero.")
```

Os nomes deixam explícitas as partes do cálculo e sua ordem:

```python
total_produtos = valor_bruto * (1 - DESCONTOS_FIDELIDADE[categoria_cliente])
if "DESC10" in cupons:
    total_produtos *= 0.90

frete = FRETE_BASE + (peso_kg * CUSTO_POR_QUILO)
if "FRETE_GRATIS" in cupons:
    frete = 0.0
```

## Antes e depois

**Orientação ao agente**

- **Antes:** “Use funções pequenas, nomes descritivos, guard clauses e exceções explícitas.”
- **Depois:** as instruções definem convenções de nomes, responsabilidades, quando extrair auxiliares, mensagens de validação, tratamento de erros, critérios de comentários e cenários de teste. O objetivo é tornar intenção e contrato verificáveis, não produzir menos linhas.

**Validação de números**

- **Antes:** as verificações `valor_bruto <= 0` e `peso_kg < 0` não rejeitavam `NaN` ou infinito; esses valores podiam propagar `nan` ou `inf` para o total.
- **Depois:** `math.isfinite` verifica o valor bruto e o peso, e valores não finitos causam `ValueError` com mensagens específicas. Testes cobrem `NaN`, infinito positivo e negativo.

## Orientações e sugestões

As orientações que mais ajudaram foram usar nomes do domínio, tornar explícita a sequência de descontos e frete, validar no início e escrever testes pelo comportamento. Elas facilitam entender o contrato sem depender de comentários que apenas narram o código.

- **Aceitas:** validar valores não finitos, porque impede que o cálculo retorne um total inválido; adicionar `.gitignore` para caches gerados pelo Python.
- **Adaptadas:** recomendações genéricas como “código limpo” e “funções pequenas” viraram critérios concretos para este cálculo. Não foi criada uma função auxiliar só para encurtar a função existente, que continua sendo uma operação coesa.
- **Rejeitada por ora:** migrar de `float` para `Decimal`. Isso pode ser apropriado para um sistema financeiro, mas altera a API e exige decidir requisitos de precisão, arredondamento e compatibilidade. Não era necessário para resolver os problemas identificados nesta atividade.

Reduzir linhas ou aumentar a quantidade de funções não é, isoladamente, uma melhoria: a avaliação considera clareza da intenção, correção do contrato e facilidade de verificar o comportamento.

## Verificações

Comando executado na raiz do projeto:

```powershell
python -m unittest discover -s tests -v
```

**Resultado:** 8 testes aprovados (`OK`), incluindo cálculo normal, frete grátis, cupons inválidos/duplicados, categorias e valores inválidos ou não finitos. O resultado está registrado em [execucoes/2026-10-19-ajustes-projeto.md](execucoes/2026-10-19-ajustes-projeto.md).

## Aplicação na equipe

Eu incorporaria o critério de **rastreabilidade entre regra de negócio, tratamento de erro e teste** à geração e à revisão de código. Para cada regra alterada, deve ser possível apontar o comportamento esperado, a resposta para entradas inválidas e o teste que protege cada caso.

Para praticá-lo, a equipe precisaria incluir exemplos válidos, limites e inválidos nos critérios de aceite das tarefas; fornecer esses critérios ao agente de geração e pedir testes correspondentes; usar uma lista curta de revisão que confira contrato, erros, testes e documentação; e executar a suíte relevante na integração contínua. Falhas não explicadas seriam resolvidas antes da integração. A discussão de abstrações deve se basear em benefício para o domínio e clareza, não em metas de tamanho ou contagem de funções.
