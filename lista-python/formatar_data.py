import datetime

meses = {
    1:"Janeiro",
    2:"Fevereiro",
    3:"Março",
    4:"Abril",
    5:"Maio",
    6:"Junho",
    7:"Julho",
    8:"Agosto",
    9:"Setembro",
    10:"Outubro",
    11:"Novembro",
    12:"Dezembro",
}

def validar_data(dia, mes, ano):
    if dia > 31 or dia < 1:
        return False
    elif mes > 12 or mes < 1:
        return False
    elif ano > datetime.datetime.now().year:
        return False
    
def ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            return False
        return True

def verificar_mes(mes):
    nums_meses = meses.keys()

    for num in nums_meses:
        if mes == num:
            return mes[num]

def verificar_dia(dia, mes, ano):
    if mes == meses[4] or mes == meses[6] or mes == meses[9] or mes == meses[11] and dia == 31:
        return False

    if ano_bissexto(ano):
        if mes == meses[2] and dia > 29:
            return False
        return True

    if mes == meses[2] and dia > 28:
        return False

    return True

    

def formatar_data(data):
    data_separada = data.split("/")
    dia = int(data_separada[0])
    mes = int(data_separada[1])
    ano = int(data_separada[2])

    if validar_data(dia, mes, ano):
        return "Data inválida"
    
    mes = verificar_mes(mes)

    if not verificar_dia(dia, mes):
        return "Dia inválido"

    return f'{dia} de {mes} de {ano}'

print(formatar_data(input("Data - dd/mm/yyyy: ")))