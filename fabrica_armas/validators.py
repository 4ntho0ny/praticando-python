import datetime

def isEmpty(strng):
    if not strng:
        print("Este campo não pode ser vazio")
        return True
    return False

def validar_formato_data(data):
    return datetime.datetime.strptime(data, "%d/%m/%Y")