from datetime import datetime
import re

class Cliente:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    @classmethod
    def validar_nome(nome):
        return True if nome != "" else False
    
    @classmethod
    def validar_cpf(cpf):
        return True if re.match(r"/^\d{3}\.\d{3}\.\d{3}\-\d{2}$/", cpf) else False

    @classmethod
    def validar_data(data_nascimento):
        try:
            return bool(datetime.strptime(data_nascimento, "%d/%m/%Y"))
        except ValueError:
            return False
    @classmethod
    def alterar(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
    @classmethod
    def relatorio(self):
        print(f'DADOS DO CLIENTE\n   Nome: {self.nome}\n   CPF: {self.cpf}\n   Data de Nascimento: {self.data_nascimento}')