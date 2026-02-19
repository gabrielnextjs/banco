import time
senha = "1417"
tentativa = ""
erro = 0
metodo_pagamento = (input("Qual su metodo de pagamento? DIGITE (1) PARA CARTAO E (2) PARA PIX"))

if metodo_pagamento == "1" or metodo_pagamento == "2":
    print("Aguarde")
    time.sleep(3)
    if metodo_pagamento == "1":
        print(f"seu metodo de pagamento e CARTAO ....")
        time.sleep(1)
        while tentativa != senha:
            tentativa = (input("digite a senha correta do cartao"))
            if tentativa != senha:
                erro = erro + 1
                if erro == 3:
                    print("Cartao Bloqueado")
                    break
        if tentativa == senha:
            time.sleep(2)
            print("Pagamento aprovado")
    elif metodo_pagamento == "2":
        print(f"Seu metodo de pagamnto e PIX ...")
        time.sleep(1)
        print("Pagamnto aprovado")
else:
    print(f"Nao aceitamos o metodo {metodo_pagamento}")