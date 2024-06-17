def adc(v1, v2):
    return v1 + v2
def sub(v1, v2):
    return v1 - v2
def mult(v1, v2):
    return v1 * v2
def div(v1, v2):
    return v1 / v2

v1 = float(input("Valor 1: "))
opr = input("Operação (+, -, x, /): ")
v2 = float(input("Valor 2: "))

if opr == "+":
    print(adc(v1, v2))
elif opr == "-":
    print(sub(v1, v2))
elif opr == "x":
    print(mult(v1, v2))
elif opr == "/":
    print(div(v1, v2))