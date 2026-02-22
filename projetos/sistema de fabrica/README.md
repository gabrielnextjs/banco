# Sistema de Fabrica

## Visao geral
Simulacao de linha de producao de garrafas com controle de qualidade por peso.
Garrafas aprovadas e rejeitadas sao registradas em arquivos separados.

## O que o sistema faz
- Gera lote de garrafas com peso aleatorio.
- Aprova garrafas dentro da faixa de peso definida.
- Registra rejeicoes fora da faixa.
- Agrupa garrafas aprovadas em caixas de tamanho fixo.
- Salva dados de caixas, aprovadas e rejeitadas em arquivos texto.

## Regras principais
- Faixa de aprovacao: 490g a 510g.
- Cada caixa fecha com 6 garrafas aprovadas.
- Cada garrafa possui codigo e lote para rastreio.

## Como executar
`ash
python main.py
`

## Arquivo principal
- main.py

## Melhorias sugeridas
- Tornar faixa de peso configuravel.
- Mostrar resumo final (total aprovado, rejeitado, caixas fechadas).
- Persistir dados em formato estruturado (json/csv).
