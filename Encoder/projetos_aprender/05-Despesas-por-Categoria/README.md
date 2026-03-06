# Projeto 05 - Despesas por Categoria (Especificacao Completa)

## Contexto
Agora o foco e analise: entender para onde o dinheiro esta indo.

## Objetivo de negocio
- Classificar gastos por categoria.
- Identificar maior centro de custo.

## Escopo obrigatorio (MVP)
Menu:
1. Adicionar despesa
2. Listar despesas
3. Ver total por categoria
4. Ver categoria com maior gasto
5. Ver percentual por categoria
6. Sair

Categorias permitidas:
- alimentacao
- transporte
- lazer
- estudos
- moradia
- saude
- outros

Cada despesa:
- descricao: `str`
- categoria: `str`
- valor: `float`

## Regras funcionais
- Categoria fora da lista deve ser rejeitada.
- Valor deve ser > 0.
- Total por categoria deve ser acumulado corretamente.
- Percentual = (total_categoria / total_geral) * 100.

## Regras tecnicas
- Funcoes minimas:
  - `adicionar_despesa(lista)`
  - `listar_despesas(lista)`
  - `total_por_categoria(lista)`
  - `categoria_maior_gasto(lista)`
  - `percentual_por_categoria(lista)`
- Normalizar categoria para minusculo.

## Criterios de aceite
- CA01: Sistema recusa categoria invalida.
- CA02: Totais por categoria estao corretos.
- CA03: Categoria de maior gasto e exibida corretamente.
- CA04: Percentuais somam aproximadamente 100%.

## Casos de teste manuais
1. Cadastrar 3 despesas em categorias diferentes.
2. Validar totais individuais.
3. Validar categoria de maior gasto.
4. Validar percentuais no resumo.

## Estrutura sugerida
- `main.py`

## Entrega esperada
- Relatorio por categoria claro e correto.
- Codigo pronto para integrar no sistema final.

## Base para consulta
- `Aprendizado/Curso 1.15 - Logica e Estruturas/indices.ipynb`
- `projetos/Sistema de Cadastro de Membros/main.py`
