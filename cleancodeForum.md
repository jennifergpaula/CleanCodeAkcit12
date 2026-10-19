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

## Reflexão sobre as orientações e sugestões

### Orientações que tornaram a solução mais compreensível

As orientações mais úteis foram as que transformaram ideias gerais em critérios observáveis:

- **Nomes ligados ao domínio:** `valor_bruto`, `categoria_cliente`, `total_produtos` e `FRETE_BASE` ajudam a entender o cálculo sem precisar decifrar abreviações.
- **Etapas e ordem explícitas:** separar subtotal, desconto de cupom e frete deixa visível a sequência comercial e facilita comparar o código com o contrato.
- **Validação antecipada e erros específicos:** guard clauses para limites e valores não finitos tornam claro o que a função aceita e por que uma entrada é recusada.
- **Comentários com propósito:** a orientação de comentar decisões não óbvias, em vez de narrar cada linha, mantém a explicação junto ao código sem duplicar o que ele já comunica.
- **Testes por comportamento:** nomes como `test_rejeita_valor_bruto_nao_finito` mostram a regra protegida. Os testes permitem avaliar se a solução está correta, em vez de usar quantidade de linhas ou funções como medida de qualidade.

Essas orientações ajudam porque comunicam intenção, regras e limites. Não exigem simplesmente encurtar o código nem dividir uma função que já representa uma operação coesa.

### Sugestões aceitas, adaptadas e rejeitadas

- **Aceitas:** validar `NaN` e infinitos para valor bruto e peso, pois sem essa checagem o cálculo pode retornar `nan` ou `inf` em vez de um total utilizável. A validação veio acompanhada de mensagens explícitas e testes para os três valores não finitos.
- **Aceita:** adicionar regras ao `.gitignore` para caches Python, evitando que arquivos gerados sejam confundidos com código-fonte.
- **Adaptadas:** orientações genéricas como “use funções pequenas” e “escreva código limpo” foram convertidas em critérios verificáveis para este domínio: nomes de variáveis, limites de responsabilidades, ordem das regras, mensagens de erro, estilo de comentários e cenários de teste. Não se criou uma função auxiliar apenas para reduzir linhas.
- **Rejeitada por ora:** trocar `float` por `Decimal`. `Decimal` pode ser apropriado para dinheiro em sistemas de produção, mas mudaria os tipos e o contrato da função; essa mudança precisa de um requisito explícito de precisão e de compatibilidade, além de testes e decisão sobre arredondamento. No escopo atual, a alteração não era necessária para resolver o problema identificado.

### Aplicação na empresa

Eu incorporaria à geração e revisão de código o critério de **rastreabilidade entre regra, tratamento de erro e teste**. Para cada regra ou validação alterada, a proposta deve indicar o comportamento esperado, a resposta para entradas inválidas e o teste que protege esse comportamento. O revisor confirma essa correspondência, não a quantidade de linhas, funções ou comentários.

Para colocar isso em prática, a equipe precisaria ajustar a rotina de trabalho:

1. Ao abrir uma tarefa, registrar critérios de aceite observáveis e exemplos de entradas válidas, limites e inválidas.
2. Incluir esses critérios no contexto usado para gerar código e pedir que a ferramenta proponha ou atualize os testes correspondentes.
3. Na revisão, usar uma lista curta: contrato atendido, erros explícitos, testes cobrindo os cenários e documentação atualizada quando necessário.
4. Executar a suíte relevante na integração contínua e tratar falhas como bloqueio até serem explicadas ou corrigidas.
5. Discutir abstrações pela clareza e pela necessidade do domínio, não por metas de reduzir linhas ou aumentar a quantidade de funções.

Esse processo adiciona uma verificação focada ao fluxo existente, sem transformar Clean Code em uma lista de métricas superficiais.
