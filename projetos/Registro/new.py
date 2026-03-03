from tkinter import *

root = Tk()

class application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        self.widgets__frame1()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='#1E90FF')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width=650 , height=500)
    def frames_de_tela(self):
        self.frame_1 = Frame(self.root , bd= 4, bg="#dfe3ee" , highlightbackground='#759fe6' , highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root , bd= 4, bg="#dfe3ee" , highlightbackground='#759fe6' , highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    def widgets__frame1(self):
        self.bt_limpar = Button(self.frame_1, text="Limpar", border=2, background="#c3c96a", 
                                foreground="white" , font= ("Verdana", 9 ,'bold'))
        self.bt_limpar.place(relx= 0.2, rely= 0.1 , relwidth=0.1 , relheight= 0.15)

        self.bt_limpar = Button(self.frame_1, text="Buscar", border=2, background="#b96ac9", 
                                foreground="white" , font= ("Verdana", 9 ,'bold'))
        self.bt_limpar.place(relx= 0.3, rely= 0.1 , relwidth=0.1 , relheight= 0.15)

        self.bt_limpar = Button(self.frame_1, text="Novo", border=2, background="#6a90c9", 
                                foreground="white" , font= ("Verdana", 9 ,'bold'))
        self.bt_limpar.place(relx= 0.6, rely= 0.1 , relwidth=0.1 , relheight= 0.15)

        self.bt_limpar = Button(self.frame_1, text="Alterar", border=2, background="#88c96a", 
                                foreground="white" , font= ("Verdana", 9 ,'bold'))
        self.bt_limpar.place(relx= 0.7, rely= 0.1 , relwidth=0.1 , relheight= 0.15)

        self.bt_limpar = Button(self.frame_1, text="Apagar", border=2, background="#c96a6a", 
                                foreground="white" , font= ("Verdana", 9 ,'bold'))
        self.bt_limpar.place(relx= 0.8, rely= 0.1 , relwidth=0.1 , relheight= 0.15)

        #Label e entrada do codigo

        self.lb_codigo = Label(self.frame_1, text="Codigo", bg="#dfe3ee", foreground="#6a90c9")
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.lb_codigo_entry = Entry(self.frame_1, bg="#dfe3ee", foreground="#000000")
        self.lb_codigo_entry.place(relx= 0.05, rely= 0.15, relwidth=0.08)

        #Label e entrada do nome

        self.nome = Label(self.frame_1, text="Nome", bg="#dfe3ee", foreground="#6a90c9")
        self.nome.place(relx= 0.05, rely= 0.35)

        self.lb_nome_entry = Entry(self.frame_1, bg="#dfe3ee", foreground="#000000")
        self.lb_nome_entry.place(relx= 0.05, rely= 0.45, relwidth=0.85)

        #Label e entrada do telefone

        self.telefone = Label(self.frame_1, text="Telefone", bg="#dfe3ee", foreground="#6a90c9")
        self.telefone.place(relx= 0.05, rely= 0.6)

        self.lb_telefone_entry = Entry(self.frame_1, bg="#dfe3ee", foreground="#000000")
        self.lb_telefone_entry.place(relx= 0.05, rely= 0.7, relwidth=0.4)

        #Label e entrada da cidade

        self.cidade = Label(self.frame_1, text="Cidade", bg="#dfe3ee", foreground="#6a90c9")
        self.cidade.place(relx= 0.5, rely= 0.6)

        self.lb_cidade_entry = Entry(self.frame_1, bg="#dfe3ee", foreground="#000000")
        self.lb_cidade_entry.place(relx= 0.5, rely= 0.7, relwidth=0.4)



application()