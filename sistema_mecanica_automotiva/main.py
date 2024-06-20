import sistema_mecanica_automotiva.functions as functions
import cliente
import veiculo
import servico
import fornecedor
import conta

running = True

# Banco de dados improvisado
clientes = []
veiculos = []
fornecedores = []
contas = []
servicos = []

while running:
    opc = int(input("1-Seção de Cadastro\n->"))

    if opc == 1:
        opc_cad = int(input("\n============== <<Cadastrar>> ==============\n1-cliente\n2-veículo\n3-serviço\n4-Fornecedor\n5-conta\n0-Sair\n-> "))

        if opc_cad == 1:
            nome = functions.cadastrar_nome()
            cpf = functions.cadastrar_cpf()
            data_nascimento = functions.cadastrar_data()
            cliente = cliente.Cliente(nome, cpf, data_nascimento)
            clientes.append(cliente)

        elif opc_cad == 2:
            modelo, marca, placa, cor, ano = functions.cadastrar_veiculo()
            veiculo = veiculo.Veiculo(modelo, marca, placa, cor, ano)
            veiculos.append(veiculo)
        
        # elif opc_cad == 3: