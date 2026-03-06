import time
senha = ""
erros = 0
max_erros = 3
menu = 0
lista = []


def numero(mensagem, tipo= int):
    while True:
        try:
            return tipo(input(mensagem).replace(",","."))
        except ValueError:
            print("\nDigite apenas numeros")


while menu != 6:
    menu = numero('''
Selecione o produto que deseja comprar:
                     
[1] Memoria ram
[2] Procesador
[3] Cooler
[4] SSD
[5] Mostrar Carrinho
[6] Sair
Insira: ''')
    
    if menu == 6:
        print("Voce saiu!")
        break

    elif menu == 5:
        if not lista:
            print("Carrinho vazio!")
        else:
            print("")
            for item in lista:
                print(f"{item['produto']:<15} R$ {item['preco']:.2f}")

            sub_menu = 0

            while sub_menu != 2:
                sub_menu = numero('''
[1] Continuar comprando
[2] Pagar
[3] Limpar carrinho
Insira: '''
    )
                if sub_menu == 1:
                    break
                elif sub_menu == 2:
                    menu_pay = 0
                    metodo_pagamento = 0
                    total = 0
                    for item in lista: 
                        total += item["preco"]
                    print("")
                    print(f"Total: R$ {total:.2f}")
                    while menu_pay != 2:
                        menu_pay = numero('''
[1] Confirmar
[2] Cancelar
Insira: ''')
                        if menu_pay == 1:
                            print(f"Voce esta pagando R$ {total:.2f}")
                            while metodo_pagamento != 3:
                                metodo_pagamento = numero('''
Insira seu metodo de pagamento: 
[1] Cartao
[2] Pix
[3] Voltar
Insira: ''')
                                if metodo_pagamento == 1:
                                    senha = input("Insira sua senha: ")
                                    senha = len(senha)
                                    if senha == 4:
                                        print("Pagamento aprovado")
                                        lista.clear()
                                        break
                                    else:
                                        print("Sua senha deve ter 4 caracteres")
                                elif metodo_pagamento == 2:
                                    print("Pagamento aprovado")
                                    lista.clear()
                                    break
                                elif metodo_pagamento == 3:
                                    print("Voce saiu!")
                                    break
                                else:
                                    print("Esta opcao nao existe")
                            break

                    
                elif sub_menu == 3:
                    lista.clear()
                    print("Carrinho Limpo")
                    break

    elif menu == 4:
        lista.append({"produto": "SSD" , "preco": 300})
        print(f"SSD adicionado ao carrinho!")

    elif menu == 3:
        lista.append({"produto": "Cooler" , "preco": 300})
        print(f"Cooler adicionado ao carrinho!")

    elif menu == 2:
        lista.append({"produto": "Processador" , "preco":  500})
        print(f"Processador adicionado ao carrinho!")

    elif menu == 1:
        lista.append({"produto": "Memoria Ram" , "preco": 345})
        print(f"Memoria Ram adicionado ao carrinho!")
    
    else:
        print("Esta opcao nao exite")


