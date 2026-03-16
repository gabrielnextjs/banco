from utils import *

nome  = input("Insira seu nome: ")
nota =  preven("Informe sua nota: ", float)

if nota >= 7:
    print(f"{nome}, voce foi aprovado(A)")
elif nota >= 4 :
    print(f"{nome}, Pode fazer a recuperacao")
else:
    print(f"{nome}, voce foi reprovado(A)") 