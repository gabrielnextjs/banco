import random

def soma(n1,n2):
    resultado = n1 + n2
    return resultado


def alet():
    numero_alet = random.randint(1,6)
    return numero_alet

def evaluate_number():
    number_al = alet()
    if number_al % 2 == 0 :
        print(f"Seu numero e {number_al} e voce ganhou")
        return False

    else:
        print(f"Seu numero e {number_al} e voce perdeu")
        return True
