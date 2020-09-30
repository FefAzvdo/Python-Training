from random import randint

aleatorio = randint(0, 5)

escolhido = int(input("Qual número vc acha que é ? "))

if aleatorio == escolhido:
    print("Boa, acertou !")
else:
    print(f"Errou ! O número era: {aleatorio}")
