import validators as v

class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__matricula = ""
        self.__senha = ""
        self.__fone = ""
        self.__email = ""
        self.__endereco = ""
    
    def cadastrar_pessoa(self):
        while True:
            nome = input("Nome: ")
            if v.isEmpty(nome):
                continue
            elif nome.isalpha():
                self.__nome = nome
                break
            print("Digite apenas letras")
        while True:
            matricula = input("Matricula: ")
            if v.isEmpty(matricula):
                continue
            elif matricula.isnumeric():
                self.__matricula = matricula
                break
            print("Digite apenas números")
        while True:
            senha = input("Senha: ")
            if v.isEmpty(senha):
                continue
            self.__senha = senha
            break
        while True:
            fone = input("Telefone (DDD999999999): ")
            if v.isEmpty(fone):
                continue
            elif fone.isnumeric():
                self.__fone = fone
                break
            print("Digite apenas números")
        while True:
            email = input("Email: ")
            if v.isEmpty(email):
                continue
            elif "@" in email:
                self.__email = email
                break
            print("Email inválido")
        while True:
            endereco = input("Endereco: ")
            if v.isEmpty(endereco):
                continue
            self.__endereco = endereco
            break
    
    def relatorio(self):
        print(
f'''
==========<<DADOS>>==========
Nome: {self.__nome}
Matrícula: {self.__matricula}
Senha: {self.__senha}
Telefone: {self.__fone}
Email: {self.__email}
Endereço: {self.__endereco}
=============================
''')