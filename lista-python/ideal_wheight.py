height = int(input("Height(cm): "))
gender = input("Gender(m/f): ")

# Ex 012
# print(f'Wheight: {72.7 * (height / 100) - 58:.2f}kg')

# Ex 013
if(gender == 'f'):
    print(f'Wheight: {62.1 * (height / 100) - 44.7:.2f}kg')
elif(gender == 'm'):
    print(f'Wheight: {72.7 * (height / 100) - 58:.2f}kg')