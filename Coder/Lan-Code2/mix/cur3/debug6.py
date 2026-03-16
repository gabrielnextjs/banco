from utils import *

class Aluno:
    def __init__(self, nome, nota_t1, nota_t2, nota_t3):
        self.nome = nome
        self.nota_t1 = nota_t1
        self.nota_t2 = nota_t2
        self.nota_t3 = nota_t3

    def calcular_media(self):
        return (self.nota_t1 + self.nota_t2 + self.nota_t3) / 3

    
    def passou(self, precisa):
        media_aluno = self.calcular_media()
        return media_aluno >= precisa

premen("Seja bem vindo!")

nome = input("Qual seu nome: ")
nota_t1 = preven("Qual sua nota do primeiro trimestre: ")
nota_t2 = preven("Qual sua nota do segundo trimestre: ")
nota_t3 = preven("Qual sua nota do terceiro trimestre: ")
passar = preven("Insira quantos pontos voce precisa: ")

dados_alunos = Aluno(nome,nota_t1,nota_t2,nota_t3)
if dados_alunos.passou(passar):
    print("Voce passou!")
else:
    print("Voce nao passou")
        
        
        
        