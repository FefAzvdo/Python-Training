preco = float(input("Digite o preço do produto: "))
print("""
      [1] - Dinheiro/cheque - 10% desconto

      [2] - A vista no cartão - 5% desconto

      [3] - Em até 2x no cartão - preço normal

      [4] - 3x ou mais no cartão - 20% de juros

      """)
condicao = int(input("Digite a condição de pagamento: "))

if condicao == 1:
    preco_final = preco * 0.9
elif condicao == 2:
    preco_final = preco * 0.95
elif condicao == 3:
    preco_final = preco
elif condicao == 4:
    preco_final = preco * 1.2
else:
    print("Digite um valor válido para condição !")

print("O preço a ser pago é: R$ {:.2f}".format(preco_final))
