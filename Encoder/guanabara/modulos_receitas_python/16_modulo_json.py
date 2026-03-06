import json
import urllib.request

perfil_python = {
    "usuario": "SGP_Dev",
    "nivel": 99,
    "premium": True,
    "saldo": None,
    "tecnologias": ["Python", "TypeScript", "Dart"],
}

perfil_json_str = json.dumps(perfil_python)
print(type(perfil_json_str))
print(perfil_json_str)

perfil_formatado = json.dumps(perfil_python, indent=4, sort_keys=True, ensure_ascii=False)
print(perfil_formatado)

resposta_api = '{"status": "success", "data": {"id": 42, "ativo": true}}'
dados_python = json.loads(resposta_api)

print(type(dados_python))
print(dados_python["status"])
print(dados_python["data"]["id"])
print(dados_python["data"]["ativo"])

banco_usuarios = [
    {"id": 1, "nome": "Ana", "admin": True},
    {"id": 2, "nome": "Bruno", "admin": False},
    {"id": 3, "nome": "Carla", "admin": True},
]

with open("usuarios.json", "w", encoding="utf-8") as arquivo:
    json.dump(banco_usuarios, arquivo, indent=4, ensure_ascii=False)

with open("usuarios.json", "r", encoding="utf-8") as arquivo:
    usuarios_carregados = json.load(arquivo)

for usuario in usuarios_carregados:
    tipo = "Admin" if usuario["admin"] else "Usuário"
    print(f"[{tipo}] ID {usuario['id']}: {usuario['nome']}")

url = "https://viacep.com.br/ws/30140071/json/"
try:
    with urllib.request.urlopen(url) as resposta:
        dados_cep = json.loads(resposta.read().decode("utf-8"))
    print(f"CEP:    {dados_cep.get('cep')}")
    print(f"Rua:    {dados_cep.get('logradouro')}")
    print(f"Cidade: {dados_cep.get('localidade')}")
    print(f"Estado: {dados_cep.get('uf')}")
except Exception as e:
    print(f"Erro ao buscar CEP: {e}")
