# Jogo de Apostas

## Visao geral
Jogo de terminal com saldo inicial, aposta por rodada e sorteio de dado.
O usuario escolhe um modo de jogo e o sistema atualiza o saldo com base no resultado.

## O que o sistema faz
- Inicia com saldo fixo.
- Permite apostar e encerrar quando quiser.
- Modo 1: par/impar (ganha ou perde o valor apostado).
- Modo 2: numero exato (premiacao maior em caso de acerto).

## Regras principais
- A aposta deve ser maior que zero e menor ou igual ao saldo.
- Se saldo chegar a zero, o jogo termina.
- O dado e sorteado de 1 a 6 (andom.randint).

## Como executar
`ash
python main.py
`

## Arquivo principal
- main.py

## Melhorias sugeridas
- Corrigir regra de par/impar para considerar escolha do usuario.
- Criar historico de rodadas com saldo antes/depois.
- Adicionar dificuldade com multiplicadores de premio.
