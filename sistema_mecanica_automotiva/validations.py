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
        styles.msg_erro("Data inválida!")
        return False
    return True

def validar_valor():
    try:
        valor = float(input("Valor: "))
        if valor < 0:
            styles.msg_erro("O valor não pode ser menor que 0!")
            return None
        return valor
    except:
        styles.msg_erro("Valor inválido!")
        return None

def validar_data_final(referencia_data):
    data = input(f'Data {referencia_data} (dia/mês/ano): ')

    if validar_formato_data(data) == False:
        return None
    data_atual = datetime.now().strftime("%d/%m/%Y")
    data_termino_obj = transformar_datetime_obj(data)
    data_atual_obj = transformar_datetime_obj(data_atual)
    
    if data_termino_obj < data_atual_obj:
        styles.msg_erro("Insira uma data a frente da atual!")
        return None
    return data

def verificar_lista_vazia(lista):
    if lista == []:
        styles.msg_erro("Esta lista está vazia!")
        return False
    return True

# ======== validações cliente ========

def validar_cpf(cpf):
    if cpf.isnumeric():
        if len(cpf) == 11:
            return True
    styles.msg_erro("CPF inválido!")
    return False

def validar_data_nascimento(data):
    if validar_formato_data(data) == False:
        return False
    
    data_atual = datetime.now().strftime("%d/%m/%Y")
    data_nascimento_obj = transformar_datetime_obj(data)
    data_atual_obj = transformar_datetime_obj(data_atual)
    delta_year = data_atual_obj.year - data_nascimento_obj.year
    print(delta_year)
    if data_nascimento_obj > data_atual_obj or delta_year < 18:
        styles.msg_erro("Data de nascimento inválida!")
        return False
        
    return True

# ======== validações veículo ========
    
def validar_placa(placa):
    if placa == "":
        styles.msg_erro("O campo \"Placa\" não pode ser vazio!")
        return False
    elif len(placa) == 7:
        if placa[0:3].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5:7].isnumeric():
            return True
    styles.msg_erro("Placa do veículo inválida!")
    return False

def validar_ano_veiculo(ano):
    if ano.isnumeric():
        if ano > datetime.now().strftime("%Y"):
            styles.msg_erro("Valor do ano inválido!")
            return False
        return True
    else:
        styles.msg_erro("Digite o ano do veículo!")

# ======== validações fonecedor ========

def validar_cnpj(cnpj):
    if cnpj.isnumeric():
        if len(cnpj) == 14:
            return True
    styles.msg_erro("CNPJ inválido!")
    return False