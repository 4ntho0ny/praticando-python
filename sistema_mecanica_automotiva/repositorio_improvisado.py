from model import cliente, veiculo, servico, conta, fornecedor, peca

# Banco de dados improvisado
clientes = []
veiculos = [veiculo.Veiculo("Civic", "Honda", "ABC-1234", "Prata", 2020)]
fornecedores = [fornecedor.Fornecedor("Fornecedor XYZ", "00.000.000/0001-00")]
contas = [conta.Conta("Conta de Luz", 150.0, "2024-06-30")]
servicos = [servico.Servico("Troca de Óleo", 100.0, "2024-06-20")]
pecas = [peca.Peca("Disco de Freio", "Brembo", 350.0, True, "DF12345")]