# Calculadora de Juros Compostos

## Visao geral
Este projeto simula crescimento de patrimonio com aporte inicial, aportes mensais, taxa e periodo em meses.
O foco e ajudar a visualizar quanto dinheiro pode ser acumulado e quanto esse valor renderia por mes.

## O que o sistema faz
- Recebe nome, aporte inicial, tempo, taxa e aporte mensal.
- Calcula o montante mes a mes com juros compostos.
- Compara o rendimento mensal com um salario desejado.
- Exibe mensagens diferentes para cenario de meta atingida ou nao.

## Regras principais
- Valores devem ser informados em formato numerico.
- O calculo usa capitalizacao mensal.
- Existe tratamento de erro para entrada invalida (ValueError).

## Como executar
`ash
python main.py
`

## Arquivo principal
- main.py

## Melhorias sugeridas
- Separar calculo em funcao dedicada (calcular_montante).
- Validar taxa minima e maxima para evitar valores irreais.
- Salvar simulacoes em arquivo para historico.
