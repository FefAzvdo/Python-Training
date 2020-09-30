import math

ca = float(input("Digite a medida do cateto oposto: "))
co = float(input("Digite a medida do cateto adjacente: "))

hip = math.hypot(ca, co)

print(f"A hipotenusa desse triângulo vale: {hip}")
