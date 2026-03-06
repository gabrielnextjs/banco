# Projeto 03 - Caixa Pessoal com Historico (Especificacao Completa)

## Contexto
Voce vai construir um caixa financeiro simples para controlar entradas e saidas.

## Objetivo de negocio
- Acompanhar saldo em tempo real.
- Registrar historico de movimentacoes.

## Escopo obrigatorio (MVP)
Menu:
1. Registrar entrada
2. Registrar saida
3. Ver saldo
4. Ver historico
5. Ver resumo (total entradas/saidas)
6. Sair

Movimentacao:
- tipo: `entrada` ou `saida`
- descricao: `str`
- valor: `float`

## Regras funcionais
- Saldo inicial = 0.0
- Valor deve ser > 0.
- Nao permitir saida maior que saldo.
- Historico deve manter ordem cronologica de cadastro.

## Regras tecnicas
- Funcoes minimas:
  - `registrar_entrada(movs, saldo)`
  - `registrar_saida(movs, saldo)`
  - `mostrar_saldo(saldo)`
  - `listar_historico(movs)`
  - `mostrar_resumo(movs, saldo)`
- Atualizar saldo imediatamente apos cada operacao.
- Tratar `ValueError` para valores invalidos.

## Criterios de aceite
- CA01: Entradas somam corretamente no saldo.
- CA02: Saidas subtraem corretamente no saldo.
- CA03: Saida sem saldo suficiente e bloqueada com mensagem.
- CA04: Resumo exibe totais corretos e saldo final.
- CA05: Historico apresenta todas operacoes na ordem correta.

## Casos de teste manuais
1. Entrada 100.00 -> saldo 100.00.
2. Saida 30.00 -> saldo 70.00.
3. Saida 100.00 -> bloqueada.
4. Ver resumo: entradas 100.00, saidas 30.00, saldo 70.00.

## Estrutura sugerida
- `main.py`

## Entrega esperada
- Sistema robusto contra erros de digitacao.
- Fluxo completo de caixa funcional.

## Base para consulta
- `projetos/Sistema de Controle de Estoque/main.py`
- `projetos/Calculadora de Juros Compostos/main.py`
