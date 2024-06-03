senha_validada = False

while senha_validada == False:
    user = input("User: ")
    senha = input("Password: ")

    if senha == user:
        print("A senha não pode ser igual ao nome do usuário")
        continue

    if len(senha) < 8:
        print("A senha precisa ter no mínimo 8 caracteres")
        continue
    
    senha_validada = True