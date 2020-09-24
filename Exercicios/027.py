velocidade = int(input("Qual a velocidade do carro ? "))

if velocidade > 80:
    print(
        f"Multado ! Você excedeu o limite permitido em: {velocidade - 80} kms")
    multa = (velocidade - 80) * 7
    print(f"Você vai pagar {multa} reais")
else:
    print("Velocidade permitida !")
