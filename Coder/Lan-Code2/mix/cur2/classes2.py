from utils import *

class Clientes:
    def __init__(self, nome , email, senha,  plano):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.plano = plano
        self.planos = ["Ultra", "Basic"]
        if self.plano in self.planos:
            self.plano = plano
        else:
            self.plano = None

    def mudar_plano(self, novo_plano):
        if novo_plano == self.plano:
            print("Voce ja esta neste plano")
        else:
            if novo_plano in self.planos:
                self.plano = novo_plano
                print("Plano alterado")
            else:
                print("Plano inexistente")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme or self.plano == "Ultra":
            print(f"Ver filme {filme}")
        else:
            print("Voce nao pode ver este conteudo, faca o upgrade para ver")
            while True:
                plano_upgrade = preven('''
Mudar de plano:
[1] Sim
[2] Nao
Insira: ''')
                if plano_upgrade == 1:
                    update_customer_plan(self)
                    break
                elif plano_upgrade == 2:
                    break
                else:
                    print("Insira somente opcoes validas")

nome = input("Insira seu nome: ")
email = input("Insira seu email: ")
senha = input("Insira sua senha: ")

while True:
    plano = preven('''
Qual plano:
[1] Basic
[2] Ultra
[3] Sair
Insira:  ''')
    if plano == 1:
        sele = "Basic"
        break
    elif plano == 2:
        sele = "Ultra"
        break
    elif plano == 3:
        sele = None
        break
    else:
        print("Esta opcao nao existe")

def update_customer_plan(cliente):

    while True:
        novo_plano_sele = preven('''
Qual plano:
[1] Basic
[2] Ultra
[3] Sair
Insira:  ''')
        if novo_plano_sele == 1:
            novo_plano = "Basic"
            cliente.mudar_plano(novo_plano)
            break
        elif novo_plano_sele == 2:
            novo_plano = "Ultra"
            cliente.mudar_plano(novo_plano)
            break
        elif novo_plano_sele == 3:
            break
        else:
            print("Esta opcao nao existe")



cliente = Clientes(nome , email, senha, sele)

while True:
    conteudo = preven('''
Catalago:
[1] Frozen
[2] Divertidamente
[3] Perdidos no espaco
[4] Percy jackson
[5] Sair 
Insira: ''')
    if conteudo == 1:
        cliente.ver_filme("Frozen", plano_filme= "Basic")
    elif conteudo == 2:
        cliente.ver_filme("Divertidamente", plano_filme= "Basic")
    elif conteudo == 3:
        cliente.ver_filme("Perdidos no espaco", plano_filme= "Ultra")
    elif conteudo == 4:
        cliente.ver_filme("Percy jackson", plano_filme= "Ultra")
    elif conteudo == 5:
        break
    else:
        print("Insira apenas opcoes validas")


print(cliente.nome, cliente.email, cliente.senha, cliente.plano)

    
