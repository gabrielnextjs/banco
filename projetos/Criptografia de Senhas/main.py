def codificar(senha, chave):
    resultado = ""
    for letra in senha:
        numero_secreto = ord(letra) + chave
        nova_letra = chr(numero_secreto)
        resultado = resultado + nova_letra
    return resultado

def descodificar(senha_ca, chave):
    resultado_de = ""
    for letra in senha_ca:
        numero_secreto_de = ord(letra) - chave
        nova_letra_de = chr(numero_secreto_de)
        resultado_de = resultado_de + nova_letra_de
    return resultado_de

opcao = 0

while opcao != 3:
    try:

        opcao = int(input('''
[1] CODIFICAR UMA SENHA
[2] DESCODIFICAR UMA SENHA
[3] SAIR DO SISTEMA
DIGITE O NUMERO QUE CORRRESPONDE A SUA ESCOLHA: '''))
        
        if opcao == 1:
            texto = input("Digite a senha que sera criptrografada: ")
            chave = int(input("Agora digite uma chave secreta composta apena por numeros: "))
            senha_pronta = codificar(texto, chave)
            print(f'''Aqui esta sua nova senha lacrada:
                        {senha_pronta}''')
            with open("cursogemini/senhas_salvas.txt", "a") as arquivo:
                arquivo.write(f"Senha codificada: {senha_pronta} , Usando a chave: {chave} \n")

        elif opcao == 2:
            texto_de = input("Digite a senha que sera descriptrografada: ")
            chave = int(input("Agora digite uma chave secreta composta apena por numeros: "))
            senha_pronta_de = descodificar(texto_de, chave)
            print(f'''Aqui esta sua nova senha liberada:
                        {senha_pronta_de}''')
            
        elif opcao == 3:
            print("Saindo do sistema")
            break

    except ValueError:
        print("LEIA COM ATENCAO: DIGITE APENAS NUMEROS")