# OS QUATRO MODOS DE ABERTURA:
# "w", "a", "r", "r+", "x"

cabecalho = "=== Histórico de Vendas - Loja SGP Tech ===\n"
with open("historico.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(cabecalho)

nova_venda = "Venda #102: Placa Mãe - R$ 800.00"
with open("historico.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nova_venda}\n")

novas_vendas = [
    "Venda #103: SSD M.2  - R$ 450.00\n",
    "Venda #104: Monitor  - R$ 1200.00\n",
    "Venda #105: Teclado  - R$ 350.00\n",
]
with open("historico.txt", "a", encoding="utf-8") as arquivo:
    arquivo.writelines(novas_vendas)

with open("historico.txt", "r", encoding="utf-8") as arquivo:
    conteudo_completo = arquivo.read()
    print(conteudo_completo)

with open("historico.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas, start=1):
        print(f"[{i:02d}] {linha.strip()}")

import os

caminho = "historico.txt"
if os.path.exists(caminho):
    tamanho = os.path.getsize(caminho)
    print(f"Arquivo existe! Tamanho: {tamanho} bytes")
else:
    print("Arquivo não encontrado. Criando novo...")
