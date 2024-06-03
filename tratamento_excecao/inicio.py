while True:
    try:
        var = int(input("Digite uma palavra: "))
        print(var)
        break
    except ValueError:
        print("Digite apenas números inteiros")
    except:
        print("Erro desconhecido")
    finally:
        print("Final do algoritmo")