from model import cliente, veiculo, servico, conta, fornecedor, peca

# Banco de dados improvisado
clientes = [cliente.Cliente("Anthony", "12312312312", "13/04/2005")]
veiculos = [veiculo.Veiculo("Civic", "Honda", "ABC-1234", "Prata", 2020)]
fornecedores = [fornecedor.Fornecedor("Fornecedor XYZ", "00.000.000/0001-00")]
contas = [conta.Conta("dssfs", "dsfsdf", "sadfsfs")]
servicos = [servico.Servico("Troca de Oleo", 100.0, "2024-06-20")]
pecas = [peca.Peca("Disco de Freio", "Brembo", 350.0, True, "DF12345")]