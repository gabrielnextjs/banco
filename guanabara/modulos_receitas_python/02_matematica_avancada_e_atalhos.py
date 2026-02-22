import math

# =========================================================
# OPERADORES ARITMÉTICOS FUNDAMENTAIS
# =========================================================
soma = 10 + 5
divisao = 10 / 2  # Sempre retorna float: 5.0
div_inteira = 10 // 3  # Corta decimais, retorna inteiro: 3
resto = 10 % 3  # Resto da divisão: 1
potencia = 2 ** 10  # 2 elevado a 10: 1024

# =========================================================
# FUNÇÕES MATEMÁTICAS NATIVAS (SEM IMPORT)
# =========================================================
maior = max(10, 50, 5)
menor = min(10, 50, 5)
absoluto = abs(-273.15)
arred = round(15.7891, 2)
quociente, resto2 = divmod(17, 5)
print(f"17 dividido por 5: {quociente} com resto {resto2}")

# =========================================================
# MÓDULO MATH (MATEMÁTICA CIENTÍFICA)
# =========================================================
raiz = math.sqrt(144)
pi = math.pi
euler = math.e
piso = math.floor(9.9)
teto = math.ceil(9.1)
log10 = math.log10(1000)
seno = math.sin(math.radians(90))

cateto_a = 3
cateto_b = 4
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
print(f"Hipotenusa: {hipotenusa}")

# =========================================================
# OPERADORES DE ATRIBUIÇÃO
# =========================================================
pontos = 100
pontos += 50
pontos -= 20
pontos *= 2
pontos //= 3
pontos **= 2

# =========================================================
# OPERADORES DE COMPARAÇÃO
# =========================================================
# a == b, a != b, a > b, a >= b, a < b, a <= b
