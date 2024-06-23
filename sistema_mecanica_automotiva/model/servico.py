import styles

class Servico:
    def __init__(self, nome, valor, data_termino):
        self.nome = nome
        self.valor = valor
        self.data_termino = data_termino
    
    def relatorio(self):
        styles.titulo("DADOS DO SERVIÇO")
        print(f'\n   Nome: {self.nome}\n   Valor: {self.valor}\n   Data do término: {self.data_termino}')
        