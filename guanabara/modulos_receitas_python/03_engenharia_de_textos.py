noticia = "   Lançamento do novo servidor Bedrock!!!   "

# =========================================================
# 1. LIMPEZA, CONTAGEM E PADRONIZAÇÃO
# =========================================================
texto_limpo = noticia.strip()
texto_maiuscu = texto_limpo.upper()
texto_minuscu = texto_limpo.lower()
texto_titulo = texto_limpo.title()
tamanho = len(texto_limpo)

# =========================================================
# 2. BUSCA DENTRO DA STRING
# =========================================================
if "Bedrock" in texto_limpo:
    print("Esta notícia é sobre Minecraft!")

posicao = texto_limpo.find("servidor")
contagem = texto_limpo.count("o")
indice = texto_limpo.index("novo")

print(f"Palavra 'servidor' começa na posição: {posicao}")
print(f"A letra 'o' aparece {contagem} vezes")

# =========================================================
# 3. SUBSTITUIÇÃO E VERIFICAÇÃO
# =========================================================
novo_texto = texto_limpo.replace("Bedrock", "Java")
comeca_com = texto_limpo.startswith("Lançamento")
termina_com = texto_limpo.endswith("!!!")

# =========================================================
# 4. FATIAMENTO DE ALTA PRECISÃO (SLICING)
# =========================================================
hash_completo = "LOTE-A_9942_GABINETE"
prefixo = hash_completo[:6]
codigo_meio = hash_completo[7:11]
ultimas = hash_completo[-4:]
invertida = hash_completo[::-1]
a_cada_dois = hash_completo[::2]

# =========================================================
# 5. DIVIDIR E JUNTAR (SPLIT E JOIN)
# =========================================================
tags = "Next.js, React, Supabase, Python"
lista_tags = tags.split(", ")
separador = " | "
tags_reunidas = separador.join(lista_tags)

# =========================================================
# 6. F-STRINGS COM FORMATADORES AVANÇADOS (RELATÓRIOS)
# =========================================================
nome_produto = "SSD M.2 NVMe"
preco = 459.9
estoque = 7

print(f"{'Produto':<20} {'Preço':>10} {'Qtd':>5}")
print(f"{'---' * 12}")
print(f"{nome_produto:<20} R${preco:>8.2f} {estoque:>5d}")

salario_alto = 12500000.50
print(f"Salário: R$ {salario_alto:,.2f}")

id_pedido = 42
print(f"Pedido Nº {id_pedido:05d}")
