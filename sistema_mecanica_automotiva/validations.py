from datetime import datetime
import styles

# ======== validações gerais ========

def str_vazia(text):
    if text == "":
        return False
    return True

def validar_data(data):
    try:
        data = datetime.strptime(data, "%d/%m/Y")
    except:
        styles.desenhar_barra()
        print("Data inválida!")
        styles.desenhar_barra()
        return None
    return data


# ======== validações veículo ========
    
def validar_placa(placa):
    if placa == "":
        styles.desenhar_barra()
        print("O campo \"Placa\" não pode ser vazio!")
        styles.desenhar_barra()
        return False
    elif len(placa) == 7:
        if placa[0:3].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5:7].isnumeric():
            return True
    styles.desenhar_barra()
    print("Placa do veículo inválida!")
    styles.desenhar_barra()
    return False

def validar_ano(ano):
    if ano.isnumeric():
        if ano > datetime.now().strftime("%Y"):
            styles.desenhar_barra()
            print("Valor do ano inválido")
            styles.desenhar_barra()
            return False
        return True
    else:
        styles.desenhar_barra()
        print("Digite o ano do veículo")
        styles.desenhar_barra()

# ======== validações serviço ========

def validar_valor():
    try:
        valor = float(input("Valor: "))
        if valor < 0:
            return None
        return valor
    except:
        print("Valor inválido!")
        return None
