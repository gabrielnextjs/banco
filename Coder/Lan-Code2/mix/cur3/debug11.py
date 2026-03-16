from utils import *

class Aluno:
    def __init__(self, nome, sala, turno, idade, ano_letivo):
        self.nome = nome
        self.sala = sala
        self.turno = turno
        self.idade = idade
        self.ano_letivo = ano_letivo

    def arquivar_dados(self):
        alunos = {
            "nome": self.nome,
            "sala": self.sala,
            "turno": self.turno,
            "situacao": self.situacao,
            "idade": self.idade,
            "ano_letivo": self.ano_letivo
        }
        return alunos
    
    def gerar_numero_matricula(self):
        return f"{self.nome[:3].upper()}{self.sala}{self.turno[0].upper()}"
    
    def salvar_dados(self):
        if not self.prevenir_duplicidade(self.nome):
            dados = self.arquivar_dados()
            with open("dados_aluno.txt", "a") as arquivo:
                arquivo.write(str(dados) + "\n")

    def declarar_situacao(self):
        if self.idade < 18:
            situacao = "Menor de idade"
        else:
            situacao = "Maior de idade"
        return situacao


    def exebir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Sala: {self.sala}")
        print(f"Turno: {self.turno}")
        print(f"Idade: {self.idade}")
        print(f"Ano Letivo: {self.ano_letivo}")
        print(f"Situação: {self.declarar_situacao()}")
    
    def prevenir_duplicidade(self, nome):
        with open("dados_aluno.txt", "r") as arquivo:
            for linha in arquivo:
                if nome in linha:
                    return True
        return False
    
    def biblioteca(self):
        print("Acessando a biblioteca...")
        if self.sala == "A" and self.turno == "Manhã":
            print("Você tem acesso à biblioteca das 8h às 12h.")
        elif self.sala == "B" and self.turno == "Tarde":
            print("Você tem acesso à biblioteca das 13h às 17h.")
        else:
            print("Você tem acesso à biblioteca das 8h às 17h.")



opcoes = {
    1: Aluno.exebir_dados,
    2: Aluno.salvar_dados,
    3: Aluno.biblioteca,
}

    
nome = input("Insira seu nome: ")
sala = input("Insira sua sala: ")
turno = input("Insira seu turno: ")
idade = int(input("Insira sua idade: "))
ano_letivo = input("Insira seu ano letivo: ")
while True:
    opcao = preven("Escolha uma opção:\n1. Exibir dados\n2. Salvar dados\n3. Acessar biblioteca\n4. Sair\nInsira: ")
    if opcao == 4:
        print("Saindo...")
        break
    elif opcao in opcoes:
        aluno = Aluno(nome, sala, turno, idade, ano_letivo)
        opcoes[opcao](aluno)
    else:
        print("Opção inválida. Tente novamente.")


