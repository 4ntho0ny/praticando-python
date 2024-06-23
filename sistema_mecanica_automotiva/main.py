import functions
import model.cliente as cliente
import model.veiculo as veiculo
import model.servico as servico
import model.fornecedor as fornecedor
import model.conta as conta
import model.peca as peca
import validations as valid
import styles
from repositorio_improvisado import clientes, veiculos, servicos, contas, fornecedores, pecas

running = True

while running:
    styles.titulo("Menu")
    opc = None
    try:
        opc = int(input("\n1-Seção de Cadastro\n2-Seção de exclusão\n3-Seção de alteração\n4-Geração de relatório\n-> "))
    except ValueError:
        styles.msg_erro("Opção indisponível!")

    # Seção de cadastro
    if opc == 1:
        styles.clear_t()
        styles.titulo("Cadastrar")
        opc_cad = None
        try:
            opc_cad = int(input("\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-peça\n6-conta\nqualquer outro número-Sair do cadastro\n-> "))
        except ValueError:
            styles.msg_erro("Opção indisponível!")

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
        
        elif opc_cad == 5:
            nome, marca, preco, original, codigo = functions.cadastrar_peca()
            peca = peca.Peca(nome, marca, preco, original, codigo)
            pecas.append(peca)

        elif opc_cad == 6:
            nome, valor, data_vencimento = functions.cadastrar_conta()
            conta = conta.Conta(nome, valor, data_vencimento)
            contas.append(conta)

        else:
            continue

        # ====================
        # LOGS
        # ====================
        # print(clientes[0].nome, clientes[1].nome)
        # print(veiculos[0].modelo)
        # print(servicos[0].nome)
        # print(pecas[0].nome)
        # print(fornecedores[0].nome)
        # print(contas[0].nome)
    
    # Seção de exclusão
    if opc == 2:
        styles.clear_t()
        styles.titulo("Excluir")
        opc_exclus = None
        try:
            opc_exclus = int(input("\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-peça\n6-conta\nqualquer outro número-Sair da seção de exclusão\n-> "))
        except ValueError:
            styles.msg_erro("Opção indisponível!")

        # ====================
        # LOGS
        # ====================
        # print(clientes[0].nome)
        # print(veiculos[0].modelo)
        # print(servicos[0].nome)
        # print(pecas[0].nome)
        # print(fornecedores[0].nome)
        # print(contas[0].nome)

        if opc_exclus == 1:
            styles.titulo("Excluir cliente")
            if not valid.verificar_lista_vazia(clientes):
                continue
            while True:
                cpf = input("Insira o cpf do cliente que deseja excluir: ")
                if functions.excluir_cliente(cpf) == False:
                    continue
                break

        elif opc_exclus == 2:
            styles.titulo("Excluir veículo")
            if not valid.verificar_lista_vazia(veiculos):
                continue
            while True:
                placa = input("Insira a placa do veículo que deseja excluir: ")
                if functions.excluir_veiculo(placa) == False:
                    continue
                break

        elif opc_exclus == 3:
            styles.titulo("Excluir serviço")
            if not valid.verificar_lista_vazia(servicos):
                continue
            while True:
                nome = input("Insira nome do serviço que deseja excluir: ")
                data = input("Insira data de termino do serviço que deseja excluir: ")
                valor = float(input("Insira valor do serviço que deseja excluir: "))
                if functions.excluir_servico(nome, data, valor) == False:
                    continue
                break

        elif opc_exclus == 4:
            styles.titulo("Excluir fornecedor")
            if not valid.verificar_lista_vazia(fornecedores):
                continue
            while True:
                cnpj = input("Insira CNPJ do fornecedor que deseja excluir: ")
                if functions.excluir_fornecedor(cnpj) == False:
                    continue
                break

        elif opc_exclus == 5:
            styles.titulo("Excluir peça")
            if not valid.verificar_lista_vazia(pecas):
                continue
            while True:
                codigo = input("Insira o código da peça que deseja excluir: ")
                if functions.excluir_peca(codigo) == False:
                    continue
                break

        elif opc_exclus == 6:
            styles.titulo("Excluir conta")
            if not valid.verificar_lista_vazia(contas):
                break
            while True:
                nome = input("Insira o nome da conta que deseja excluir: ")
                data = input("Insira a data da conta que deseja excluir: ")
                valor = float(input("Insira o valor da conta que deseja excluir: "))
                if functions.excluir_conta(nome, data, valor) == False:
                    continue
                break
        
        else:
            continue

        # ====================
        # LOGS
        # ====================
        # print(clientes[0].nome, clientes[1].nome)
        # print(veiculos[0].modelo)
        # print(servicos[0].nome)
        # print(pecas[0].nome)
        # print(fornecedores[0].nome)
        # print(contas[0].nome)
            