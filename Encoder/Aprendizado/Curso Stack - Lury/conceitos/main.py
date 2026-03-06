from functions import *


print("##########################")
print("Qual a data de vencimento?")
print("##########################")

data_vencimento = input("")

if len(data_vencimento) == 10:
    print(vereficar_vencimento(data_vencimento))
else:
    print("Entrada invalida")
