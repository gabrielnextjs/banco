# =========================================================
# FUNÇÃO COM PARÂMETROS PADRÃO (DEFAULT)
# =========================================================
def calculadora_juros_compostos(capital, meses, juros=0.05):
    """
    Calcula o montante de juros compostos.

    Args:
        capital (float): Valor inicial investido.
        meses (int): Período de investimento em meses.
        juros (float): Taxa de juros mensal. Padrão: 5%.

    Returns:
        float: Montante final arredondado em 2 casas decimais.
    """
    montante = capital * ((1 + juros) ** meses)
    return round(montante, 2)


lucro1 = calculadora_juros_compostos(1000, 12, 0.10)
lucro2 = calculadora_juros_compostos(500, 6)
print(f"Investimento 1: R$ {lucro1}")

# =========================================================
# *args
# =========================================================
def somar_tudo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total


print(somar_tudo(1, 2, 3))
print(somar_tudo(10, 20, 30, 40, 50))


def registrar_log(nivel, *mensagens):
    for msg in mensagens:
        print(f"[{nivel.upper()}] {msg}")


registrar_log("info", "Servidor iniciado", "Porta 8080 aberta", "3 usuários online")

# =========================================================
# **kwargs
# =========================================================
def criar_perfil_jogador(nome, **atributos):
    print(f"\n=== Perfil de {nome} ===")
    for atributo, valor in atributos.items():
        print(f"  {atributo}: {valor}")


criar_perfil_jogador(
    "SGP_Dev",
    nivel=99,
    guilda="STREET",
    rank="Diamante",
    kills=4200,
    vitorias=310,
)

# =========================================================
# FUNÇÕES QUE RETORNAM MÚLTIPLOS VALORES
# =========================================================
def analisar_lista(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)


menor, maior, media = analisar_lista([85, 92, 78, 95, 60])
print(f"Menor: {menor} | Maior: {maior} | Média: {media:.1f}")
