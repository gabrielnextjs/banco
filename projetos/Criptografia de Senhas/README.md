# Criptografia de Senhas

## Visao geral
Projeto de criptografia simples por deslocamento de caracteres.
O usuario pode codificar ou decodificar uma senha usando uma chave numerica.

## O que o sistema faz
- Mostra menu com opcoes de codificar, decodificar e sair.
- Converte cada caractere para codigo numerico (ord), aplica deslocamento e reconverte (chr).
- Salva senhas codificadas em arquivo texto para consulta futura.

## Regras principais
- A chave deve ser numerica.
- Entradas invalidas no menu sao tratadas com 	ry/except.
- O metodo nao e criptografia forte; e apenas educativo.

## Como executar
`ash
python main.py
`

## Arquivos principais
- main.py
- senhas_salvas.txt

## Melhorias sugeridas
- Permitir escolher arquivo de saida.
- Adicionar limite de chave para evitar caracteres invalidos.
- Implementar versao com cifra de Vigenere para comparar abordagens.
