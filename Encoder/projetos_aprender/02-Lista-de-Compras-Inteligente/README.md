# Projeto 02 - Lista de Compras Inteligente (Especificacao Completa)

## Contexto
Uma pessoa precisa organizar compras de mercado e acompanhar o que ja foi comprado.

## Objetivo de negocio
- Reduzir esquecimento de itens.
- Facilitar visualizacao de pendencias.

## Escopo obrigatorio (MVP)
Menu:
1. Adicionar item
2. Listar itens
3. Marcar item como comprado
4. Remover item
5. Buscar item
6. Sair

Cada item deve ter:
- nome: `str`
- quantidade: `int`
- comprado: `bool`

## Regras funcionais
- Nome nao pode ser vazio.
- Quantidade deve ser inteiro > 0.
- Busca deve ignorar maiusculas/minusculas.
- Nao duplicar item com mesmo nome (case insensitive).
- Ao marcar como comprado, item deve mudar para `comprado=True`.

## Regras tecnicas
- Funcoes minimas:
  - `adicionar_item(lista)`
  - `listar_itens(lista)`
  - `marcar_comprado(lista)`
  - `remover_item(lista)`
  - `buscar_item(lista)`
- Usar lista de dicionarios.
- Tratar entradas invalidas com `try/except`.

## Criterios de aceite
- CA01: Item cadastrado aparece na listagem com quantidade correta.
- CA02: Marcacao de comprado muda status sem duplicar item.
- CA03: Remocao funciona para item existente e informa se nao encontrado.
- CA04: Busca retorna resultados corretos ignorando caixa.
- CA05: Sistema nao quebra em entradas invalidas.

## Casos de teste manuais
1. Adicionar `Arroz`, qtd 2.
2. Adicionar `arroz`, validar bloqueio de duplicidade.
3. Marcar `Arroz` como comprado.
4. Buscar `ARROZ` e validar resultado.
5. Remover `Arroz` e validar lista vazia.

## Estrutura sugerida
- `main.py`

## Entrega esperada
- CRUD funcional no terminal.
- Codigo com funcoes pequenas e legiveis.

## Base para consulta
- `projetos/Sistema de Cadastro de Membros/main.py`
- `Aprendizado/Curso 1.15 - Logica e Estruturas/indices.ipynb`
