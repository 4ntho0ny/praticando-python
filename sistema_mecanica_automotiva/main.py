import functions
import model.cliente as cliente
import model.veiculo as veiculo
import model.servico as servico
import model.fornecedor as fornecedor
import model.conta as conta
import model.peca as peca
import styles

running = True

# Banco de dados improvisado
clientes = []
veiculos = []
fornecedores = []
contas = []
servicos = []
pecas = []

while running:
    opc = None
    try:
        opc = int(input("\n============== <<Menu>> ==============\n1-Seção de Cadastro\n-> "))
    except ValueError:
        styles.desenhar_barra()
        print("Escolha uma opção!")
        styles.desenhar_barra()

    if opc == 1:
        opc_cad = int(input("\n============== <<Cadastrar>> ==============\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-conta\n6-peça\n0-Sair\n-> "))

        if opc_cad == 1:
            nome, cpf, data_nascimento = functions.cadastrar_cliente()
            cliente = cliente.Cliente(nome, cpf, data_nascimento)
            clientes.append(cliente)

        elif opc_cad == 2:
            modelo, marca, placa, cor, ano = functions.cadastrar_veiculo()
            veiculo = veiculo.Veiculo(modelo, marca, placa, cor, ano)
            veiculos.append(veiculo)
        
        elif opc_cad == 3:
            nome, valor, data_termino = functions.cadastrar_servico()
            servico = servico.Servico(nome, valor, data_termino)
            servicos.append(servico)
        
        elif opc_cad == 4:
            nome, cnpj = functions.cadastrar_fornecedor()
            fornecedor = fornecedor.Fornecedor(nome, cnpj)
            fornecedores.append(fornecedor)
        
        elif opc_cad == 6:
            nome, marca, preco, original = functions.cadastrar_peca()
            peca = peca.Peca(nome, marca, preco, original)
            pecas.append(peca)
        else:
            continue