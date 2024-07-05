import validators as v

class Cliente:
    def __init__(self):
        self.__nome = ""
        self.__cpf = ""
        self.__data_nascimento = ""
        self.__sexo = ""
        self.__endereco = ""
        self.__salario = ""
    
    def cadastrar_cliente(self):
        while True:
            nome = input("Nome: ")
            if v.isEmpty(nome):
                continue
            elif nome.isalpha():
                self.__nome = nome
                break
            print("Digite apenas letras")
        while True:
            cpf = input("CPF: ")
            if v.isEmpty(cpf):
                continue
            elif cpf.isnumeric():
                if len(cpf) != 11:
                    print("CPF inválido")
                    continue
                self.__cpf = cpf
                break
            print("Digite apenas números")
        while True:
            try:
                data_nascimento = v.validar_formato_data(input("Data de nascimento: "))
            except ValueError:
                print("Data com formato inválido")
                continue
            self.__data_nascimento = data_nascimento.date()
            break
        while True:
            sexo = input("Sexo (m/f): ").lower()
            if sexo == 'm' or sexo == 'f':
                self.__sexo = sexo
                break
            print("Sexo inválido")
            continue
        while True:
            endereco = input("Endereco: ")
            if v.isEmpty(endereco):
                continue
            self.__endereco = endereco
            break
        while True:
            try:
                salario = float(input("Salário: "))
            except ValueError:
                print("Valor do salário inválido")
                continue
            if salario <= 0:
                print("Digite apenas números positivos")
                continue
            self.__salario = salario
            break

    def relatorio(self):
        print(
f'''
==========<<DADOS>>==========
Nome: {self.__nome}
CPF: {self.__cpf}
Data nascimento: {self.__data_nascimento}
Sexo: {self.__sexo}
Salário: {self.__salario}
Endereço: {self.__endereco}
=============================
''')