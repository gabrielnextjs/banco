import functools
import time


def saudacao():
    return "Olá, mundo!"


minha_funcao = saudacao
print(minha_funcao())


def cronometrar(func):
    """Decorador que mede o tempo de execução de qualquer função."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"[TEMPO] '{func.__name__}' levou {fim - inicio:.4f}s")
        return resultado

    return wrapper


@cronometrar
def processar_dados(quantidade):
    """Simula um processamento demorado."""
    total = sum(range(quantidade))
    return total


resultado = processar_dados(1_000_000)
print(f"Resultado: {resultado}")

USUARIOS_ADMIN = {"sgp_dev", "admin_root"}


def requer_admin(func):
    """Bloqueia a execução se o usuário não for administrador."""

    @functools.wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if usuario not in USUARIOS_ADMIN:
            print(f"[ACESSO NEGADO] '{usuario}' não tem permissão de admin!")
            return None
        return func(usuario, *args, **kwargs)

    return wrapper


@requer_admin
def deletar_banco_de_dados(usuario):
    print(f"[{usuario}] Banco de dados deletado com sucesso.")


deletar_banco_de_dados("usuario_comum")
deletar_banco_de_dados("sgp_dev")


def repetir(vezes):
    """Faz a função repetir sua execução N vezes."""

    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                resultado = func(*args, **kwargs)
            return resultado

        return wrapper

    return decorador


@repetir(vezes=3)
def enviar_ping(servidor):
    print(f"Ping enviado para {servidor}...")


enviar_ping("sgpnoticias.com.br")
