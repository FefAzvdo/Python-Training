valorDaCasa = float(input("Qual é o valor da casa ? "))
valorDoSalario = float(input("Qual é o valor do seu salário ? "))
anos = int(input("Em quantos anos você vai pagar ? "))

parcela = valorDaCasa/(anos*12)

print("Valor máximo de parcela R$ ", valorDoSalario * 1.3)

if parcela >= valorDoSalario * 1.3:
    excedido = parcela - (valorDoSalario * 1.3)
    print("Infelizmente você não vai receber o empréstimo :( ")
    print("Sua parcela excedeu o valor máximo em R${:.2f}".format(excedido))
else:
    print(
        "Você vai receber o empréstimo, e vai pagar R$ {:.2f} por mês".format(parcela))
