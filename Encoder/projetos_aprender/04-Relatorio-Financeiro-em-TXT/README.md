# Projeto 04 - Relatorio Financeiro em TXT (Especificacao Completa)

## Contexto
A equipe precisa persistir os dados financeiros em arquivo para auditoria simples.

## Objetivo de negocio
- Garantir rastreabilidade das movimentacoes.
- Permitir consulta posterior sem executar o sistema.

## Escopo obrigatorio (MVP)
Partindo do Projeto 03, adicionar:
1. Salvar relatorio no encerramento.
2. Opcionalmente carregar relatorio anterior para consulta.

Formato minimo no arquivo:
- Cabecalho com data/hora da execucao.
- Lista de movimentacoes (tipo, descricao, valor).
- Total de entradas.
- Total de saidas.
- Saldo final.

## Regras funcionais
- Criar arquivo automaticamente se nao existir.
- Nao gravar arquivo vazio sem cabecalho.
- Formatar valores com 2 casas.

## Regras tecnicas
- Nome sugerido: `relatorio_caixa.txt`.
- Encapsular em funcao:
  - `salvar_relatorio(movs, saldo, caminho)`
- Usar `with open(..., "w", encoding="utf-8")`.

## Criterios de aceite
- CA01: Arquivo e criado ao sair.
- CA02: Conteudo do arquivo bate com dados exibidos no terminal.
- CA03: Cabecalho, corpo e resumo estao legiveis.
- CA04: Nao ocorre excecao de escrita em fluxo normal.

## Casos de teste manuais
1. Registrar 2 entradas e 1 saida.
2. Encerrar e abrir arquivo.
3. Conferir se totais e saldo final estao corretos.

## Estrutura sugerida
- `main.py`
- `relatorio_caixa.txt` (gerado pela execucao)

## Entrega esperada
- Persistencia confiavel.
- Relatorio legivel e consistente.

## Base para consulta
- `projetos/Criptografia de Senhas/main.py`
- `projetos/Sistema de Controle de Estoque/main.py`
