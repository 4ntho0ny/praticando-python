import math

area = float(input("Área(m^2): "))
litros_tintas = area / 3

if litros_tintas <= 18:
    print("Uma lata")
else:
    print(f'{math.ceil(litros_tintas / 18)} latas')