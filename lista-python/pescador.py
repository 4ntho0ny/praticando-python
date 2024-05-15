wheight = int(input("Wheight of fishes: "))
peso_excedido = wheight - 50 
if peso_excedido > 0:
    print(
f'''
Peso dos peixes: {wheight}
Peso excedido: {peso_excedido}
Multa: {peso_excedido * 4}
'''
    )