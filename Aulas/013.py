# Estruturas de Repetição


# Output: 1, 2, 3, 4, 5
for count in range(1, 6):
    print(count)

# Executa 3x
# Output: * * *
for count in range(0, 3):
    print("*")

for count in range(0, 11):
    if(count % 2 == 0):
        print(f"{count} é PAR")
    else:
        print(f"{count} é ÍMPAR")

for count in range(6, 0, -1):
    print(count)

n = int(input("Digite um número: "))
for count in range(0, n+1):
    print(count)
