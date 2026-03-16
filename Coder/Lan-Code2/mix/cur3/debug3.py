from utils import *

class Dados_user:
    def __init__(self , nome, telefone, identidade):
        self.nome = nome
        self.telefone = telefone
        self.identidade = identidade

    def printar_dados(self):
        print(f'''
Nome: {self.nome}
Telefone: {self.telefone}
Identidade: {self.identidade}''')
        
nome = input("Insira seu nome: ")
telefone = preven("Insira seu telefone: ")
identidade = preven("Insira sua identidade: ")
        
p_dados = Dados_user(nome,telefone,identidade)
p_dados.printar_dados()