# socorram me subi no onibus em marrocos

frase = input("Digite uma frase: ")
formatada = frase.replace(" ", "")

print("Frase =>", formatada)
print("Ao contrário =>", formatada[::-1])

if formatada == formatada[::-1]:
    print("É PALÍNDROMO")
else:
    print("NÃO É PALÍNDROMO")
