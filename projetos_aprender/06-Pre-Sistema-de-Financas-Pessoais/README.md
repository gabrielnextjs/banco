# Projeto 06 - Pre Sistema de Financas Pessoais (Especificacao Completa)

## Contexto
Este projeto e a pre-entrega do sistema grande.
Aqui voce junta tudo que praticou: receitas, despesas, saldo, historico e persistencia.

## Objetivo de negocio
- Dar visibilidade total da vida financeira basica do usuario.
- Preparar base tecnica para evoluir ao projeto final.

## Escopo obrigatorio (MVP)
Menu:
1. Adicionar receita
2. Adicionar despesa
3. Listar lancamentos
4. Ver resumo financeiro
5. Buscar lancamento por descricao
6. Salvar e sair

Cada lancamento:
- tipo: `receita` ou `despesa`
- descricao: `str`
- valor: `float`

Resumo financeiro deve mostrar:
- total de receitas
- total de despesas
- saldo atual
- quantidade de lancamentos

## Regras funcionais
- Valor > 0 obrigatorio.
- Nao permitir despesa maior que saldo atual.
- Buscar descricao ignorando maiusculas/minusculas.
- Salvar todos os lancamentos em arquivo texto ao sair.

## Regras tecnicas
- Funcoes minimas:
  - `adicionar_receita(lancamentos, saldo)`
  - `adicionar_despesa(lancamentos, saldo)`
  - `listar_lancamentos(lancamentos)`
  - `resumo_financeiro(lancamentos, saldo)`
  - `buscar_lancamento(lancamentos)`
  - `salvar_dados(lancamentos, saldo, caminho)`
- Validar todas entradas numericas com `try/except`.
- Usar lista de dicionarios como estrutura central.

## Criterios de aceite
- CA01: Receita aumenta saldo corretamente.
- CA02: Despesa valida reduz saldo corretamente.
- CA03: Despesa acima do saldo e bloqueada.
- CA04: Resumo mostra totais corretos apos varias operacoes.
- CA05: Busca encontra lancamentos por parte da descricao.
- CA06: Arquivo salvo ao sair com dados consistentes.

## Casos de teste manuais
1. Receita 1000 -> saldo 1000.
2. Despesa 150 -> saldo 850.
3. Despesa 900 -> bloquear.
4. Buscar `mercado` apos lancamento com essa palavra.
5. Salvar e conferir arquivo final.

## Definicao de pronto (DoD)
- Fluxo completo sem crash.
- Todas regras de negocio atendidas.
- Codigo modular com funcoes.
- Leitura do codigo clara para manutencao.

## Estrutura sugerida
- `main.py`
- `dados_financas.txt` (gerado pela execucao)

## Entrega esperada
- Projeto pronto para evoluir para o Sistema de Financas Pessoais definitivo.

## Base para consulta
- `projetos/Sistema de Controle de Estoque/main.py`
- `projetos/Criptografia de Senhas/main.py`
- `projetos/Calculadora de Juros Compostos/main.py`
