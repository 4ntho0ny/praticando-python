from arma import Arma
from pessoa import Pessoa
from cliente import Cliente
from listas import armas, pessoas, clientes
from os import system

running = True

while running:
    try:
        opc = int(input("1-Cadastrar pessoa\n2-Cadastrar cliente\n3-Cadastrar arma\n4-Relatório pessoas\n5-Relatório armas\n6-Relatório clientes\nQualquer outro número-Sair\n->"))
    except ValueError:
        print("Opção inválida!")
        continue

    if opc == 1:
        system('cls')
        pessoa = Pessoa()
        pessoa.cadastrar_pessoa()
        pessoas.append(pessoa)
    elif opc == 2:
        system('cls')
        cliente = Cliente()
        cliente.cadastrar_cliente()
        clientes.append(cliente)
    elif opc == 3:
        system('cls')
        arma = Arma()
        arma.cadastrar_arma()
        armas.append(arma)
    elif opc == 4:
        if pessoas == []:
            print("Lista de pessoas vazia")
        else:
            for pessoa in pessoas:
                pessoa.relatorio()
    elif opc == 5:
        if armas == []:
            print("Lista de armas vazia")
        else:
            for arma in armas:
                arma.relatorio()
    elif opc == 6:
        if clientes == []:
            print("Lista de clientes vazia")
        else:
            for cliente in clientes:    
                cliente.relatorio()
    else:
        system('cls')
        print("Programa finalizado!")
        break