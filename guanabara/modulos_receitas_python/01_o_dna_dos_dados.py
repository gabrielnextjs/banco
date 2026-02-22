# =========================================================
# TIPOS PRIMITIVOS DE DADOS
# =========================================================
curso = "Ciência da Computação"  # String (str)  -> Sempre entre aspas
idade = 16  # Integer (int) -> Números inteiros
nota = 755.40  # Float -> Decimais (PONTO, não vírgula!)
aprovado = True  # Boolean (bool)-> True ou False (inicial maiúscula)
vazio = None  # NoneType -> Ausência total de valor

# Descobrindo o tipo do dado
print(type(nota))  # <class 'float'>
print(type(vazio))  # <class 'NoneType'>

# None é diferente de 0 ou de ""! É o "nada oficial" do Python.
saldo_pendente = None
if saldo_pendente is None:
    print("Aguardando dados do banco...")

# =========================================================
# CONVERSÃO DE TIPOS (CASTING)
# =========================================================
preco_site = "2500.00"
preco_real = float(preco_site)  # "2500.00" -> 2500.0 (agora dá para calcular!)
idade_texto = str(idade)  # 16 -> "16" (agora dá para concatenar!)
nota_inteira = int(755.99)  # 755.99 -> 755 (CUIDADO: corta os decimais!)

# =========================================================
# ATRIBUIÇÃO MÚLTIPLA (PYTHÔNICO)
# =========================================================
# 3 variáveis recebem 3 valores na mesma linha, em ordem:
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# O underscore _ é convenção para "valor que não me interessa":
nome, _, sobrenome = "Ana", "Maria", "Silva"

# Troca de variáveis SEM variável temporária (exclusivo Python!):
a, b = 5, 10
a, b = b, a  # Agora a=10 e b=5

# =========================================================
# isinstance() VS type() (O VERIFICADOR PROFISSIONAL)
# =========================================================
# isinstance() é mais seguro pois aceita múltiplos tipos de uma vez:
preco = 29.99
if isinstance(preco, (int, float)):
    print("É numérico. Pode calcular desconto!")

# A Armadilha do input(): sempre retorna str.
entrada = "123"  # substitui input("Digite algo: ") para exemplo offline
if not isinstance(entrada, str):
    print("Isso nunca vai aparecer pois input() sempre retorna str!")

# Exemplos de conversão de entrada:
milhas = int("150")
saldo = float("1500.50")
print(f"Milhas: {milhas} | Saldo: {saldo}")
