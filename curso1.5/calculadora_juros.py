import time

nome = input("Qual e seu nome? ")
time.sleep(1)
nome = nome.title()

print(f"Ola {nome}, Seja bem-vindo a calculadora de juros composto")
time.sleep(1)
print("Aguarde ...")

dinheiro_inicial = int(input(f"{nome} Digite apenas em numeros o valor do seu primeiro aporte: "))

confir = 1

if dinheiro_inicial <=500:
    print(f"Este valor e o minimo para o primeiro aporte, seus resultados podem ser baixos")
    confir = int(input(f"{nome} para continuar digite (1) se quiser sair (2)"))

if  confir == 1:

    time.sleep(1)
    tempo = int(input(f"{nome} Digite em numeros por quantos meses voce deixaria seu dinheiro investido: "))
    time.sleep(1)
    taxa = float(input(f"{nome} Digite em decimal a taxa mensal do seu investimento: "))
    aporte = int(input("Em numeros ensira seu aporte mensal? "))
    time.sleep(1)
    salario_desejado = int(input(f"{nome} qual seria seu salario desejado"))

    tempo_decorrido = 0

    while tempo_decorrido < tempo:
        if tempo_decorrido == 0:

            montante = dinheiro_inicial * (1 + taxa) ** 1
            montante = round(montante, 2)
            tempo_decorrido = tempo_decorrido + 1
        else:

            montante = (montante + aporte) * (1 + taxa) ** 1
            montante = round(montante, 2)
            tempo_decorrido = tempo_decorrido + 1
             


    salario_mensal = (montante * taxa)
    salario_mensal = round(salario_mensal, 2)

    time.sleep(1)

    print("Aguarde ...")
    print("------------------------------------------------")

    print(f"Parabens {nome}, ao final do ivestimento voce tera o valor de R${montante}")

    if salario_mensal >= salario_desejado:
        print(f"Parabens {nome} , eu alario mensal com essse montante e de R$ {salario_mensal}")

    elif salario_mensal < salario_desejado:
        print(f"{nome} Infelizmente com esse valor voce nao ira conseguir aposentar, salario mensal e de {salario_mensal}")

elif confir == 2:
    print(f"Obrigado {nome} volte sempre")





