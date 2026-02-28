import math


def e_palindromo(palavra):
    j = len(palavra)-1
    resultado = 0
    for i in range(len(palavra)):
        if palavra[i] ==  palavra[j]:
            resultado = resultado + 1
        if i >= j:
            break
        j = j - 1

    if resultado == math.ceil(len(palavra)/2):
        return True
    else:
        return False
    
def e_palindromo_recursive(palavra):
    if len(palavra) <= 1:
        return True
    else:
        return palavra[0] == palavra[-1] and e_palindromo_recursive(palavra[1:-1])
    
palavras = ["arara", "racecar", "carro", "cama", "level"]

for palavra in palavras:
    print(palavra)
    print(e_palindromo(palavra))
    print("\n")
    


