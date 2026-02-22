# ---------------------------------------------------------
# LISTAS
# ---------------------------------------------------------
jogos = ["Cities Skylines", "Minecraft", "Assassin's Creed"]
jogos.append("GTA V")
jogos.insert(1, "Valorant")
jogos.remove("Minecraft")
removido = jogos.pop(0)
jogos.sort()
jogos.reverse()
total = len(jogos)
existe = "GTA V" in jogos
copia = jogos.copy()

# ---------------------------------------------------------
# TUPLAS
# ---------------------------------------------------------
coordenadas_servidor = (-23.55052, -46.63330)
versao_app = (2, 5, 1)
cores_rgb = (255, 165, 0)

latitude, longitude = coordenadas_servidor
major, minor, patch = versao_app
print(f"Versão: {major}.{minor}.{patch}")

# ---------------------------------------------------------
# SETS / CONJUNTOS
# ---------------------------------------------------------
ips_logados = {"192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.3"}
print(ips_logados)

ips_logados.add("203.0.113.42")
ips_logados.discard("10.0.0.5")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)

lista_com_repeticoes = [1, 2, 2, 3, 3, 3, 4]
lista_unica = list(set(lista_com_repeticoes))

# ---------------------------------------------------------
# DICIONÁRIOS
# ---------------------------------------------------------
perfil = {"usuario": "SGP Notícias", "seguidores": 1500, "verificada": False}

seguidores = perfil.get("seguidores", 0)
premium = perfil.get("premium", False)

print(list(perfil.keys()))
print(list(perfil.values()))
for chave, valor in perfil.items():
    print(f"  {chave}: {valor}")

perfil["site"] = "sgpnoticias.com.br"
del perfil["verificada"]

banco_dados = [
    {"id": 1, "cargo": "Perito em Tecnologia", "ativo": True},
    {"id": 2, "cargo": "Agente de Polícia", "ativo": False},
    {"id": 3, "cargo": "Desenvolvedor Sênior", "ativo": True},
]

for funcionario in banco_dados:
    if funcionario["ativo"]:
        print(f"ID {funcionario['id']}: {funcionario['cargo']}")
