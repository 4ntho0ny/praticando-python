import styles

class Fornecedor:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
    
    def relatorio(self):
        styles.clear_t()
        styles.titulo("DADOS DO FORNECEDOR")
        print(f'\n   Nome: {self.nome}\n   CNPJ: {self.cnpj}')
