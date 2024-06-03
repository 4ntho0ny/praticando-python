letra = input("Digite uma letra:")
vogais = ['a', 'e', 'i', 'o', 'u']
cont = 0

for vogal in vogais:
    if letra == vogal:
        print("vogal")
    else:
        cont += 1
if cont == len(vogais):
    print("consoante")
