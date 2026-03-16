import time
from utils import premen , preven

def numero(mensagem, tipo= int):
    while True:
        try:
            return tipo(input(mensagem).replace(",","."))
        except ValueError:
            print("\nDigite apenas numeros")

def mensagem(mensagem):
    tamanho = max(35, len(mensagem))
    print("-" * tamanho)
    print(f"{mensagem:^{tamanho}}")
    print("-" * tamanho)

def somar():
    numero1 = int(input("Insira o primeiro numero: "))
    numero2 = int(input("Insira o segundo numero: "))
    somar = numero1 + numero2
    print("")
    print(f"Resultado: {somar}")

def subtrair():
    numero1 = int(input("Insira o primeiro numero: "))
    numero2 = int(input("Insira o segundo numero: "))
    subtrair = numero1 - numero2
    print("")
    print(f"Resultado: {subtrair}")

def multiplicar():
    numero1 = int(input("Insira o primeiro numero: "))
    numero2 = int(input("Insira o segundo numero: "))
    multiplicar = numero1 * numero2
    print("")
    print(f"Resultado: {multiplicar}")

def dividir():
    numero1 = int(input("Insira o primeiro numero: "))
    numero2 = int(input("Insira o segundo numero: "))
    dividir = numero1 / numero2
    print("")
    print(f"Resultado: {dividir}")

def calculadora():
    mensagem("Calculadora")
    while True:
        menu = int(input('''
OQUE VOCE DESEJA:
[1] SOMAR
[2] SUBTRAIR
[3] MULTIPLICAR 
[4] DIVIDIR
[5] SAIR
INSIRA: '''))
        if menu == 1:
            somar()
        elif menu == 2:
            subtrair()
        elif menu == 3:
            multiplicar()
        elif menu == 4:
            dividir()
        elif menu == 5:
            break
        else: 
            mensagem("Insira uma opcao valida")
            time.sleep(1)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1 

def area():
    mensagem("Ola, seja bem vindo!")
    largura = numero("Insira a largura do terreno: ", float)
    comprimento = numero("Insira a comprimento do terreno: ", float)
    area = largura * comprimento
    print(f"A area do terrono e: {area}")

def contagem():
    mensagem("Ola, seja bem vindo(a)!")
    Inicio = numero("Inicio: ")
    Fim = numero("Fim: ")
    Passo = numero("Passo: ")

    pos = Inicio
    while pos <= Fim:
        print(pos)
        pos += Passo
        time.sleep(0.1)
    while pos >= Fim:
        print(pos)
        pos -= Passo
        time.sleep(0.1)

def maior():

    lista = []
    while True:
        numeros = preven("Insira os numeros (ou digite [0] para encerrar): ")
        if numeros == 0:
            break
        lista.append(numeros)
    if lista:
        premen(f"O maior numero e {max(lista)}")
    else:
        premen("Nenhum numero inserido.")



