import math

area = float(input("Área(m^2): "))
litros_tintas = area / 6 

if litros_tintas <= 3.6:
    print("Um galão -> 25.00")
else:
    total_galoes = math.ceil(litros_tintas / 3.6)
    print(f'{total_galoes} galões -> {total_galoes * 25:.2f}')

if litros_tintas <= 18:
    print("Uma lata -> 80.00")
else:
    total_latas = math.ceil(litros_tintas / 18)
    print(f'{total_latas} latas -> {total_latas * 80:.2f}')

    qnt_galoes = 0
    sobra_tinta = 0
    qnt_latas = 0

    qnt_latas = math.ceil(litros_tintas / 18)
    sobra_tinta = math.ceil(litros_tintas % 18)
    qnt_galoes = math.ceil(sobra_tinta / 3.6)

    print(
f'''
Menor Custo

{qnt_galoes} galões -> {qnt_galoes * 25:.2f}
{qnt_latas} latas -> {qnt_galoes * 80:.2f}
'''
    )

