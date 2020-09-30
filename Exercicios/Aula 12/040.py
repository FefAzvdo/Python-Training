# Condição de existência de um triângulo

# Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência:
# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.


# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

a = float(input("Digite o tamanho da primeira medida: "))
b = float(input("Digite o tamanho da segunda medida: "))
c = float(input("Digite o tamanho da terceira medida: "))

isTriangle = abs(b - c) < a < (b + c)

if isTriangle:
    print("Forma um triângulo")
    if a == b and a == c:
        print("Tipo de triângulo: Equilátero")
    elif a == b and a != c:
        print("Tipo de triângulo: Isósceles")
    else:
        print("Tipo de triângulo: Escaleno")
else:
    print("Não forma um triângulo")
