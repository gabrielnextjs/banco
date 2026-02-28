import time


while True:
    try:
        timer = int(input("Em segundos digite o insira o tempo: "))
        break
    except ValueError:
        print("Insira apenas numeros.")


while timer != 0:
    minutos, segundos = divmod(timer , 60)
    display = "{:02d}:{:02d}".format(minutos, segundos)
    print(f"TIMER: ",display, end="\r")
    time.sleep(1)
    timer = timer - 1

print("O cronometro chegou ao fim")