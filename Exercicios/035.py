num = int(input("Digite um número :"))
print("""    
        [1] - Binário
        [2] - Hexadecimal
        [3] - Octal                
      """)
base = int(input("Digite a base de conversão: "))

if base == 1:
    print("O número convertido em binário é: {}".format(bin(num)))
elif base == 2:
    print("O número convertido em hexadecimal é: {}".format(hex(num)))
elif base == 3:
    print("O número convertido em Octal é: {}".format(oct(num)))
else:
    print("Digite um número válido da próxima vez")
