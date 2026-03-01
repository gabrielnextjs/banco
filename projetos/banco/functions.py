import json
import hashlib
import tkinter as tk

def carregar_contas():
    with open("/home/gabriel/Documentos/Projeto/banco/projetos/banco/contas.json" , "r") as arquivo:
        contas = json.load(arquivo)
    return contas

def salvar_contas(contas):
    with open("/home/gabriel/Documentos/Projeto/banco/projetos/banco/contas.json" , "w") as arquivo:
        json.dump(contas, arquivo)

def cadastrar(contas):
    nome = input("Insira o nome de usuario da conta: ")
    while True:
        try:
            senha = hashear(int(input("Digite a senha da conta: ")))
            agencia = int(input("Digite a agencia da conta: "))
            break
        except ValueError:
            print("Digite apenas numeros")
    saldo = 0

    numero = str(len(contas) + 1).zfill(4)

    contas[numero] = {
        "nome": nome,
        "senha": senha,
        "agencia": agencia,
        "saldo": saldo,
    }
    salvar_contas(contas)

def login(contas):
    while True:
        try:
            numero = input("Digite o numero da conta: ").zfill(4)
            senha = int(input("Digite a senha da conta: "))
            break
        except ValueError:
            print("Digite apenas numeros")

    if numero in contas:
        if contas[numero]["senha"] == hashear(senha):
            print("Login Realizado")
            contas[numero]["numero"] = numero.zfill(4)
            return contas[numero]
        print("Senha incorreta")
    else:
        print("Conta nao encontrada")

    return None

def depositar(conta_logada, contas):
    while True:
        try:
            valor = int(input("Digite o  valor do deposito: "))
            break
        except ValueError:
            print("Digite apenas numeros")

    if valor == 0:
        print("O valor deve ser maior doque zero absoluto")
    else:
        deseja = 0
        while deseja != 2:
            deseja = int(input(f'''
Voce esta depositando para conta: {contas[conta_logada["numero"]]["nome"] } digite [1] para prosseguir e [2] para cancelar: '''))
            if deseja == 1:
                contas[conta_logada["numero"]]["saldo"] += valor
                salvar_contas(contas)
                print(f"deposito de valor R$ {valor:.2f} realizado")
                break
            elif deseja == 2:
                break

def trasferir(conta_logada, contas):
        while True:
            try:
                destino = input("Digite o numero da conta pra qual deseja trasferir: ").zfill(4)
                valor = int(input("Digite o  valor da transferencia: "))
                break
            except ValueError:
                print("Digite apenas numeros")

        if destino not in contas:
            print("Esta conta nao existe")
        elif valor == 0:
            print("O valor deve ser maior doque zero absoluto")
        elif destino == conta_logada["numero"]:
            print("Voce nao pode trasferir para voce mesmo")
        elif conta_logada["saldo"] < valor:
            print("Saldo insuficiente")
        else:
            deseja = 0
            while deseja != 2:
                deseja = int(input(f'''
Voce esta trasferindo para conta: {contas[destino]["nome"]} digite [1] para prosseguir e [2] para cancelar: '''))
                if deseja == 1:
                    contas[conta_logada["numero"]]['saldo'] -= valor
                    contas[destino]["saldo"] += valor
                    salvar_contas(contas)
                    print(f"Trasferencia de valor R$ {valor:.2f} realizada")
                    break
                elif deseja == 2:
                    break

def hashear(senha):
    return hashlib.sha256(str(senha).encode()).hexdigest()

def sacar(conta_logada, contas):
    while True:
        try:
            valor = int(input("Digite o  valor do saque: "))
            break
        except ValueError:
            print("Digite apenas numeros")

    if valor == 0:
        print("O valor deve ser maior doque zero absoluto")
    elif contas[conta_logada["numero"]]["saldo"] < valor:
        print("Saldo insufiente")
    else:
        deseja = 0
        while deseja != 2:
            deseja = int(input(f'''
Voce esta sacando para conta: {contas[conta_logada["numero"]]["nome"] } digite [1] para prosseguir e [2] para cancelar: '''))
            if deseja == 1:
                contas[conta_logada["numero"]]["saldo"] -= valor
                salvar_contas(contas)
                print(f"Saque de valor R$ {valor:.2f} realizado")
                break
            elif deseja == 2:
                break

def ao_clicar():
    print("Clicou")


