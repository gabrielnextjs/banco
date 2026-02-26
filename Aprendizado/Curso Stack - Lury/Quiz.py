print("Seja bem vindo ao quiz Geladeira")

comecar_user = input("Deseja inicar? (S/N)").strip().lower()

if comecar_user != "s":
    quit()

score = 0

print("Comecando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstart Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
pergunta_1 = input("Resposta: ").strip().lower()

if pergunta_1 == "a":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")
    

print("Qual o nome do protagonista do jogo GTA San Andreas \n (A) Carlos Josh \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n")

pergunta_2 = input("Resposta: ").strip().lower()

if pergunta_2 == "b":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")

print(f"Quiz acabou... Pontuacao: {score}")