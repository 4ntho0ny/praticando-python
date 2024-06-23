import styles

class Peca:
    def __init__(self, nome, marca, preco, original, codigo):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.original = original
        self.codigo = codigo
    
    def relatorio(self):
        styles.clear_t()
        styles.titulo("DADOS DA PECA")
        print(f'\n   Nome: {self.nome}\n   CÓDIGO: {self.codigo}\n   MARCA: {self.marca}\n   PREÇO: {self.preco}\n   ORIGINAL? {self.original}')