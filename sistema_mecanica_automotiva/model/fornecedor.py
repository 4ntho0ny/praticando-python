class Fornecedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
    
    def relatorio(self):
        print(f'DADOS DO CLIENTE\n   Nome: {self.nome}\n   CNPJ: {self.cnpj}')
