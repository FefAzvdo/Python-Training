lista_pesos = []
for c in range(0, 5):
    peso = float(input("Digite o seu peso (kg): "))
    lista_pesos.append(peso)

print("Peso máximo =>", max(lista_pesos))
print("Peso mínimo =>", min(lista_pesos))
