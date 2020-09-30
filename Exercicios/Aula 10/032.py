salario = float(input("Quanto você ganha: "))

if salario >= 1250:
    salario = salario * 1.1
else:
    salario = salario * 1.5

print(f"O seu novo salário é {salario}")
