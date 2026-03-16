from modulos import *
from utils import *

perdeu = evaluate_number()

if perdeu:
    while True:
        escolha = preven("Digite [1] para jogar de novo e [0] para sair: ")
        if escolha == 1:
            p = evaluate_number()
            if not p:
                break
        elif escolha == 0:
            print("Voce saiu!")
            break
        else:
            print("Esta opcao nao existe")






