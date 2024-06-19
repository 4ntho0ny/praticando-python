import re

class Fornecedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj

    def validar_nome(nome):
        return True if nome != "" else False

    def validar_cnpj(cnpj):
        return True if re.match(r"\\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}\\", cnpj) else False

    def alterar(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
    
    def relatorio(self):
        print(f'DADOS DO CLIENTE\n   Nome: {self.nome}\n   CNPJ: {self.cnpj}')
