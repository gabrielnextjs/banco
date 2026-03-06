# =========================================================
# AS FORMAS DE IMPORTAR
# =========================================================
import math

resultado = math.sqrt(144)

from math import pi, sqrt

resultado = sqrt(144)
area = pi * (5**2)

from math import *  # noqa: F403,F401

import datetime as dt
import json as j

agora = dt.datetime.now()


def iniciar_sistema():
    print("Sistema iniciado!")


def parar_sistema():
    print("Sistema encerrado.")


if __name__ == "__main__":
    iniciar_sistema()
    print("Rodando em modo principal...")
    parar_sistema()
