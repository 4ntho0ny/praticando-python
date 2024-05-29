opc = 0

while opc != -1:
    opc = int(input("1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n->"))
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite um número: "))

    if opc == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    if opc == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    if opc == 3:
        print(f'{n1} x {n2} = {n1 * n2}')
    if opc == 4:
        print(f'{n1} / {n2} = {n1 / n2}')