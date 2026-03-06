import json
import os
from datetime import datetime

ARQUIVO_DB = "estoque.json"


class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
        }

    def __str__(self):
        return (
            f"[ID:{self.id:03d}] {self.nome:<20} "
            f"R${self.preco:>8.2f}  Qtd: {self.quantidade:>4d}"
        )


def carregar_estoque():
    if not os.path.exists(ARQUIVO_DB):
        return []
    try:
        with open(ARQUIVO_DB, "r", encoding="utf-8") as f:
            dados = json.load(f)
        return [Produto(**p) for p in dados]
    except (json.JSONDecodeError, KeyError):
        print("[AVISO] Banco de dados corrompido. Iniciando do zero.")
        return []


def salvar_estoque(estoque):
    with open(ARQUIVO_DB, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in estoque], f, indent=4, ensure_ascii=False)


def listar_produtos(estoque):
    if not estoque:
        print("\n[INFO] Nenhum produto cadastrado.")
        return
    print(f"\n{'=' * 55}")
    print(f"  {'ID':<6} {'Nome':<20} {'Preço':>9}  {'Qtd':>6}")
    print(f"{'=' * 55}")
    for produto in estoque:
        print(f"  {produto}")
    print(f"{'=' * 55}")
    total_itens = sum(p.quantidade for p in estoque)
    valor_total = sum(p.preco * p.quantidade for p in estoque)
    print(
        f"  Total em estoque: {total_itens} itens | "
        f"Valor total: R$ {valor_total:,.2f}\n"
    )


def buscar_produto(estoque, id_busca):
    for produto in estoque:
        if produto.id == id_busca:
            return produto
    return None


def adicionar_produto(estoque):
    print("\n--- Cadastrar Novo Produto ---")
    try:
        novo_id = max((p.id for p in estoque), default=0) + 1
        nome = input("Nome do produto: ").strip()
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        preco = float(input("Preço (ex: 299.90): "))
        quantidade = int(input("Quantidade inicial: "))
        if preco <= 0 or quantidade < 0:
            raise ValueError("Preço e quantidade devem ser positivos.")

        novo = Produto(novo_id, nome, preco, quantidade)
        estoque.append(novo)
        salvar_estoque(estoque)

        ts = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"[{ts}] Produto '{nome}' cadastrado com ID {novo_id:03d}!")

    except ValueError as e:
        print(f"[ERRO] Dado inválido: {e}")


def registrar_venda(estoque):
    print("\n--- Registrar Venda ---")
    try:
        id_venda = int(input("ID do produto vendido: "))
        produto = buscar_produto(estoque, id_venda)

        if produto is None:
            print(f"[ERRO] Produto ID {id_venda} não encontrado.")
            return

        qtd = int(input(f"Quantidade (disponível: {produto.quantidade}): "))
        if qtd <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        if qtd > produto.quantidade:
            raise ValueError(f"Estoque insuficiente! Disponível: {produto.quantidade}")

        produto.quantidade -= qtd
        salvar_estoque(estoque)
        total = produto.preco * qtd
        print(f"Venda registrada! {qtd}x {produto.nome} = R$ {total:.2f}")

        if produto.quantidade <= 5:
            print(
                f"[ALERTA] Estoque baixo: apenas {produto.quantidade} "
                "unidades restantes!"
            )

    except ValueError as e:
        print(f"[ERRO] {e}")


def main():
    estoque = carregar_estoque()
    print("\n  Sistema de Gestão de Estoque SGP Tech v1.0")

    while True:
        print("\n[1] Listar  [2] Adicionar  [3] Vender  [0] Sair")
        opcao = input("Opção: ").strip()

        match opcao:
            case "1":
                listar_produtos(estoque)
            case "2":
                adicionar_produto(estoque)
            case "3":
                registrar_venda(estoque)
            case "0":
                print("Encerrando sistema. Até logo!")
                break
            case _:
                print("[AVISO] Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
