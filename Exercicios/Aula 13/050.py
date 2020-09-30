num = int(input("Digite um número: "))
count = 0

for c in range(num, 0, -1):
    if(num % c == 0):
        print("Divisível por: ", c)
        count = count + 1

if(count > 2):
    print("NÃO É PRIMO")
else:
    print("É PRIMO")
