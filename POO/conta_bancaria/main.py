from conta import Conta

running = True
conta = None

while running:
    opc = None
    print("================<<Sua conta>>================\n")

    opc = int(input("1-Cadastro\n2-Saldo\n3-Saque\n4-Depósito\n-> "))

    if opc == 1:
        nome = saldo = cpf = senha = 0
        while True:
            validar_nome = input("Nome: ").strip().upper()

            if validar_nome == "":
                print("Digite seu nome")
                continue
            elif not validar_nome.isalpha():
                print("Nome inválido")
                continue
            nome = validar_nome
            break
        
        while True:
            validar_senha = input("Senha: ")

            if validar_senha == "":
                print("Digite sua senha")
                continue
            senha = validar_senha
            break

        while True:
            validar_cpf = input("CPF: ")
            
            if validar_cpf == "":
                print("Digite seu cpf")
                continue
            elif len(validar_cpf) > 11 or len(validar_cpf) < 11:
                print("Digite apenas 11 números")
                continue
            elif validar_cpf.isnumeric():
                cpf = validar_cpf
                break

        while True:
            try:
                saldo = float(input("Saldo: "))
                break
            except ValueError:
                print("Valor digitado inválido!")
                continue
        
        conta = Conta(nome, saldo, cpf, senha)

    if opc == 2:
        count = 3
        saldo = 0
        while count > 0:
            senha = input("Digite sua senha: ")
            saldo = conta.extrato(senha)
            if saldo == None:
                count -= 1
                print(f'Você tem {count} tentativas')
                continue
            print(saldo)
            break
        
    if opc == 3:
        count = 3
        saldo = 0
        while count > 0:
            senha = input("Senha: ")
            try:
                valor = float(input("Valor: "))
            except ValueError:
                print("Valor inválido")
                continue
            saque = conta.sacar(senha, valor)
            if saque == None:
                count -= 1
                print(f'Você tem {count} tentativas')
                continue
            if saque == -1:
                continue
            print(saque)
            break

    if opc == 4:
        while True:
            try:
                valor = float(input("Valor: "))
            except ValueError:
                print("Valor inválido")
                continue
            conta.depositar(valor)
            break