import random
import string
import time

def gerador_senha(tamanho_senha = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    senha_pronta = ""
    for i in range(0, tamanho_senha):
        digit = random.choice(options)
        senha_pronta = senha_pronta + digit
    return senha_pronta


print("Seja bem vindo!")
time.sleep(1)

while True:
    try:
        dig_senha = int(input("Insira em numeros, o tamanho da senha a ser gerada: "))
        break
    except ValueError:
        print("Digite apenas numeros")
    time.sleep(2)

senha = gerador_senha(dig_senha)
time.sleep(1)
timer = 30
while timer != 0:
    minutos , segundos = divmod(timer, 60)
    display = "{:02d}:{:02d}".format(minutos, segundos)
    contagem = f"Sua senha: {senha} Senha sumira em: {display} "
    print(contagem,end="\r")
    time.sleep(1)
    timer = timer - 1

senha_tamanho = len(contagem)
print("-" * senha_tamanho)
print("Senha segura!")
senha = None




