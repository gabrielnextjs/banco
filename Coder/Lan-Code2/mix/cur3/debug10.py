from utils import *

def beber_agua():
    print("Bebendo agua")

def beber_cerveja():
    print("Bebendo cerveja")

lista = {
    1: beber_agua, 
    2: beber_cerveja
}


while True:
    selecao = preven('''
Escolha: 
[1] Beber agua
[2] Beber cerveja
[3] Sair
Insira: ''')
    
    if selecao == 3:
        print("Saindo")
        break

    elif selecao in lista:
        lista[selecao]()
    
    else:
        print("Esta opcao e invalida")