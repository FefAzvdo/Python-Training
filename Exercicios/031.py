n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2:
    if n1 > n3:
        print(f"{n1} é o maior")
else:
    if n2 > n3:
        print(f"{n2} é o maior")
    else:
        print(f"{n3} é o maior")
