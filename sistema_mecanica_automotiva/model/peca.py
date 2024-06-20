class Peca:
    def __init__(self, nome, marca, preco, original):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.original = original
    
    def relatorio(self):
        print(f'DADOS DA PEÇA\n   Nome: {self.nome}\n   MARCA: {self.cpf}\n   PREÇO: {self.preco}\n   ORIGINAL? {self.original}')