import styles

class Cliente:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
    def relatorio(self):
        styles.clear_t()
        styles.titulo("DADOS DO CLIENTE")
        print(f'\n   Nome: {self.nome}\n   CPF: {self.cpf}\n   Data de Nascimento: {self.data_nascimento}')