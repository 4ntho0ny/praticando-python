from cliente import Cliente
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
    opc = int(input("1-Cadastrar\n->"))

    if opc == 1:
        opc_cad = int(input("Cadastrar\n1-cliente\n2-veículo\n3-serviço\n4-Fornecedor\n5-conta\n0-Sair\n->"))

        if opc_cad == 1:
            cadastro = True

            while cadastro:
                nome = input("Nome: ")
                if not Cliente().validar_nome(nome):
                    print("O campo nome não pode ser vazio!")
                    continue
                cpf = input("CPF: ")
                if not Cliente().validar_cpf(cpf):
                    print("CPF inválido!")
                    continue
                data_nascimento = input("Data de nascimento: ")
                if not Cliente().validar_data(data_nascimento):
                    print("data de nascimento inválida!")
                    continue
                cliente = Cliente(nome, cpf, data_nascimento)
                clientes.append(cliente)

        # elif opc_cad == 2:
        #     cadastro = True
        #     cad_veiculo = veiculo.Veiculo()

        #     while cadastro:
        #         modelo = input("Modelo: ")
        #         if not cad_veiculo.is_none(modelo):
        #             print("O campo modelo não pode ser vazio!")
        #             continue
        #         marca = input("Marca: ")
        #         if not cad_veiculo.is_none(marca):
        #             print("O campo marca não pode ser vazio!")
        #             continue
        #         placa = input("Placa do veículo: ")
        #         if not cad_veiculo.validar_placa(placa):
        #             print("Placa do veículo inválida!")
        #             continue
        #         ano = input("Ano: ")
        #         if not cad_veiculo.is_none(ano):
        #             print("O campo ano não pode ser vazio!")
        #             continue
        #         cor = input("Cor: ")
        #         if not cad_veiculo.is_none(cor):
        #             print("O campo cor não pode ser vazio!")
        #             continue
        #         veiculo = veiculo.Veiculo(modelo, marca, placa, cor, ano)
        #         veiculos.append(veiculo)