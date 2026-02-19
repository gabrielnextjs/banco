import tkinter as tk

# 1. O "Cérebro" (O que acontece quando o usuário clica)
def acao_do_botao():
    texto_tela.config(text="Você clicou! O motor funcionou! 🚀")

# 2. A "Roupa" (A Janela Visual)
janela = tk.Tk()
janela.geometry("350x200") # Define o tamanho da janela
janela.title("Meu Primeiro App")

# 3. Colocando um texto na janela
texto_tela = tk.Label(janela, text="Bem-vindo ao sistema!")
texto_tela.pack(pady=20)

# 4. Colocando o botão na janela e conectando com o "Cérebro"
botao = tk.Button(janela, text="Clique Aqui", command=acao_do_botao)
botao.pack()

# 5. O loop que mantém a janela aberta na tela
janela.mainloop()