import random
esteira = []
garrafas_aprovadas = []
estoque_caixa = []
caixa_aberta = []

for i in range(60):
    peso_sorteado = random.choice([500, 500, 500, 500, 456, 786, 510, 510, 508, 501])
    garrafa = {}
    garrafa["codigo"] = i
    garrafa["lote"] = "Lote-A"
    garrafa["peso"] = peso_sorteado
    esteira.append(garrafa)
print(f"A garrafas do {garrafa['lote']} passaram pela esteira")

arquivo_ap = open("garrafas_aprovadas.txt", "w")
arquivo = open("garrafas_regeitadas.txt", "w")
for garrafa in esteira:
    if garrafa["peso"] >= 490 and garrafa["peso"] <= 510:
        garrafas_aprovadas.append(garrafa)
        arquivo_ap.write(f"Garrafa Aprovada! Código: {garrafa['codigo']} | Lote: {garrafa['lote']} | Peso: {garrafa['peso']}\n")
        for i in range(0, len(garrafas_aprovadas)):
            if i == 20:
                print("Um lote minimo foi fechado")
    else:
        arquivo.write(f"Garrafa rejeitada! Código: {garrafa['codigo']} | Lote: {garrafa['lote']} | Peso: {garrafa['peso']}\n")


arquivo_caixa = open("caixas.txt", "w")
for garrafa in garrafas_aprovadas:
    caixa_aberta.append(garrafa)
    if len (caixa_aberta) == 6:
        codigo_bruto = f"{caixa_aberta[0]['lote']}{caixa_aberta[0]['codigo']}XYZ"
        codigo_hash = codigo_bruto[6:10]
        caixa_pronta = {"Codigo caixa:": codigo_hash, "Conteudo": caixa_aberta}
        estoque_caixa.append(caixa_pronta)
        arquivo_caixa.write(f"Caixa fechada: Hash {codigo_hash} | Garrafas: {len(caixa_aberta)}\n")
        caixa_aberta = []
    
arquivo.close()
arquivo_caixa.close()
arquivo_ap.close()