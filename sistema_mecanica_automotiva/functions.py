from datetime import datetime

# ======== <<Cliente>> ========

def cadastrar_nome():
    while True:
        nome = input("Nome: ")
        
        if nome == "":
            print("O campo \"Nome\" não pode ser vazio!")
            continue
        return nome
            
def cadastrar_cpf():
    while True:
        cpf = input("CPF: ")
        
        if cpf == "":
            print("O campo \"CPF\" não pode ser vazio!")
            continue
        elif len(cpf) != 11:
            print("CPF inválido!")
            continue
        return cpf

def cadastrar_data():
    while True:
        data = input("Data de nascimento(dia/mês/ano): ")
        if data == "":
            print("O campo \"Data de nascimento\" não pode ser vazio!")
            continue
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("Data insira a data no formato dia/mês/ano!")
            continue
        return data

# ======== <<Veículo>> ========

def cadastrar_veiculo():
    while True:
        modelo = input("Modelo do veículo: ")
        if not validar_dados_veiculo(modelo):
            print("O campo \"Modelo do veículo\" não pode ser vazio!")
            continue
        
        marca = input("Marca do veículo: ")
        if not validar_dados_veiculo(marca):
            print("O campo \"Marca do veículo\" não pode ser vazio!")
            continue
        
        placa = input("Insira a placa do veículo: ")
        if not validar_placa(placa):
            continue
        
        cor = input("Cor do veículo: ")
        if not validar_dados_veiculo(cor):
            print("O campo \"Cor do veículo\" não pode ser vazio!")
            continue
        
        ano = input("Ano do veículo")
        if not validar_ano(ano):
            continue
        
        return modelo, marca, placa, cor, ano
            
# ======== validaçoes ========

def validar_dados_veiculo(dados):
    if dados == "":
        return False
    return True
    
def validar_placa(placa):
    if placa == "":
        print("O campo \"Placa\" não pode ser vazio!")
        return False
    elif len(placa) == 7:
        if placa[0:3].isapha() and placa[3].isnum() and placa[4].isalpha() and placa[5:7].isnum():
            return True
        return False
    else:
        return False

def validar_ano(ano):
    if ano.isdigit():
        if ano > datetime.now().strftime("%Y"):
            print("Valor do ano inválido")
            return False
        return True
    else:
        print("Digite apenas o ano do veículo")