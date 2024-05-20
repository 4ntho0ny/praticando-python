while True:    
    try:
        n1 = int(input("Numero 1:"))
        n2 = int(input("Numero 2:"))
        n3 = int(input("Numero 3:"))

        if n1 > n2 and n1 > n3:
            print("Maior: N1")
            if n2 < n3:
                print("Menor: N2")
            elif n3 < n2:
                print("Menor: N3")
            else:
                print("N2 e N3 são iguais")
        elif n2 > n1 and n2 > n3:
            print("Maior: N2")
            if n1 < n3:
                print("Menor: N1")
            elif n3 < n1:
                print("Menor: N3")
            else:
                print("N1 e N3 são iguais")
        elif n3 > n1 and n3 > n2:
            print("Maior: N3")
            if n1 < n2:
                print("Menor: N1")
            elif n2 < n1:
                print("Menor: N2")
            else:
                print("N1 e N2 são iguais")
        elif n1 == n2 and n1 > n3:
            print("N1 igual a N2")
            print("Menor: N3")
        elif n1 == n3 and n1 > n2:
            print("N1 igual a N3")
            print("Menor: N2")
        elif n2 == n3 and n2 > n1:
            print("N2 igual a N3")
            print("Menor: N1")
        break
    except ValueError:
        print("Os inputs só aceitam valores inteiros")
        continue