import random
tentativa = 0

print("Seja bem vindo ao escolha certa")

def gerar_jogo(numero):
    random_number = random.randint(0, numero)
    return random_number

def vereficar(sera):
    if sera == jogo:
        print(f"Voce acertou, o numero e {jogo}")
        return sera



while True:
    try:
        numero_escolhido = int(input("Digite um numero teto do desafio: "))
        jogo = gerar_jogo(numero_escolhido)
        break
    except ValueError:
        print("Digite apenas numeros")
    
while True:
    while True:
        try:
            sera = int(input("Digite um numero e veja sua sorte: "))
            break
        except ValueError:
            print("Digite apenas numeros")

    numero_escolha = vereficar(sera)
    tentativa = tentativa + 1
    if sera != jogo:
        if tentativa == 3:
            print("O maximo de tentativas por rodada e 3")
            break

    elif sera == jogo:
        break


    
