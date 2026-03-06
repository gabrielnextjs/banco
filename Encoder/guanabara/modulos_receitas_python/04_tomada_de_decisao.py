nota_enem = 780
tem_cota = False
idade = 17

if nota_enem >= 750 or tem_cota is True:
    print("Você passou na primeira fase da UFMG!")
    if idade >= 18:
        print("Pode se matricular sozinho.")
    else:
        print("Traga um responsável para assinar os documentos.")
elif nota_enem >= 600:
    print("Você ficou na lista de espera. Fique atento ao SISU.")
else:
    print("Não foi dessa vez. Continue os estudos!")

status = "Aprovado" if nota_enem >= 600 else "Reprovado"
tipo_usuario = "Admin" if idade >= 18 else "Menor de Idade"
print(f"Status: {status} | Tipo: {tipo_usuario}")

servidor_online = True
print(f"Servidor: {'ONLINE' if servidor_online else 'OFFLINE'}")

comando_chat = "/kick"

match comando_chat:
    case "/kick":
        print("Expulsando o jogador da partida...")
    case "/ban":
        print("Banindo o jogador permanentemente!")
    case "/mute":
        print("Jogador silenciado por 10 minutos.")
    case "/help":
        print("Comandos: /kick /ban /mute /help")
    case _:
        print(f"Comando desconhecido: '{comando_chat}'")

pontos_jogador = 850
match pontos_jogador:
    case p if p >= 1000:
        print("Rank: Diamante")
    case p if p >= 500:
        print("Rank: Ouro")
    case _:
        print("Rank: Prata")
