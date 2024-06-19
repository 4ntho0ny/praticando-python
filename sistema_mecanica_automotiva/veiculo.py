class Veiculo:
    def __init__(self, modelo, marca, placa, cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.cor = cor
        self.ano = ano

    def is_none(strng):
        return True if strng != "" else False

    def validar_placa(placa):
        if placa == "":
            return False
        elif placa[0:3].isapha() and placa[3].isnum() and placa[4].isalpha() and placa[5:7].isnum():
            return True
        else:
            return False

    def alterar(self, modelo, marca, placa, cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.cor = cor
        self.ano = ano
    
    def relatorio(self):
        print(f'DADOS DO CLIENTE\n   Modelo: {self.modelo}\n   Marca: {self.marca}\n   Placa: {self.placa}\n   Cor: {self.cor}\n   Ano: {self.ano}')