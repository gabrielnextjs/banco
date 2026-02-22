import os
import random
import sys
import time

print("Analisando o lote de garrafas...")
time.sleep(1.5)

inicio = time.time()
for _ in range(1_000_000):
    pass
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

n_inteiro = random.randint(1, 100)
n_decimal = random.uniform(0.0, 1.0)
item = random.choice(["GPU", "CPU", "RAM"])
amostra = random.sample(range(1, 61), 6)

cartas = ["Ás", "Rei", "Dama", "Valete", "10", "9"]
random.shuffle(cartas)
print(f"Cartas embaralhadas: {cartas}")

if random.random() < 0.30:
    print("Você recebeu um item RARO!")

os.system("cls" if os.name == "nt" else "clear")

pasta_atual = os.getcwd()
os.makedirs("logs/2026", exist_ok=True)
arquivos = os.listdir(".")
separador = os.sep

caminho = os.path.join("logs", "2026", "vendas.txt")
print(caminho)

print(f"Versão do Python: {sys.version}")
print(f"Sistema Operacional: {sys.platform}")

if sys.platform == "win32":
    print("Rodando no Windows.")
