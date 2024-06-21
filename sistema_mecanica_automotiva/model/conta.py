class Conta:
    def __init__(self, nome, valor, data_vencimento):
        self.nome = nome
        self.valor = valor
        self.data_vencimento = data_vencimento
    
    def relatorio(self):
        print(f'DADOS DO SERVIÇO\n   Nome: {self.nome}\n   Valor: {self.valor}\n   Data_vencimento: {self.data_vencimento}')
    

