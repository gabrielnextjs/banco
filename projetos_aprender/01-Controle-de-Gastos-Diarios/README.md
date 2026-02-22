# Projeto 01 - Controle de Gastos Diarios (Especificacao Completa)

## Contexto
Voce foi contratado para desenvolver um modulo simples de controle de gastos diarios em terminal (CLI).
O sistema sera usado por uma pessoa para registrar despesas do dia e saber quanto gastou.

## Objetivo de negocio
- Evitar que a pessoa perca controle de pequenos gastos diarios.
- Entregar um resumo rapido do dia sem planilha.

## Escopo obrigatorio (MVP)
Implementar um menu com as opcoes:
1. Adicionar gasto
2. Listar gastos
3. Ver total gasto
4. Ver media por gasto
5. Sair

Cada gasto deve ter:
- descricao: `str`
- valor: `float`

## Regras funcionais
- Nao permitir descricao vazia.
- Nao permitir valor menor ou igual a zero.
- Armazenar gastos em memoria usando lista de dicionarios.
- Exibir valores com 2 casas decimais.

## Regras tecnicas
- Separar em funcoes:
  - `mostrar_menu()`
  - `ler_valor_positivo(mensagem)`
  - `adicionar_gasto(gastos)`
  - `listar_gastos(gastos)`
  - `calcular_total(gastos)`
  - `calcular_media(gastos)`
- Tratar `ValueError` em toda entrada numerica.
- Nao usar bibliotecas externas.

## Criterios de aceite
- CA01: Ao cadastrar 3 gastos validos, listagem mostra os 3 itens.
- CA02: Total corresponde a soma exata dos valores cadastrados.
- CA03: Media e calculada corretamente (total / quantidade).
- CA04: Se usuario digitar texto no valor, sistema nao quebra e solicita novamente.
- CA05: Se nao houver gastos, sistema informa isso em listagem/total/media.

## Casos de teste manuais
1. Cadastrar: Cafe 8.50, Uber 22.00, Lanche 15.40.
2. Validar total: 45.90.
3. Validar media: 15.30.
4. Tentar valor `abc` e validar recuperacao do erro.
5. Tentar valor `0` e `-5` e validar bloqueio.

## Estrutura sugerida
- `main.py`

## Entrega esperada
- Aplicacao rodando sem erro.
- Codigo organizado em funcoes.
- Fluxo completo funcional do menu.

## Base para consulta
- `projetos/Calculadora de Juros Compostos/main.py`
- `Aprendizado/Curso 1.5 - Fundamentos/teste.ipynb`
