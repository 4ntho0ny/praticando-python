from datetime import datetime

class Servico:
    def __init__(self, nome, valor, data_termino):
        self.nome = nome
        self.valor = valor
        self.data_termino = data_termino

    def validar_nome(nome):
        return True if nome != "" else False

    def validar_preco(preco):
        try:
            return bool(float(preco))
        except ValueError:
            return False
    
    def validar_data(data_nascimento):
        try:
            return bool(datetime.strptime(data_nascimento, "%d/%m/%Y"))
        except ValueError:
            return False

    def alterar(self, nome, valor, data_termino):
        self.nome = nome
        self.valor = valor
        self.data_termino = data_termino
    
    def relatorio(self):
        print(f'DADOS DO SERVIÇO\n   Nome: {self.nome}\n   Valor: {self.valor}\n   Data do término: {self.data_termino}')