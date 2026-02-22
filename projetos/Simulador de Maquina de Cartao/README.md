# Simulador de Maquina de Cartao

## Visao geral
Simulador de fluxo de pagamento com dois metodos: cartao ou pix.
No metodo cartao, ha validacao de senha com limite de tentativas.

## O que o sistema faz
- Recebe metodo de pagamento (1 cartao, 2 pix).
- Em cartao: solicita senha e bloqueia apos 3 erros.
- Em pix: aprova pagamento direto.
- Exibe retorno final do processamento.

## Regras principais
- Metodo invalido e rejeitado.
- Cartao bloqueia ao atingir 3 tentativas incorretas.
- Pagamento so aprova no cartao se senha estiver correta.

## Como executar
`ash
python main.py
`

## Arquivo principal
- main.py

## Melhorias sugeridas
- Ocultar senha durante digitacao.
- Salvar tentativas em log.
- Permitir valor da compra e comprovante.
