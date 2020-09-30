from math import sin, cos, tan, radians

angulo = float(input("Digite o valor do ângulo: "))

angulo_em_rad = radians(angulo)

seno = sin(angulo_em_rad)
cosseno = cos(angulo_em_rad)
tangente = tan(angulo_em_rad)

print("Seno: ", seno)
print("Cosseno: ", cosseno)
print("Tangente: ", tangente)
