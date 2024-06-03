# def olaUser(firstname, lastname = "edasd"):
#     print(f'Olá {firstname} {lastname}')

# olaUser(firstname = input("Username: "), lastname= "Chendrik")

# --------------------------------------------------------------------------------------------------------------

# def calcular_pagamento(qtd_horas, valor_hora):
#     horas = int(qtd_horas)
#     valor = int(valor_hora)
#     salario = 0
#     if horas <= 40:
#         salario = horas * valor
#     else:
#         salario = 40 * valor + (horas - 40 * (1.5 * valor))
#     print(salario)

# calcular_pagamento(int(input("Horas trabalhas: "), int(input("Valor/hora: "))))

# --------------------------------------------------------------------------------------------------------------

def par(x):
    return True if x % 2 == 0 else False

for x in range(1, 10):
    print(par(x))