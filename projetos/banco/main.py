import tkinter
from functions import *
contas  = carregar_contas()


print("BEM VINDO!")

menu = 0

while menu != 3:
    while True:
        try:
            menu = int(input('''
[1]Criar conta
[2]Login na conta
[3]Sair
INSIRA: '''))
            break
        except ValueError:
            print("Digite apenas numeros")


    if menu == 3:
        print("Voce saiu")
        break
    if menu == 1:
        cadastrar(contas)
    elif menu  == 2:
        conta_logada = login(contas)

        if conta_logada:
                menu_conta = 0
                while menu_conta != 5:
                    while True:
                        try:
                            menu_conta = int(input('''
[1]Ver saldo
[2]Transferir
[3]Depositar
[4]Sacar
[5]Sair
INSIRA: '''))
                            break
                        except ValueError:
                            print("Digite apenas numeros")

                    if menu_conta == 1:
                        print(f"Saldo: R$ {conta_logada['saldo']:.2f}")
                    elif menu_conta == 2:
                        trasferir(conta_logada, contas)
                    elif menu_conta == 3:
                        depositar(conta_logada, contas)
                    elif menu_conta == 4:
                        sacar(conta_logada, contas)
                    elif menu_conta == 5:
                        print("Voce saiu!")
                        break


print(tkinter.TkVersion)