peso = float(input("Qual é o seu peso (kg)?"))
altura = float(input("Qual é sua altura (m)?"))

imc = peso/pow(altura, 2)

print("imc => {:.2f}".format(imc))

# if imc < 18.5:
#     print("Abaixo do peso")
# elif imc >= 18.5 and imc < 25:
#     print("Peso ideal")
# elif imc >= 25 and imc < 30:
#     print("Sobrepeso")
# elif imc >= 30 and imc < 40:
#     print("Obesidade")
# else:
#     print("Obesidade Mórbida")


# Outra forma de escrever:

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")
