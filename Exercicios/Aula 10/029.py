distancia = int(input("Qual a distância da viagem ? "))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f"Você vai pagar R$ {preco} para viajar")
