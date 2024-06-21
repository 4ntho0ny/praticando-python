class Peca:
    def __init__(self, nome, marca, preco, original, codigo):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.original = original
        self.codigo = codigo
    
    def relatorio(self):
        print(f'DADOS DA PEÇA\n   Nome: {self.nome}\n   CÓDIGO:{self.codigo}\n   MARCA: {self.cpf}\n   PREÇO: {self.preco}\n   ORIGINAL? {self.original}')