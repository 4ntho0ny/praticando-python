import styles

class Veiculo:
    def __init__(self, modelo, marca, placa, cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.cor = cor
        self.ano = ano
    
    def relatorio(self):
        styles.clear_t()
        styles.titulo("DADOS DO VEICULO")
        print(f'\n   Modelo: {self.modelo}\n   Marca: {self.marca}\n   Placa: {self.placa}\n   Cor: {self.cor}\n   Ano: {self.ano}')