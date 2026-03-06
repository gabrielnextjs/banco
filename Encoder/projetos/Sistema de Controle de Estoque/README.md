# Sistema de Controle de Estoque

## Visao geral
Sistema CLI para registrar pecas, consultar estoque e realizar vendas.
O objetivo e praticar CRUD basico com lista de dicionarios e escrita em arquivo.

## O que o sistema faz
- Cadastra nova peca com nome, preco e quantidade.
- Lista pecas cadastradas no estoque.
- Vende unidades de uma peca especifica.
- Salva o estado do estoque em arquivo ao sair.

## Regras principais
- Quantidade vendida nao pode ser maior que estoque disponivel.
- Produto inexistente gera aviso ao usuario.
- Entradas numericas invalidas sao tratadas com 	ry/except.

## Como executar
`ash
python main.py
`

## Arquivo principal
- main.py

## Melhorias sugeridas
- Carregar estoque salvo ao iniciar.
- Criar codigo unico por peca.
- Exibir relatorio de produtos com baixo estoque.
