import validations as valid
from repositorio_improvisado import clientes, veiculos, servicos, contas, fornecedores, pecas
import styles

# ======== <<Cliente>> ========

def cadastrar_cliente():
    styles.titulo("Cadastrar Cliente")
    nome = cpf = data_nascimento = ""
    
    while True:
        nome = input("Nome: ")
        
        if not valid.str_vazia(nome):
            styles.desenhar_barra()
            print("O campo \"Nome\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        elif not nome.isalpha():
            styles.desenhar_barra()
            print("Nome inválido")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        cpf = input("CPF: ")
        
        if not valid.str_vazia(cpf):
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
            styles.desenhar_barra()
            print("O campo \"Data de nascimento\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        elif not valid.validar_data_nascimento(data_nascimento):
            continue
        break
    
    return nome, cpf, data_nascimento

def excluir_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes.remove(cliente)
            styles.desenhar_barra()
            print("Cliente excluido!")
            styles.desenhar_barra()
            return True
    styles.desenhar_barra()
    print("Este CPF não está na lista de clientes!")
    styles.desenhar_barra()
    return False

# ======== <<Veículo>> ========

def cadastrar_veiculo():
    styles.titulo("Cadastrar veículo")
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
        elif not cor.isalpha():
            styles.desenhar_barra()
            print("Cor inválida")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        ano = input("Ano do veículo: ")
        if not valid.validar_ano_veiculo(ano):
            continue
        break

    return modelo, marca, placa, cor, ano

def excluir_veiculo(placa):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            veiculos.remove(veiculo)
            styles.desenhar_barra()
            print("Veículo excluido!")
            styles.desenhar_barra()
            return True
    styles.desenhar_barra()
    print("Esta placa não está na lista de veiculos!")
    styles.desenhar_barra()
    return False

# ======== <<Serviço>> ========

def cadastrar_servico():
    styles.titulo("Registrar Serviço")
    nome = valor = data_termino = ""

    while True:
        nome = input("Nome do serviço: ")
        if not valid.str_vazia(nome):
            styles.desenhar_barra()
            print("O campo \"Nome do serviço\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        elif not nome.isalpha():
            styles.desenhar_barra()
            print("Nome do serviço inválido!")
            styles.desenhar_barra()
            continue
        break

    while True:
        valor = valid.validar_valor()
        if valor == None:
            continue
        break

    while True:
        data_termino = valid.validar_data_final("do término do serviço")
        if data_termino == None:
            continue
        break

    return nome, valor, data_termino

def excluir_servico(nome, data, valor):
    for servico in servicos:
        if servico.nome == nome and servico.data_termino == data and servico.valor == valor:
            servicos.remove(servico)
            styles.desenhar_barra()
            print("Serviço excluido!")
            styles.desenhar_barra()
            return True
    styles.desenhar_barra()
    print("Este serviço não está na lista de servicos!")
    styles.desenhar_barra()
    return False

# ======== <<Fornecedor>> ========

def cadastrar_fornecedor():
    styles.titulo("Registrar Fornecedor")
    nome = cnpj = ""
    
    while True:
        nome = input("Nome do Fornecedor: ")
        
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

def excluir_fornecedor(cnpj):
    for fornecedor in fornecedores:
        if fornecedor.cnpj == cnpj:
            fornecedores.remove(fornecedor)
            styles.desenhar_barra()
            print("Fornecedor excluido!")
            styles.desenhar_barra()
            return True
    styles.desenhar_barra()
    print("Este CNPJ não está na lista de fornecedores!")
    styles.desenhar_barra()
    return False

# ======== <<Peça>> ========

def cadastrar_peca():
    styles.titulo("Registrar Peça")
    nome = marca = preco = original = codigo = ""

    while True:
        nome = input("Nome da peça: ")

        if not valid.str_vazia(nome):
            styles.desenhar_barra()
            print("O campo \"Nome\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break
    
    while True:
        marca = input("Marca da peça: ")

        if not valid.str_vazia(marca):
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
        
        if not valid.str_vazia(original):
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

    while True:
        codigo = input("Código da peça: ")

        if not valid.str_vazia(codigo):
            styles.desenhar_barra()
            print("O campo \"Código\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        break
    
    return nome, marca, preco, original, codigo

def excluir_peca(codigo):
    for peca in pecas:
        if peca.codigo == codigo:
            pecas.remove(peca)
            styles.desenhar_barra()
            print("Peça excluida!")
            styles.desenhar_barra()
            return True
    styles.desenhar_barra()
    print("Este código não está na lista de peças!")
    styles.desenhar_barra()
    return False

# ======== <<Conta>> ========

def cadastrar_conta():
    styles.titulo("Registrar Conta")
    nome = valor = data_vencimento = ""

    while True:
        nome = input("Registrar conta: ")

        if not valid.str_vazia(nome):
            styles.desenhar_barra()
            print("O campo \"Conta\" não pode ser vazio!")
            styles.desenhar_barra()
            continue
        elif not nome.isalpha():
            styles.desenhar_barra()
            print("Conta inválido")
            styles.desenhar_barra()
            continue
        break

    while True:
        valor = valid.validar_valor()

        if valor == None:
            continue
        break

    while True:
        data_vencimento = valid.validar_data_final("do vencimento da conta")

        if data_vencimento == None:
            continue
        break

    return nome, valor, data_vencimento

def excluir_conta(nome, data, valor):
    for conta in contas:
        if conta.nome == nome and conta.data_vencimento == data and conta.valor == valor:
            contas.remove(conta)
            styles.desenhar_barra()
            print("Conta excluida!")
            styles.desenhar_barra()
            return True
    styles.desenhar_barra()
    print("Esta conta não está na lista de contas!")
    styles.desenhar_barra()
    return False