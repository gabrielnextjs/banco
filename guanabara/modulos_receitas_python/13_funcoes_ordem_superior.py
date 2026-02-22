# =========================================================
# LAMBDA: A FUNÇÃO ANÔNIMA DE UMA LINHA
# =========================================================
def dobrar_normal(x):
    return x * 2


dobrar = lambda x: x * 2
print(dobrar(5))

somar = lambda a, b: a + b
potencia = lambda base, exp: base**exp
verificar_par = lambda n: n % 2 == 0

print(somar(3, 4))
print(potencia(2, 8))
print(verificar_par(10))

# =========================================================
# map() - TRANSFORMAR TODOS OS ITENS DE UMA LISTA
# =========================================================
precos = [100, 250, 1800, 499]
precos_com_desconto = list(map(lambda p: round(p * 0.90, 2), precos))
print(precos_com_desconto)

ids_texto = ["1", "2", "3", "4", "5"]
ids_int = list(map(int, ids_texto))
print(ids_int)

# =========================================================
# filter() - FILTRAR ITENS DE UMA LISTA POR CONDIÇÃO
# =========================================================
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)

funcionarios = [
    {"nome": "Ana", "salario": 4500},
    {"nome": "Bruno", "salario": 7000},
    {"nome": "Carla", "salario": 9000},
    {"nome": "Diego", "salario": 3200},
]
seniors = list(filter(lambda f: f["salario"] > 5000, funcionarios))
for s in seniors:
    print(f"{s['nome']}: R$ {s['salario']}")

# =========================================================
# sorted() COM key= (ORDENAÇÃO PERSONALIZADA)
# =========================================================
tecnologias = ["Python", "JS", "TypeScript", "Go", "Dart"]
por_tamanho = sorted(tecnologias, key=lambda t: len(t))
print(por_tamanho)

por_salario = sorted(funcionarios, key=lambda f: f["salario"])
por_salario_desc = sorted(funcionarios, key=lambda f: f["salario"], reverse=True)
for f in por_salario_desc:
    print(f"{f['nome']}: R$ {f['salario']}")
