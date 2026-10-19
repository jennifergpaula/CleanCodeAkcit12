# Registro de execução — ajustes do projeto

**Data:** 2026-10-19

## Ajustes realizados

- Adicionada validação de finitude para `valor_bruto` e `peso_kg`; entradas `NaN`, `inf` e `-inf` agora lançam `ValueError` com mensagens explícitas.
- Adicionados testes para cada tipo de valor não finito em ambos os parâmetros.
- Criado `.gitignore` para excluir `__pycache__/` e arquivos Python compilados.
- Atualizados o README, a skill e o prompt para documentar e preservar as validações.
- Atualizada a árvore de arquivos do README para incluir `execucoes/`, `.gitignore` e `cleancodeForum.md`.
- Documentados os princípios de Clean Code efetivamente observáveis (nomes significativos, coesão, simplicidade, guard clauses, regras nomeadas, erros explícitos, testes por comportamento e documentação alinhada) e as convenções a seguir em futuras alterações.

## Verificação

Comando executado:

```powershell
python -m unittest discover -s tests -v
```

Resultado: 8 testes aprovados.
