import time
opcao = 0
membros = []

while opcao != 3:
    print("-----------STREET SPORTS-----------")
    time.sleep(2)
    opcao = int(input('''
[1] Adicionar novo memebro
[2] Ver lista de membros
[3] Sair
DIGITE UMA OPCAO A SEGUIR: '''))
    if opcao == 3:
        print("Saindo do sistema")
        break
    elif opcao == 1:
        novo_membro = {}
        novo_membro["nome"] = input("Qual o nome do membro? ")
        novo_membro["nivel"] = int(input("Qual o nivel do membro? "))
        membros.append(novo_membro)
    elif opcao == 2:
        caracteres = len(membros)
        if caracteres == 0:
            print("Nao a membros cadastrados")
        else:
            for memebro in membros:
                print(memebro)



        
        
