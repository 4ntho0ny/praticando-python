import validations as valid
from repositorio_improvisado import clientes, veiculos, servicos, contas, fornecedores, pecas
import styles

# ======== <<Cliente>> ========

def cadastrar_cliente():
    styles.clear_t()
    styles.titulo("Cadastrar Cliente")
    nome = cpf = data_nascimento = ""
    
    while True:
        nome = input("Nome: ")
        
        if not valid.str_vazia(nome):
            styles.msg_erro("O campo \"Nome\" não pode ser vazio!")
            continue
        elif not nome.isalpha():
            styles.msg_erro("Nome inválido")
            continue
        break
    
    while True:
        cpf = input("CPF: ")
        
        if not valid.str_vazia(cpf):
            
            styles.msg_erro("O campo \"CPF\" não pode ser vazio!")
            continue
        elif not valid.validar_cpf(cpf):
            continue
        break

    while True:
        data_nascimento = input("Data de nascimento(dia/mês/ano): ")
        if not valid.str_vazia(data_nascimento):
            styles.msg_erro("O campo \"Data de nascimento\" não pode ser vazio!")
            continue
        elif not valid.validar_data_nascimento(data_nascimento):
            continue
        break
    
    return nome, cpf, data_nascimento

def editar_cliente(cliente_dados_antigos):
    styles.clear_t()
    styles.titulo("Editar Cliente")
    nome, cpf, data_nascimento = cadastrar_cliente()
    cliente_dados_antigos.nome = nome
    cliente_dados_antigos.cpf = cpf
    cliente_dados_antigos.data_nascimento = data_nascimento

def excluir_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes.remove(cliente)
            styles.clear_t()
            styles.msg_sucesso("Cliente excluido!")
            return True
    styles.clear_t()
    styles.msg_erro("Este CPF não está na lista de clientes!")
    return False

def buscar_cliente_cpf(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    styles.clear_t()
    styles.msg_erro("Este CPF não está na lista de clientes!")
    return None

# ======== <<Veículo>> ========

def cadastrar_veiculo():
    styles.clear_t()
    styles.titulo("Cadastrar veículo")
    modelo = marca = placa = cor = ano = ""

    while True:
        modelo = input("Modelo do veículo: ")
        if not valid.str_vazia(modelo):
            styles.msg_erro("O campo \"Modelo\" não pode ser vazio!")
            continue
        break

    while True:
        marca = input("Marca do veículo: ")
        if not valid.str_vazia(marca):
            styles.msg_erro("O campo \"Marca\" não pode ser vazio!")
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
            styles.msg_erro("O campo \"Cor\" não pode ser vazio!")
            continue
        elif not cor.isalpha():
            styles.msg_erro("Cor inválida")
            continue
        break
    
    while True:
        ano = input("Ano do veículo: ")
        if not valid.validar_ano_veiculo(ano):
            continue
        break

    return modelo, marca, placa, cor, ano

def editar_veiculo(veiculo_dados_antigos):
    styles.clear_t()
    styles.titulo("Editar Veiculo")
    modelo, marca, placa, cor, ano = cadastrar_veiculo()
    veiculo_dados_antigos.modelo = modelo
    veiculo_dados_antigos.marca = marca
    veiculo_dados_antigos.placa = placa
    veiculo_dados_antigos.cor = cor
    veiculo_dados_antigos.ano = ano

def excluir_veiculo(placa):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            veiculos.remove(veiculo)
            styles.clear_t()
            styles.msg_sucesso("Veículo excluido!")
            return True
    styles.clear_t()
    styles.msg_erro("Esta placa não está na lista de veiculos!")
    return False

def buscar_veiculo_placa(placa):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            return veiculo
    styles.clear_t()
    styles.msg_erro("Esta placa não está na lista de veiculos!")
    return None

# ======== <<Serviço>> ========

def cadastrar_servico():
    styles.clear_t()
    styles.titulo("Registrar Serviço")
    nome = valor = data_termino = ""

    while True:
        nome = input("Nome do serviço: ")
        if not valid.str_vazia(nome):
            styles.msg_erro("O campo \"Nome do serviço\" não pode ser vazio!")
            continue
        elif not nome.isalpha():
            styles.msg_erro("Nome do serviço inválido!")
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

def editar_servico(servico_dados_antigos):
    styles.clear_t()
    styles.titulo("Editar servico")
    nome, valor, data_termino = cadastrar_servico()
    servico_dados_antigos.nome = nome
    servico_dados_antigos.valor = valor
    servico_dados_antigos.data_termino = data_termino

def excluir_servico(nome, data, valor):
    for servico in servicos:
        if servico.nome == nome and servico.data_termino == data and servico.valor == valor:
            servicos.remove(servico)
            styles.clear_t()
            styles.msg_sucesso("Serviço excluido!")
            return True
    styles.clear_t()
    styles.msg_erro("Este serviço não está na lista de servicos!")
    return False

def buscar_servico(nome):
    styles.clear_t()
    for servico in servicos:
        if servico.nome == nome:
            return servico
    styles.clear_t()
    styles.msg_erro("Este servico não está na lista de servicos!")
    return None

# ======== <<Fornecedor>> ========

def cadastrar_fornecedor():
    styles.clear_t()
    styles.titulo("Registrar Fornecedor")
    nome = cnpj = ""
    
    while True:
        nome = input("Nome do Fornecedor: ")
        
        if not valid.str_vazia(nome):
            styles.msg_erro("O campo \"Nome\" não pode ser vazio!")
            continue
        break
    
    while True:
        cnpj = input("CNPJ: ")
        
        if not valid.validar_cnpj(cnpj):
            continue
        break

    return nome, cnpj

def editar_fornecedor(fornecedor_dados_antigos):
    styles.clear_t()
    styles.titulo("Editar fornecedor")
    nome, cnpj = cadastrar_fornecedor()
    fornecedor_dados_antigos.nome = nome
    fornecedor_dados_antigos.cnpj = cnpj

def excluir_fornecedor(cnpj):
    for fornecedor in fornecedores:
        if fornecedor.cnpj == cnpj:
            fornecedores.remove(fornecedor)
            styles.clear_t()
            styles.msg_sucesso("Fornecedor excluido!")
            return True
    styles.clear_t()
    styles.msg_erro("Este CNPJ não está na lista de fornecedores!")
    return False

def buscar_fornecedor(cnpj):
    for fornecedor in fornecedores:
        if fornecedor.cnpj == cnpj:
            return fornecedor
    styles.clear_t()
    styles.msg_erro("Este CNPJ não está na lista de fornecedores!")
    return None

# ======== <<Peça>> ========

def cadastrar_peca():
    styles.clear_t()
    styles.titulo("Registrar Peça")
    nome = marca = preco = original = codigo = ""

    while True:
        nome = input("Nome da peça: ")

        if not valid.str_vazia(nome):
            styles.msg_erro("O campo \"Nome\" não pode ser vazio!")
            continue
        break
    
    while True:
        marca = input("Marca da peça: ")

        if not valid.str_vazia(marca):
            styles.msg_erro("O campo \"Marca\" não pode ser vazio!")
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
            styles.msg_erro("Este campo não pode ser vazio!")
            continue
        elif original == "s":
            original = True
        elif original == "n":
            original = False
        else:
            styles.msg_erro("Valor inválido!")
            continue
        break

    while True:
        codigo = input("Código da peça: ")

        if not valid.str_vazia(codigo):
            styles.msg_erro("O campo \"Código\" não pode ser vazio!")
            continue
        break
    
    return nome, marca, preco, original, codigo

def editar_peca(peca_dados_antigos):
    styles.clear_t()
    styles.titulo("Editar peca")
    nome, marca, preco, original, codigo = cadastrar_peca()
    peca_dados_antigos.nome = nome
    peca_dados_antigos.marca = marca
    peca_dados_antigos.preco = preco
    peca_dados_antigos.original = original
    peca_dados_antigos.codigo = codigo

def excluir_peca(codigo):
    for peca in pecas:
        if peca.codigo == codigo:
            pecas.remove(peca)
            styles.clear_t()
            styles.msg_sucesso("Peça excluida!")
            return True
    styles.clear_t()
    styles.msg_erro("Esta peça não está na lista de peças!")
    return False

def buscar_peca(codigo):
    for peca in pecas:
        if peca.codigo == codigo:
            return peca
    styles.clear_t()
    styles.msg_erro("Este codigo não está na lista de pecas!")
    return None

# ======== <<Conta>> ========

def cadastrar_conta():
    styles.clear_t()
    styles.titulo("Registrar Conta")
    nome = valor = data_vencimento = ""

    while True:
        nome = input("Registrar conta: ")

        if not valid.str_vazia(nome):
            styles.msg_erro("O campo \"Conta\" não pode ser vazio!")
            continue
        elif not nome.isalpha():
            styles.msg_erro("Conta inválida!")
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

def editar_conta(conta_dados_antigos):
    styles.clear_t()
    styles.titulo("Editar conta")
    nome, valor, data_vencimento = cadastrar_conta()
    conta_dados_antigos.nome = nome
    conta_dados_antigos.valor = valor
    conta_dados_antigos.data_vencimento = data_vencimento

def excluir_conta(nome, data, valor):
    for conta in contas:
        if conta.nome == nome and conta.data_vencimento == data and conta.valor == valor:
            contas.remove(conta)
            styles.clear_t()
            styles.msg_sucesso("Conta excluida!")
            return True
    styles.clear_t()
    styles.msg_erro("Esta conta não está na lista de contas!")
    return False

def buscar_conta(nome):
    styles.clear_t()
    for conta in contas:
        if conta.nome == nome:
            return conta
    styles.clear_t()
    styles.msg_erro("Este conta não está na lista de contas!")
    return None