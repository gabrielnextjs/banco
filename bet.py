import random
import time
saldo = 100

while saldo > 0:
    print(f"Seu saldo e de {saldo}" )
    aposta = int(input(f"Seu saldo e {saldo}. Qual o valor da sua aposta? (Se voce quiser sair digite (0)"))
    if aposta == 0:
        print(f"Voce sacou o valor de {saldo} e saiu do jogo ate a proxima.")
        break
    dado = random.randint(1, 6)
    if aposta > saldo or aposta <=0:
        print(f"Seu saldo atual e menor ou maior que de sua aposta por favor digite um valor menor ou igual que {saldo}")
    else:
    
        jogo = input("Escolha o jogo: [1] Par/Ímpar ou [2] Número Exato: ")

        if jogo == "1":

            if dado % 2 == 0:
                time.sleep(3)
                print(f"o dado rolou e caiu {dado} voce GANHOU!")
                saldo = saldo + aposta
            else:
                time.sleep(3)
                print(f"O dado rolou e caiu {dado} voce PERDEU!")
                saldo = saldo - aposta

        elif jogo == "2":

            palpite = int(input("Qual numero de 1 a 6 voce escolhe"))
            

            if palpite == dado:
                time.sleep(3)
                saldo = saldo + (aposta * 5)
                print(f"Parabens voce acertou com o numero {palpite} seu novo saldo e {saldo}")
            else:
                time.sleep(3)
                saldo = saldo - aposta
                print(f"Infelizmente voce perdeu e o valor de {aposta} foi debitado do seu saldo, seu novo saldo e {saldo}")



