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
    
    # Seção de exclusão
    elif opc == 2:
        styles.clear_t()
        styles.titulo("Excluir")
        opc_exclus = None
        try:
            opc_exclus = int(input("\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-peça\n6-conta\nqualquer outro número-Sair da seção de exclusão\n-> "))
        except ValueError:
            styles.msg_erro("Opção indisponível!")

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

    # Seção de alteracao
    elif opc == 3:
        styles.clear_t()
        styles.titulo("Alterar")
        opc_alterar = None
        try:
            opc_alterar = int(input("\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-peça\n6-conta\nqualquer outro número-Sair da seção de exclusão\n-> "))
        except ValueError:
            styles.msg_erro("Opção indisponível!")
        
        if opc_alterar == 1:
            styles.titulo("Alterar Dados do Cliente")
            if not valid.verificar_lista_vazia(clientes):
                continue
            while True:
                c = functions.buscar_cliente_cpf(input("Digite o CPF do cliente: "))
                if c == None:
                    continue
                functions.editar_cliente(c)
                break

        elif opc_alterar == 2:
            styles.titulo("Alterar Dados do Veiculo")
            if not valid.verificar_lista_vazia(veiculos):
                continue
            while True:
                v = functions.buscar_veiculo_placa(input("Digite a placa do veiculo: "))
                if v == None:
                    continue
                functions.editar_veiculo(v)
                break

        elif opc_alterar == 3:
            styles.titulo("Alterar Dados do Servico")
            if not valid.verificar_lista_vazia(servicos):
                continue
            while True:
                s = functions.buscar_servico(input("Digite o nome do servico: "))
                if s == None:
                    continue
                functions.editar_servico()
                break

        elif opc_alterar == 4:
            styles.titulo("Alterar Dados do Fornecedor")
            if not valid.verificar_lista_vazia(fornecedores):
                continue
            while True:
                f = functions.buscar_fornecedor(input("Digite o cnpj do fornecedor: "))
                if f == None:
                    continue
                functions.editar_fornecedor(f)
                break

        elif opc_alterar == 5:
            styles.titulo("Alterar Dados da Peca")
            if not valid.verificar_lista_vazia(pecas):
                continue
            while True:
                p = functions.buscar_peca(input("Digite codigo da peca: "))
                if p == None:
                    continue
                functions.editar_peca(p)
                break

        elif opc_alterar == 6:
            styles.titulo("Alterar Dados da Conta")
            if not valid.verificar_lista_vazia(contas):
                continue
            while True:
                c = functions.buscar_conta(input("Digite o nome da conta: "))
                if c == None:
                    continue
                functions.editar_conta(c)
                break
        print(contas[0].nome)

    # Seção de relatorio
    elif opc == 4:
        styles.clear_t()
        styles.titulo("Gerar Relatorio")
        opc_relat = None
        try:
            opc_relat = int(input("\n1-cliente\n2-veículo\n3-serviço\n4-fornecedor\n5-peça\n6-conta\nqualquer outro número-Sair da seção de exclusão\n-> "))
        except ValueError:
            styles.msg_erro("Opção indisponível!")
        
        if opc_relat == 1:
            styles.titulo("Gerar relatorio do cliente")
            if not valid.verificar_lista_vazia(clientes):
                continue
            while True:
                c = functions.buscar_cliente_cpf(input("Insira o cpf do cliente: "))
                if c == None:
                    continue
                c.relatorio()
                break
        
        elif opc_relat == 2:
            styles.titulo("Gerar relatorio do veiculo")
            if not valid.verificar_lista_vazia(veiculos):
                continue
            while True:
                v = functions.buscar_veiculo_placa(input("Insira a placa do veiculo: "))
                if v == None:
                    continue
                v.relatorio()
                break

        elif opc_relat == 3:
            styles.titulo("Gerar relatorio do servico")
            if not valid.verificar_lista_vazia(servicos):
                continue
            while True:
                s = functions.buscar_servico(input("Nome do servico: "))
                if s == None:
                    continue
                s.relatorio()
                break

        elif opc_relat == 4:
            styles.titulo("Gerar relatorio do fornecedor")
            if not valid.verificar_lista_vazia(fornecedores):
                continue
            while True:
                f = functions.buscar_fornecedor(input("CNPJ do fornecedor: "))
                if f == None:
                    continue
                f.relatorio()
                break

        elif opc_relat == 5:
            styles.titulo("Gerar relatorio da peca")
            if not valid.verificar_lista_vazia(peca):
                continue
            while True:
                p = functions.buscar_peca(input("Informe o codigo da peca: "))
                if p == None:
                    continue
                p.relatorio()
                break

        elif opc_relat == 6:
            styles.titulo("Gerar relatorio da conta")
            if not valid.verificar_lista_vazia(contas):
                continue
            while True:
                c = functions.buscar_conta(input("Informe o nome da conta: "))
                if c == None:
                    continue
                c.relatorio()
                break

        else:
            continue