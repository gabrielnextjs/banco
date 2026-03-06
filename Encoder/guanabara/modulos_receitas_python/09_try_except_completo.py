try:
    numero = int("10")  # substitui input("Quantas caixas? ")
    receita = 1500.00
    preco_por_caixa = receita / numero

    with open("banco_secreto.txt", "r", encoding="utf-8") as f:
        dados = f.read()

except ValueError:
    print("ERRO: Digite apenas números inteiros!")

except ZeroDivisionError:
    print("ERRO: Não é possível dividir por zero!")

except FileNotFoundError:
    print("ERRO: O arquivo 'banco_secreto.txt' não foi encontrado.")

except PermissionError:
    print("ERRO: Permissão negada pelo sistema operacional.")

except (TypeError, AttributeError) as e:
    print(f"ERRO DE TIPO/ATRIBUTO: {e}")

except Exception as erro_desconhecido:
    print(f"PANE CRÍTICA: {type(erro_desconhecido).__name__}: {erro_desconhecido}")

else:
    print(f"Sucesso! Cada caixa custa R$ {preco_por_caixa:.2f}")
    print("Dados do banco carregados com êxito!")

finally:
    print("Encerrando conexão com o servidor e liberando memória...")


# =========================================================
# LEVANTANDO SEUS PRÓPRIOS ERROS (raise)
# =========================================================
def sacar_dinheiro(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo!")
    if valor > saldo:
        raise ValueError(f"Saldo insuficiente. Saldo: R${saldo:.2f}")
    return saldo - valor


try:
    novo_saldo = sacar_dinheiro(500.00, 700.00)
except ValueError as e:
    print(f"Operação recusada: {e}")
