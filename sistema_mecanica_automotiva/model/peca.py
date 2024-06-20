class Peca:
    def __init__(self, nome, marca, preco, original):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.original = original

    def validar_nome(nome):
        return True if nome != "" else False

    def validar_marca(marca):
        return True if marca != "" else False

    def validar_preco(preco):
        try:
            return bool(float(preco))
        except ValueError:
            return False
    
    def validar_entrada_original(original):
        if original == "S" or original == "N":
            return True
        else:
            return False
    
    def atribuir_valor_original(original):
        if original == "S":
            return "sim"
        elif original == "N":
            return "não"

    def alterar(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    def relatorio(self):
        print(f'DADOS DA PEÇA\n   Nome: {self.nome}\n   MARCA: {self.cpf}\n   PREÇO: {self.preco}\n   ORIGINAL? {self.original}')