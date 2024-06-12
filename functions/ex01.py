import datetime

def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    
    return (valor_prestacao + valor_prestacao * 0.03) + (1 / 1000 *  valor_prestacao) * dias_atraso

def imprimirRelatorio(lista_pagamentos, total_pagamentos):
    print(f'------------{datetime.datetime.now().strftime("%d/%m/%y")} - {len(lista_pagamentos)} pagamentos------------')
    for pagamento in lista_pagamentos:
        pagamento = str(pagamento)
        print(f'- R${pagamento.replace(".", ",")}')
    print(f'Total - {total_pagamentos}\n--------------------------------------------------------------------------------------------------')

def somar_pagamentos(lista_pagamentos):
    soma = 0
    for pagamento in lista_pagamentos:
        soma += pagamento
    return soma

running = True
lista_pagamentos = []

while running:
    try:
        valor_prestacao = float(input("Valor da prestação: "))

        if valor_prestacao == 0:
            total_pagamentos = somar_pagamentos(lista_pagamentos)
            imprimirRelatorio(lista_pagamentos, total_pagamentos)
            running = False

        dias_atraso = int(input("Dias em atraso(se nao estiver atrasado, coloque 0): "))
    except ValueError:
        print("Valor inválido")
        continue
    
    if valor_prestacao < 0 or dias_atraso < 0:
        print("Não podem existir valores menores que zero ")
    else:    
        lista_pagamentos.append(valorPagamento(valor_prestacao, dias_atraso))