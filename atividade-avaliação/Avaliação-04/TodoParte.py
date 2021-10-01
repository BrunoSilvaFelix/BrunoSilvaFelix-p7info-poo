class Pedido():
    def __init__(self, id, *itens):
        self.id = id
        self.itens = list(map(lambda x : x.__dict__, itens))

    def pagamento(self):
        print("Produtos:")
        for a in self.itens:
            print(a["nome"])
        print("Total:", sum(list(map(lambda x : x["preco"], self.itens))))

class itemPedido():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

pedido1 = Pedido(1, itemPedido("Carne", 20), itemPedido("Arroz",6))
pedido1.pagamento()
