while True:
    opc = int(input("Digite o valor 1 ou 0 para encerrar: "))

    if opc == 1:
        print("Valor correto")
    elif opc == 0:
        print("Encerrar programa")
        break
    else:
        print("Valor inválido")
