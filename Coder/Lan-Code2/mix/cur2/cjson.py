import json



with open("Coder/Lan-Code2/mix/cur2/frutas.json", "r", encoding="utf8") as arq:
   dados = json.load(arq)
   print(dados)