from utils import *

class Carro:
    def __init__(self, modelo, ano, preco, idade):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.idade = idade
        self.ligado = False

    def test_drive(self):
        if self.idade >= 21:
            premen("Pode testar!")
        else:
            premen("Infelizmente voce nao tem a idade minima para testar!")

    def informacoes(self):
        premen(f"Modelo: {self.modelo} , Ano: {self.ano} , Preco: R${self.preco}")

    def ligar(self):
        if not self.ligado:
            premen("Ligando")
            self.ligado = True
        else:
            premen("O carro ja esta ligado")
    
    def desligar(self):
        if self.ligado:
            premen("Desligando")
            self.ligado = False
        else:
            premen("O carro nao esta ligado")

    
carro1 = Carro("Onix", 2023 , 7000 , 12)

while True:
    opcao = preven('''
Escolha sua opcao:
[1] Test drive
[2] Ligar carro
[3] Informacoes carro
[4] Desligar carro
[5] Sair
Insira: ''')

    if opcao == 1:
        carro1.test_drive()
    elif opcao == 2:
        carro1.ligar()
    elif opcao == 3:
        carro1.informacoes()
    elif opcao == 4:
        carro1.desligar()
    elif opcao == 5:
        break


