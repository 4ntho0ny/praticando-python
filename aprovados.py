soma_nota = 0
media = 0

for i in range(0, 2):
    soma_nota += float(input("Nota: "))

media = soma_nota / 2

if media < 10 and media >= 7:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")