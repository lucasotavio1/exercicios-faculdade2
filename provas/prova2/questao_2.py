from datetime import date
from typing import List


class Cliente:
    def __init__(self, id: int, nome: str, email: str, endereco: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.carrinho = Carrinho(id=self.id)

    def fazer_pedido(self):
        pedido = self.carrinho.checkout()
        return pedido


class Produto:
    def __init__(self, codigo: int, nome: str, descricao: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def consultar_detalhes(self):
        return f"Código: {self.codigo}\nNome: {self.nome}\nDescrição: {self.descricao}\nPreço: {self.preco}"


class ItemPedido(Produto):
    def __init__(self, codigo: int, nome: str, descricao: str, preco: float, quantidade: int, subtotal: float):
        super().__init__(codigo, nome, descricao, preco)
        self.quantidade = quantidade
        self.subtotal = subtotal


class Pedido:
    def __init__(self, id: int, data: date, total: float = 0.0):
        self.id = id
        self.data = data
        self.total = total

    def adicionar_produto(self, produto: Produto, quantidade: int):
        subtotal = produto.preco * quantidade
        item = ItemPedido(produto.codigo, produto.nome,
                          produto.descricao, produto.preco, quantidade, subtotal)
        return item

    def calcular_total(self, itens_pedido: list[ItemPedido]):
        total_calculado = 0.0
        for item in itens_pedido:
            total_calculado += item.subtotal
        return total_calculado


class Carrinho:
    def __init__(self, id: int, itens: List[ItemPedido] = None):
        self.id = id
        self.itens = itens if itens is not None else []

    def adicionar_item(self, produto: Produto, quantidade: int):
        subtotal = produto.preco * quantidade
        item = ItemPedido(produto.codigo, produto.nome,
                          produto.descricao, produto.preco, quantidade, subtotal)
        self.itens.append(item)

    def remover_item(self, item: ItemPedido):
        self.itens.remove(item)

    def checkout(self):
        pedido = Pedido(id=1, data=date.today())
        total_pedido = pedido.calcular_total(self.itens)
        pedido.total = total_pedido
        return pedido


class Boleto:
    def __init__(self, codigo_barras: str, vencimento: date):
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar_pagamento(self) -> bool:
        print(f"Processando pagamento com Boleto: {self.codigo_barras}")
        return True


class CartaoCredito:
    def __init__(self, numero: str, bandeira: str):
        self.numero = numero
        self.bandeira = bandeira

    def processar_pagamento(self) -> bool:
        print(
            f"Processando pagamento com Cartão de Crédito {self.bandeira}: **** **** **** {self.numero[-4:]}")
        return True


class Pagamento:
    def __init__(self, pagamento_id: str, valor: float):
        self.pagamento_id = pagamento_id
        self.valor = valor

    def realizar_pagamento(self, forma_pagamento) -> bool:
        if hasattr(forma_pagamento, 'processar_pagamento') and callable(getattr(forma_pagamento, 'processar_pagamento')):
            print(
                f"Iniciando pagamento ID: {self.pagamento_id} no valor de R$ {self.valor:.2f}")
            return forma_pagamento.processar_pagamento()
        else:
            print(
                "Forma de pagamento inválida. Não possui o método 'processar_pagamento'.")
            return False


class PagamentoOnline(Pagamento):
    def __init__(self, id: int, valor: float, numero_cartao: str, bandeira_cartao: str, gateway: str, transacao_id: str):
        super().__init__(str(id), valor)
        self.numero_cartao = numero_cartao
        self.bandeira_cartao = bandeira_cartao
        self.gateway = gateway
        self.transacao_id = transacao_id

    def realizar_pagamento(self) -> bool:
        print(
            f"  Processando pagamento online ID: {self.pagamento_id} no valor de R$ {self.valor:.2f}")
        print(f"  Via gateway: {self.gateway}")
        print(f"  Transação ID: {self.transacao_id}")
        print(
            f"  Cartão: {self.bandeira_cartao} **** **** **** {self.numero_cartao[-4:]}")
        return True
