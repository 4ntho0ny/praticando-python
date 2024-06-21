import functions
import model.cliente as cliente
import model.veiculo as veiculo
import model.servico as servico
import model.fornecedor as fornecedor
import model.conta as conta
import model.peca as peca
import styles
from repositorio_improvisado import clientes, veiculos, servicos, contas, fornecedores, pecas

running = True

while running:
    styles.titulo("Menu")
    opc = None
    try:
        opc = int(input("\n1-Seção de Cadastro\n2-Seção de exclusão\n3-Seção de alteração\n4-Geração de relatório\n-> "))
    except ValueError:
        styles.desenhar_barra()
        print("Opção indisponível!")
        styles.desenhar_barra()

    # Seção de cadastro
    if opc == 1:
        styles.titulo("Cadastrar")
        opc_cad = None
        try:
            opc_cad = int(input("\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-peça\n6-conta\nqualquer botão restante-Sair do cadastro\n-> "))
        except ValueError:
            styles.desenhar_barra()
            print("Opção indisponível!")
            styles.desenhar_barra()

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
        styles.titulo("Excluir")
        opc_exclus = None
        try:
            opc_exclus = int(input("\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-peça\n6-conta\nqualquer botão restante-Sair da seção de exclusão\n-> "))
        except ValueError:
            styles.desenhar_barra()
            print("Opção indisponível!")
            styles.desenhar_barra()
        
        excluir = False


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
            while True:
                cpf = input("Insira o cpf do cliente que deseja excluir: ")
                excluir = functions.excluir_cliente(cpf)
                if excluir == False:
                    continue
                break

        elif opc_exclus == 2:
            styles.titulo("Excluir veículo")
            while True:
                placa = input("Insira a placa do veículo que deseja excluir: ")
                excluir = functions.excluir_veiculo(placa)
                if excluir == False:
                    continue
                break

        # NAO ESTA EXCLUINDO
        # elif opc_exclus == 3:
        #     styles.titulo("Excluir serviço")
        #     while True:
        #         nome = input("Insira nome do serviço que deseja excluir: ")
        #         data = input("Insira data de termino do serviço que deseja excluir: ")
        #         valor = input("Insira valor do serviço que deseja excluir: ")
        #         excluir = functions.excluir_servico(nome, data, valor)
        #         if excluir == False:
        #             continue
        #         break

        elif opc_exclus == 4:
            styles.titulo("Excluir fornecedor")
            while True:
                cnpj = input("Insira CNPJ do fornecedor que deseja excluir: ")
                excluir = functions.excluir_fornecedor(cnpj)
                if excluir == False:
                    continue
                break

        elif opc_exclus == 5:
            styles.titulo("Excluir peça")
            while True:
                codigo = input("Insira o código da peça que deseja excluir: ")
                excluir = functions.excluir_peca(codigo)
                if excluir == False:
                    continue
                break

        elif opc_exclus == 6:
            styles.titulo("Excluir conta")
            while True:
                nome = input("Insira o nome da conta que deseja excluir: ")
                data = input("Insira a data da conta que deseja excluir: ")
                valor = input("Insira o valor da conta que deseja excluir: ")
                excluir = functions.excluir_conta(nome, data, valor)
                if excluir == False:
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
            