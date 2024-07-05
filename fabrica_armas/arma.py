import validators as v

class Arma:
    def __init__(self):
        self.__tipo = ""
        self.__numero_serie = 0
        self.__calibre = 0
        self.__valor = 0.0
        self.__data_fabric = ""
        self.__marca = ""

    def cadastrar_arma(self):
        while True:
            tipo = input("Tipo de arma: ")
            if v.isEmpty(tipo):
                continue
            elif tipo.isalpha():
                self.__tipo = tipo
                break
            print("Digite apenas letras")
        while True:
            try:
                num_serie = int(input("Número de série: "))
            except ValueError:
                print("Número de serie inválido")
                continue
            self.__numero_serie = num_serie
            break
        while True:
            try:
                calibre = int(input("Calibre: "))
            except ValueError:
                print("Número do calibre inválido")
                continue
            if calibre <= 0:
                print("O número do calibre tem que ser maior que 0")
                continue
            self.__calibre = calibre
            break
        while True:
            try:
                valor = float(input("Valor: "))
            except ValueError:
                print("Valor inválido")
                continue
            if valor <= 0:
                print("O valor tem que ser maior que 0")
                continue
            self.__valor = valor
            break
        while True:
            try:
                data_fab = v.validar_formato_data(input("Data da fabricação (dia/mês/ano): "))
            except ValueError:
                print("Data com formato inválido")
                continue
            self.__data_fabric = data_fab.date()
            break
        while True:
            marca = input("Marca: ")

            if v.isEmpty(marca):
                continue
            elif marca.isalpha():
                self.__marca = marca
                break
            print("Digite apenas letras")

    def relatorio(self):
        print(
f'''
==========<<DADOS>>==========
Tipo: {self.__tipo}
Número de série: {self.__numero_serie}
Calibre: {self.__calibre}
Valor: {self.__valor}
Data de fabricação: {self.__data_fabric}
Marca: {self.__marca}
=============================
''')