import time

def ler_numero(mensagem, tipo= float):
    while True:
        try:
            return tipo(input(mensagem).replace(",","."))
        except ValueError:
            print("Digite apenas numeros")

nome = input("Insira seu nome: ")
idade = ler_numero("Insira sua idade: ",int)

def validar_idade(idade):
    return idade >= 18

def purchase_product(ler_numero, idade, validar_idade):
    produto = 0
    while produto != 3:
        produto = ler_numero("Insira o numero do produto o qual deseja comprar: \n" 
    " [1] salame\n [2] cigarro\n [3] sair\n INSIRA: ", int)
        if produto == 1:
            print(f"Produto comprado")
            time.sleep(1.5)
        elif produto == 2:
            if validar_idade(idade):
                print(f"Produto comprado")
                time.sleep(1.5)
            else:
                print("Voce nao tem idade suficiente")
                time.sleep(1.5)
        elif produto == 3:
            print("Voce saiu...")
            time.sleep(1)
            break
        else:
            print("Esta opcao nao existe")
            time.sleep(1.5)

purchase_product(ler_numero, idade, validar_idade)

