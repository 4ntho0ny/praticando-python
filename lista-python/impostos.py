valor_hora = float(input("Valor/h: "))
horas = int(input("Horas trabalhadas: "))
salario_bruto = valor_hora * horas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

print(
f'''
Salario bruto = {salario_bruto}
Valor IR = {desconto_ir}
Valor INSS = {desconto_inss}
Valor sindicato = {desconto_sindicato}
Salário líquido = {salario_bruto - desconto_ir - desconto_inss - desconto_sindicato}
'''
)
