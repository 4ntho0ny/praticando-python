num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))
soma = 0
if num2 < num1:
    for i in range(num2 + 1, num1):
        soma += i
else:
    for i in range(num1 + 1, num2):
        soma += i
print(soma)