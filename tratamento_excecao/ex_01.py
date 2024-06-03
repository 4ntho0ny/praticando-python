opc = True

while opc:
    try:
        opc = int(input("1 - Cadastro\n0 - Encerrar\n-> "))

        if opc == 1:
            nome = input("Nome: ")
            rg = input("RG: ")
            idade = int(input("Idade: "))
        elif opc == 0:
            print("Programa encerrado")
            opc = False
        else:
            print("Opção inválida")
    except ValueError:
        print("Valor digitado inválido")
