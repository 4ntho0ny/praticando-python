import validations as valid
import styles

# ======== <<Cliente>> ========

def cadastrar_cliente():
    nome = cpf = data_nascimento = ""
    
    while True:
        print("\n============== <<Cadastrar Cliente>> ==============")
        nome = input("Nome: ")
        
        if valid.str_vazia(nome):
            styles.desenhar_barra()
            print("O campo \"Nome\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        cpf = input("CPF: ")
        
        if valid.str_vazia(cpf):
            styles.desenhar_barra()
            print("O campo \"CPF\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        elif not valid.validar_cpf(cpf):
            continue
        break

    while True:
        data_nascimento = input("Data de nascimento(dia/mês/ano): ")
        if not valid.str_vazia(data_nascimento):
            continue
        elif not valid.validar_data_nascimento(data_nascimento):
            continue
        break
    
    return nome, cpf, data_nascimento

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
        if not valid.validar_ano_veiculo(ano):
            continue
        break

    return modelo, marca, placa, cor, ano

# ======== <<Serviço>> ========

def cadastrar_servico():
    print("\n============== <<Registrar Serviço>> ==============")
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
        if valid.validar_data_termino(data_termino) == None:
            continue
        break

    return nome, valor, data_termino

# ======== <<Fornecedor>> ========

def cadastrar_fornecedor():
    print("\n============== <<Registrar Serviço>> ==============")
    nom = cnpj = ""
    
    while True:
        nome = input("Nome do Fornecedor")
        
        if not valid.str_vazia(nome):
            styles.desenhar_barra()
            print("O campo \"Nome\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        cnpj = input("CNPJ: ")
        
        if not valid.validar_cnpj(cnpj):
            continue
        break
    return nome, cnpj

# ======== <<Peça>> ========

def cadastrar_peca():
    print("\n============== <<Registrar Peça>> ==============")
    nome = marca = preco = original = ""

    while True:
        if valid.str_vazia(nome):
            styles.desenhar_barra()
            print("O campo \"Nome\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        if valid.str_vazia(marca):
            styles.desenhar_barra()
            print("O campo \"Marca\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        preco = valid.validar_valor()
        
        if preco == None:
            continue
        break
    
    while True:
        original = input("Peça original(s/n)? ").lower().strip()
        
        if valid.str_vazia(original):
            styles.desenhar_barra()
            print("Este campo não pode ser vazio!")
            styles.desenhar_barra()
            continue
        elif original == "s":
            original = True
        elif original == "n":
            original = False
        else:
            styles.desenhar_barra()
            print("Valor inválido")
            styles.desenhar_barra()
            continue
        break
    
    return nome, marca, preco, original