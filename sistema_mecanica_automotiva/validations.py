from datetime import datetime
import styles

# ======== validações gerais ========

def str_vazia(text):
    if text == "":
        return False
    return True

def transformar_datetime_obj(data):
    dia, mes, ano = data.split("/")
    return datetime(int(ano), int(mes), int(dia))

def validar_formato_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        styles.desenhar_barra()
        print("Data inválida!")
        styles.desenhar_barra()
        return False
    return True

def validar_valor():
    try:
        valor = float(input("Valor: "))
        if valor < 0:
            styles.desenhar_barra()
            print("O valor não pode ser menor que 0!")
            styles.desenhar_barra()
            return None
        return valor
    except:
        styles.desenhar_barra()
        print("Valor inválido!")
        styles.desenhar_barra()
        return None

def validar_data_final(referencia_data):
    data = input(f'Data {referencia_data} (dia/mês/ano): ')

    if validar_formato_data(data) == False:
        return None
    data_atual = datetime.now().strftime("%d/%m/%Y")
    data_termino_obj = transformar_datetime_obj(data)
    data_atual_obj = transformar_datetime_obj(data_atual)
    
    if data_termino_obj < data_atual_obj:
        styles.desenhar_barra()
        print("Insira uma data a frente da atual!")
        styles.desenhar_barra()
        return None
    return data

# ======== validações cliente ========

def validar_cpf(cpf):
    if cpf.isnumeric():
        if len(cpf) == 11:
            return True
    styles.desenhar_barra()
    print("CPF inválido!")
    styles.desenhar_barra()
    return False

def validar_data_nascimento(data):
    if validar_formato_data(data) == False:
        return False
    
    data_atual = datetime.now().strftime("%d/%m/%Y")
    data_nascimento_obj = transformar_datetime_obj(data)
    data_atual_obj = transformar_datetime_obj(data_atual)
    
    # delta_dia = data_atual_obj.day - data_nascimento_obj.day
    # delta_mes = data_atual_obj.month - data_nascimento_obj.month
    delta_year = data_atual_obj.year - data_nascimento_obj.year
    print(delta_year)
    if data_nascimento_obj > data_atual_obj or delta_year < 18:
        styles.desenhar_barra()
        print("Data de nascimento inválida!")
        styles.desenhar_barra()
        return False
        
    return True

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

def validar_ano_veiculo(ano):
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

# ======== validações fonecedor ========

def validar_cnpj(cnpj):
    if cnpj.isnumeric():
        if len(cnpj) == 14:
            return True
    styles.desenhar_barra()
    print("CNPJ inválido!")
    styles.desenhar_barra()
    return False

# ======== validações peça ========

