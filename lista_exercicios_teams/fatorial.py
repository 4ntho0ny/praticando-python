num = int(input("Number: "))
mult = 1
while num > 1:
    mult *= num
    print(f'{num}', end=" x ")
    num -= 1
print(f'1 = {mult}')