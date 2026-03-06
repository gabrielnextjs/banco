import random
import time


pontos_usuario = 0
pontos_pc = 0

opcoes = [1, 2, 3]

while True:
    while True:
        try:
            escolha_usuario = int(input("Escolha: \n1(Pedra) \n2(Tesoura) \n3(Papel) \n4(Sair) \n Digite: "))
            break
        except ValueError:
            print("Digite apenas numeros")
            time.sleep(2)
    if escolha_usuario > 4:
        print("Escolha apenas os numeros apresentados")
    elif escolha_usuario < 1:
        print("Escolha apenas os numeros apresentados")
    else:
        if escolha_usuario == 4:
            print("Voce saiu do jogo")
            break

        escolha_pc = random.randint(0, 2)
        opcao_pc = opcoes[escolha_pc]
        det_escolha_pc = {1: "Pedra", 2: "Tesoura", 3: "Papel"}
        print(f"O computador escolheu {det_escolha_pc[opcao_pc]}")

        if escolha_usuario == opcao_pc:
            print("Empate")

        elif escolha_usuario == 1 and opcao_pc == 2:
            print("Voce ganhou")
            pontos_usuario = pontos_usuario + 1

        elif escolha_usuario == 2 and opcao_pc == 3:
            print("Voce ganhou")
            pontos_usuario = pontos_usuario + 1

        elif escolha_usuario == 3 and opcao_pc == 1:
            print("Voce ganhou")
            pontos_usuario = pontos_usuario + 1

        else:
            print("Voce perdeu")
            pontos_pc = pontos_pc + 1


print(f"Sua pontuacao {pontos_usuario}")
print(f"Pontuacao da IA {pontos_pc}")

if pontos_pc > pontos_usuario:
    print("Derrota")
elif pontos_usuario == pontos_pc:
    print("Empate")
else:
    print("Vitoria")