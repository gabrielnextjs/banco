def gerar_ids_ruim(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista


def gerar_ids(n):
    for i in range(n):
        yield i


gen = gerar_ids(10_000_000)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for id_val in gerar_ids(5):
    print(f"Processando ID: {id_val}")


def ler_log_gigante(caminho_arquivo):
    """Lê um arquivo de qualquer tamanho sem explodir a RAM."""
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            yield linha.strip()


lista = [n**2 for n in range(1_000_000)]
gerador = (n**2 for n in range(1_000_000))

soma_quadrados = sum(n**2 for n in range(1001))
maior_par = max(n for n in range(100) if n % 2 == 0)
print(f"Soma dos quadrados: {soma_quadrados}")
print(f"Maior par até 99:   {maior_par}")


def pipeline_producao():
    print("-> Etapa 1: Recebendo matéria-prima...")
    yield "materia_prima"

    print("-> Etapa 2: Processando na linha de montagem...")
    yield "produto_semi_acabado"

    print("-> Etapa 3: Controle de qualidade...")
    yield "produto_aprovado"

    print("-> Etapa 4: Embalando para expedição...")
    yield "produto_embalado"


for etapa in pipeline_producao():
    print(f"   Status atual: {etapa}\n")
