list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_par = []
lista_impar = []

print(list[1:10])
print(list[8:11])
for num in list:
    if num % 2 == 0:
        lista_par.append(num)
    elif num % 2 != 0:
        lista_impar.append(num)

print(f"Pares -> {lista_par}")
print(f"Ímpares -> {lista_impar}")
list.reverse()
print(list)
