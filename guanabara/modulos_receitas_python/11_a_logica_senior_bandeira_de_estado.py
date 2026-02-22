banco_cpfs = ["111.111.111-11", "222.222.222-22", "333.333.333-33"]
cpf_procurado = "222.222.222-22"  # substitui input("Digite o CPF do suspeito: ")

cpf_encontrado = False

for cpf in banco_cpfs:
    if cpf == cpf_procurado:
        cpf_encontrado = True
        print(f"ALERTA: O CPF {cpf} possui mandado de busca aberto.")
        break

if cpf_encontrado is False:
    print("Busca encerrada: CPF não consta nos registros oficiais.")

for cpf in banco_cpfs:
    if cpf == cpf_procurado:
        print(f"ALERTA: {cpf} encontrado no sistema.")
        break
else:
    print("CPF não encontrado em nenhum registro.")
