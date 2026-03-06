import json
import random

arquivo = open("Aprendizado/Curso Stack - Lury/copy_termoo/words.json", encoding="utf8")

words = json.load(arquivo)
escolha_aleatoria = random.choice(list(words.keys()))

boas_vindas = "Ola, seja bem vindo"
boas_vindas_len = len(boas_vindas)
boas_vindas_len = boas_vindas_len * 2
print(boas_vindas)
print("#" * boas_vindas_len)


user_choice = 5
win = False

while user_choice > 0 and win is not True:
    print("Dica: " + words[escolha_aleatoria])
    answer_user  = (input("Data: DDMMAAAA\n"))

    if len(answer_user) != 8:
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue
    if answer_user.isdigit():
        check = []
        pontuacao = 0
        for i in range(8):
            if answer_user[i] == escolha_aleatoria[i]:
                check.append("CR")
                pontuacao = pontuacao + 1
            else:
                check.append("ER")
        print("Resposta: ")
        print("|".join(check))
        print(" |".join(answer_user))
        user_choice = user_choice - 1

        if pontuacao == 8:
            win = True
    else:
        print("Erro na entrada. A resposta deve ser uma data.")


if win == True:
    print("VITORIA!!!!!!")
else:
    print("DERROTA!")
    print(f"Resposta era: {escolha_aleatoria}")
