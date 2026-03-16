from utils import *

def passar(idade):
    return idade <= 17

premen("Seja bem vindo!")

nome = input("Informe seu nome: ")
idade = preven("Insira sua idade: ")
tentativa = 0
senha = 14102009
tentativa_senha = 0

while tentativa != 3 and tentativa_senha != senha:
    tentativa_senha = preven("Insira a senha: ")
    tentativa += 1

    if tentativa_senha == senha:
        if passar(idade):
            print(f"Voce nao pode entrar por ter {idade} anos")
        else:
            print("Pode entrar")
    else:
        if tentativa != 3:
            print("Senha incorreta")
    
    if tentativa == 3:
        print("Sistema bloqueado, foi atinjido o limite de 3 tentativas")



