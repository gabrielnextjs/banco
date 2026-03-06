quadrados_antigo = []
for n in range(1, 11):
    quadrados_antigo.append(n**2)

quadrados = [n**2 for n in range(1, 11)]
pares = [n for n in range(1, 21) if n % 2 == 0]

nomes = ["  ana  ", "  PEDRO  ", " lucia "]
limpos = [nome.strip().title() for nome in nomes]

funcionarios = [
    {"nome": "Ana", "salario": 4500, "ativo": True},
    {"nome": "Bruno", "salario": 7000, "ativo": False},
    {"nome": "Carla", "salario": 9000, "ativo": True},
]
ativos = [f["nome"] for f in funcionarios if f["ativo"]]

precos_brl = [100.0, 250.0, 1800.0, 499.90]
precos_usd = [round(p / 5.10, 2) for p in precos_brl]
print(precos_usd)

quadrados_dict = {n: n**2 for n in range(1, 6)}
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}

letras = ["a", "b", "a", "c", "b", "a"]
frequencia = {letra: letras.count(letra) for letra in set(letras)}

indice_func = {f["nome"]: f["salario"] for f in funcionarios}
print(indice_func["Carla"])

vogais_em_frase = {letra for letra in "programação" if letra in "aeiouáéíóúãõ"}
print(vogais_em_frase)
