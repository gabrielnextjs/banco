from utils import *

class Calculadora:
    def __init__(self, num1, num2):
        self.numero_1 = num1
        self.numero_2 = num2

    
    def somar(self):
        resultado = self.numero_1 + self.numero_2
        return resultado
    
    def subtrair(self):
        resultado = self.numero_1 - self.numero_2
        return resultado
    
    def multiplicar(self):
        resultado = self.numero_1 * self.numero_2
        return resultado
    
    def dividir(self):
        if self.numero_2 != 0:
            resultado = self.numero_1 / self.numero_2
            return resultado
        else:
            return "Voce nao pode dividir por zero"


    
    def resto(self):
        resultado = self.numero_1 % self.numero_2
        return resultado
    
    def media(self, n_3):
        resultado = (self.numero_1 + self.numero_2 + n_3) / 3
        return resultado
    

premen("Ola seja bem vindo")
number1 = preven("Insira o primeiro numero: ")
number2 = preven("Insira o segundo numero: ")
number3 = 0

calcular = Calculadora(number1, number2)

while True:
    oque_deseja = preven('''
O que voce deseja:
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Resto
[6] Media entre 3 numeros
[7] Sair
Insira: ''')

    if oque_deseja == 1:
        resultado = calcular.somar()
        print(f"O resultado da soma e {resultado}")

    elif oque_deseja == 2:
        resultado = calcular.subtrair()
        print(f"O resultado da subtracao e {resultado}")

    elif oque_deseja == 3:
        resultado = calcular.multiplicar()
        print(f"O resultado da multiplicacao e {resultado}")

    elif oque_deseja == 4:
        resultado = calcular.dividir()
        print(f"O resultado da divisao e {resultado}")

    elif oque_deseja == 5:
        resultado = calcular.resto()
        print(f"O resultado da resto e {resultado}")

    elif oque_deseja == 6:
        number3 = preven("Insira o terceiro numero: ")
        resultado = calcular.media(number3)
        print(f"O resultado da media e {resultado}")

    elif oque_deseja == 7:
        break
    else:
        print("Esta opcao nao existe")




    

