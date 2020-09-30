num = input("Digite um número entra 0 e 9999: ")

formatedNum = num.zfill(4)

print("Unidade :", formatedNum[3])
print("Dezena :", formatedNum[2])
print("Centena :", formatedNum[1])
print("Milhar :", formatedNum[0])
