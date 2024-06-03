num = int(input("Digite um número: "))
conta_menos_um = 0

while num > 0:
    num -= 1
    conta_menos_um += 1

print(f'O número digitado foi subtraído por \"-1\" {conta_menos_um} vezes')