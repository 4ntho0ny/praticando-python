import validations as valid
import styles

# ======== <<Cliente>> ========

def cadastrar_nome():
    while True:
        nome = input("Nome: ")
        
        if nome == "":
            styles.desenhar_barra()
            print("O campo \"Nome\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        return nome
            
def cadastrar_cpf():
    while True:
        cpf = input("CPF: ")
        
        if cpf == "":
            styles.desenhar_barra()
            print("O campo \"CPF\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        elif len(cpf) != 11:
            print("CPF inválido!")
            continue
        return cpf

def cadastrar_data():
    while True:
        data = input("Data de nascimento(dia/mês/ano): ")
        if valid.validar_data(data) == None:
            continue
        return data

# ======== <<Veículo>> ========

def cadastrar_veiculo():
    print("\n============== <<Cadastrar veículo>> ==============\n")
    modelo = marca = placa = cor = ano = ""

    while True:
        modelo = input("Modelo do veículo: ")
        if not valid.str_vazia(modelo):
            print("O campo \"Modelo do veículo\" não pode ser vazio!")
            continue
        break

    while True:
        marca = input("Marca do veículo: ")
        if not valid.str_vazia(marca):
            styles.desenhar_barra()
            print("O campo \"Marca do veículo\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break

    while True:
        placa = input("Insira a placa do veículo: ")
        if not valid.validar_placa(placa):
            continue
        break
    
    while True:
        cor = input("Cor do veículo: ")
        if not valid.str_vazia(cor):
            styles.desenhar_barra()
            print("O campo \"Cor do veículo\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        ano = input("Ano do veículo: ")
        if not valid.validar_ano(ano):
            continue
        break

    return modelo, marca, placa, cor, ano

# ======== <<Serviço>> ========

def cadastrar_servico():
    print("\n============== <<Registrar Serviço>> ==============\n")
    nome = valor = data_termino = ""

    while True:
        nome = input("Nome do serviço: ")
        if not valid.str_vazia(nome):
            print("O campo \"Nome do serviço\" não pode ser vazio!")
            continue
        break

    while True:
        valor = valid.validar_valor()
        if valor == None:
            continue
        break

    while True:
        data_termino = input("Data do término do serviço (dia/mês/ano): ")
        if valid.validar_data(data_termino) == None:
            continue
        break

    return nome, valor, data_termino