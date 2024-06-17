def contador_digitos(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count

print(contador_digitos(int(input("Number: "))))