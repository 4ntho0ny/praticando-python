opc = 1

while opc != -1:
    opc = int(input("1-Realizar Compra\n2-Fechar Programa\n->"))

    if opc == 1:
        produto_list = []

        produto = float(input("Produto 1: "))

        produto_list.append(produto)

        i = 2

        while produto != 0:
            produto = float(input(f'Produto {i}: '))

            if produto == 0:
                total = sum(produto_list)
                print(f'Total: R$ {total}')

                pagamento_cliente = float(input("Pagamento: R$ "))

                if pagamento_cliente > total:
                    print(f'Troco: R$ {pagamento_cliente - total}')

                print("Volte sempre!!")
                break

            produto_list.append(produto)

            i += 1
    if opc == 2:
        print("Programa finalizado!")
        break
