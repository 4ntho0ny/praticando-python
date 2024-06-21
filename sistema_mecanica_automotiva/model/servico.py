from datetime import datetime

class Servico:
    def __init__(self, nome, valor, data_termino):
        self.nome = nome
        self.valor = valor
        self.data_termino = data_termino
    
    def relatorio(self):
        print(f'DADOS DO SERVIÇO\n   Nome: {self.nome}\n   Valor: {self.valor}\n   Data do término: {self.data_termino}')
        