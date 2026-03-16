from utils import *

class dados:
    def __init__(self, nome, idade, cidade, salario):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.salario = salario

    def print_dados(self):
        print(f"Ola {self.nome}, voce tem {self.idade}, ganha: R$:{self.salario: .2f} e mora em {self.cidade}")

nome = input("Insira seu nome: ")
idade = preven("Insira sua idade: ")
cidade = input("Insira sua cidade: ")
salario = preven("Insira seu salario: ")

dados_user = dados(nome,idade,cidade,salario)
dados_user.print_dados()

