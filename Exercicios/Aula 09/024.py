frase = input("Digite uma frase: ")

frase = frase.upper()

print("A letra 'A' aparece: ", frase.count('A'), 'vezes')
print("A letra 'A' aparece pela primeira vez na posição: ", frase.find('A'))
print("A letra 'A' aparece pela última vez na posição: ", frase.rfind('A'))
