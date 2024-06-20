import re

class Conta:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def relatorio(self):
        print(f'DADOS DO SERVIÇO\n   Nome: {self.nome}\n   Valor: {self.valor}')
    

