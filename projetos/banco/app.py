import tkinter as tk
from functions import *
contas = carregar_contas()

janela = tk.Tk()
janela.title("SGP Bank")
janela.geometry("400x300")
janela.configure(bg="Black")

frame_inicio = tk.Frame(janela, bg="black")
frame_inicio.pack()

titulo = tk.Label(frame_inicio ,  text="SGP Bank" , fg="white" , bg="black", font=("Arial", 32 ,"bold"))
titulo.pack(pady=80)

def ao_criar():
    pass  

def ao_login():
    frame_inicio.pack_forget()
    frame_login.pack()

botao_criar = tk.Button(
    frame_inicio,
    text="Criar conta",
    fg="black",
    bg="white",
    font=("Arial", 14),
    command=ao_criar
)
botao_criar.pack(pady=5)

botao_login = tk.Button(
    frame_inicio,
    text="Login",
    fg="black",
    bg="white",
    font=("Arial", 14),
    command=ao_login
)
botao_login.pack(pady=5)

frame_login = tk.Frame(janela, bg="black")

tk.Label(frame_login ,  text="Login" , fg="white" , bg="black", font=("Arial", 24 ,"bold"))
titulo.pack(pady=30)

tk.Label(frame_login ,  text="Numero da conta" , fg="white" , bg="black").pack()
entrada_numero = tk.Entry(frame_login)
entrada_numero.pack(pady=5)

tk.Label(frame_login ,  text="Senha" , fg="white" , bg="black").pack()
entrada_numero = tk.Entry(frame_login, show="*")
entrada_numero.pack(pady=5)

tk.Label(frame_login ,  text="Entrar" , fg="black" , bg="white", font=("Arial", 12)).pack(pady=15)

janela.mainloop()