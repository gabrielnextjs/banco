# =========================================================
# O LAÇO 'FOR' COM range()
# =========================================================
for i in range(1, 11, 2):
    print(f"Número ímpar: {i}")

for i in range(10, 0, -1):
    print(f"Lançando em {i}...")

# =========================================================
# enumerate() - O ÍNDICE GRÁTIS
# =========================================================
carrinho = ["Placa Mãe", "Memória RAM", "SSD M.2"]
for posicao, peca in enumerate(carrinho, start=1):
    print(f"Item {posicao}: {peca}")

# =========================================================
# zip() - O ZÍPER DE LISTAS
# =========================================================
jogadores = ["SnipeKing", "SGP_Dev", "Renegado77"]
pontuacoes = [4200, 3850, 5100]
for jogador, pontos in zip(jogadores, pontuacoes):
    print(f"{jogador}: {pontos} pontos")

chaves = ["nome", "nivel", "guilda"]
valores = ["SGP", 99, "STREET"]
perfil = dict(zip(chaves, valores))
print(perfil)

# =========================================================
# O LAÇO 'WHILE' COM MENU DE SISTEMA
# =========================================================
# Exemplo interativo original preservado como referência.
# while True:
#     print("\n[1] Ligar Esteira  [2] Desligar e Sair")
#     opcao = input("Digite a opção: ")
#
#     if opcao == "1":
#         print("Esteira operando...")
#         print("Garrafa defeituosa detectada!")
#         continue
#     elif opcao == "2":
#         print("Desligando motores...")
#         break
#     else:
#         print("Opção inválida.")

# =========================================================
# FOR...ELSE
# =========================================================
numeros = [2, 4, 6, 8, 10]
for n in numeros:
    if n % 2 != 0:
        print(f"Número ímpar encontrado: {n}")
        break
else:
    print("Todos os números são pares!")
