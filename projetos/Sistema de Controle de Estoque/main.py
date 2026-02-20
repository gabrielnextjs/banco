import time
opcao = 0
def adicionar():
    nova_peca = {}
    nova_peca["nome"] = input("Qual o nome da peca a ser adicionada: ")
    nova_peca["preco"] = float(input("Qual o preco do produto? "))
    nova_peca["quantidade"] = int(input("Qual a quantidade dese produto? "))
    return nova_peca

def vender():
    nome = input("Qual o nome da peca que voce vai vender: ")
    achou_produto = False

    for peca in pecas_pc:
        if nome == peca["nome"]:
            achou_produto = True
            unidades = int(input(f"Digite a quantidade do produto {nome} voce quer vender? "))
            if unidades > peca["quantidade"]:
                print("A quantidade de unidades que voce deseja vender e maior que o estoque do produto")
            else:
                peca["quantidade"] = peca["quantidade"] - unidades
                print(f"A quantidade de {unidades} foi vendida do produto {nome} e restam {peca['quantidade']}")
    if achou_produto == False:
        print("Este produto não existe no estoque!")

    return nome







pecas_pc = []


while opcao != 4:
    try:
        print("-----------CORVETE HARDWARE-----------")
        time.sleep(2)

        opcao = int(input('''
[1] Cadastrar uma peça nova
[2] Ver todas as peças disponíveis.
[3] Vender
[4] Sair e salvar
DIGITE UMA OPCAO A SEGUIR: '''))
    
        if opcao == 1:
            peca_pronta = adicionar()
            pecas_pc.append(peca_pronta)
            print(pecas_pc)
        elif opcao == 2:
            print(f"AQUI ESTA A LISTA DE PRODUTOS: {pecas_pc}")
        elif opcao == 3:
            vender_peca = vender()

        

    except ValueError:
        print("LEIA COM ATENCAO: DIGITE APENAS NUMEROS")