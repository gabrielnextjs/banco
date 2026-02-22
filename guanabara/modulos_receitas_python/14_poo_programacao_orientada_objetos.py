class Jogador:
    # ATRIBUTO DE CLASSE
    jogo = "Free Fire"
    total_jogadores = 0

    def __init__(self, nome, nivel, guilda="Sem Guilda"):
        self.nome = nome
        self.nivel = nivel
        self.guilda = guilda
        self.kills = 0
        self.vivo = True
        Jogador.total_jogadores += 1

    def atirar(self, alvo):
        if self.vivo:
            self.kills += 1
            print(f"{self.nome} eliminou {alvo}! Total: {self.kills} kills.")
        else:
            print(f"{self.nome} está morto e não pode atirar.")

    def morrer(self):
        self.vivo = False
        print(f"{self.nome} foi eliminado!")

    def __str__(self):
        status = "Vivo" if self.vivo else "Eliminado"
        return (
            f"[{self.jogo}] {self.nome} | Nv.{self.nivel} | "
            f"Guilda: {self.guilda} | Kills: {self.kills} | {status}"
        )


jogador1 = Jogador("SGP_Dev", 99, "STREET")
jogador2 = Jogador("Renegado77", 45)

jogador1.atirar("Inimigo_A")
jogador1.atirar("Inimigo_B")
jogador2.morrer()
jogador2.atirar("Alguém")

print(jogador1)
print(jogador2)
print(f"Total de jogadores criados: {Jogador.total_jogadores}")


class JogadorPremium(Jogador):
    def __init__(self, nome, nivel, guilda, skin_exclusiva):
        super().__init__(nome, nivel, guilda)
        self.skin_exclusiva = skin_exclusiva
        self.revives = 3

    def morrer(self):
        if self.revives > 0:
            self.revives -= 1
            print(f"{self.nome} usou um REVIVE! Revives restantes: {self.revives}")
        else:
            super().morrer()

    def __str__(self):
        base = super().__str__()
        return f"{base} | Skin: {self.skin_exclusiva} | Revives: {self.revives}"


premium = JogadorPremium("ElitePlayer", 99, "STREET", "Dragão Dourado")
premium.morrer()
premium.morrer()
premium.morrer()
premium.morrer()
print(premium)
