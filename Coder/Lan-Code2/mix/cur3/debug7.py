import math
import os

x = 16
raiz_quadrada = math.sqrt(x)
print(f"A raiz quadrada de {x} e {raiz_quadrada}")

angulo = 45
seno = math.sin(angulo)
print(f"O seno de {angulo} e {seno}")

diretorio = os.getcwd()
print(f"O diretorio atual e {diretorio}")

lista = [10, 20, 30]
tem = len(lista)
print(f"A lista {lista}, tem tamanho {tem}")

tem_p = sum(lista)
print(f"A lista {lista}, tem um somatorio de {tem_p}")