while True:    
    try:
        prod1 = float(input("Preço do produto: "))
        prod2 = float(input("Preço do produto: "))
        prod3 = float(input("Preço do produto: "))

        if prod1 < prod2 and prod1 < prod3:
            print("Comprar prod1")
        elif prod2 < prod1 and prod2 < prod3:
            print("Comprar prod2")
        elif prod3 < prod1 and prod3 < prod2:
            print("Comprar prod3")
        elif prod1 == prod2 and prod1 < prod3:
            print("prod1 igual a prod2")
            print("Mais baratos prod3")
        elif prod1 == prod3 and prod1 < prod2:
            print("prod1 igual a prod3")
            print("Mais baratos prod2")
        elif prod2 == prod3 and prod2 < prod1:
            print("prod2 igual a prod3")
            print("Mais baratos prod1")
        break
    except ValueError:
        print("Os inputs só aceitam valores inteiros")
        continue