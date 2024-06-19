import re

class Conta:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def validar_nome(nome):
        return True if nome != "" else False

    def validar_valor(valor):
        try:
            return bool(float(valor))
        except ValueError:
            return False
    
    def relatorio(self):
        print(f'DADOS DO SERVIÇO\n   Nome: {self.nome}\n   Valor: {self.valor}')
    

