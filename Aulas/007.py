# Operadores Aritiméticos

#   +        adição
#   -        subtração
#   *        multiplicação
#   /        divisão
#  **        potencia
#  //        divisão inteira
#  %         resto da divisão


# Ordem de precedência

# 1º ()

# 2º **

# 3º * / // %

# 4º + -


print(5+3*2)  # 11
print(3*5+4**2)  # 31
print(3*(5+4)**2)  # 243


nome = input("Qual é o seu nome? ")
print("Prazer em te conhecer {:20}!".format(nome))
print("Prazer em te conhecer {:<20}!".format(nome))

# Não quebrar a linha no final do print()
print("Prazer em te conhecer {:>20}!".format(nome), end=' ')

print("Prazer em te conhecer {:^20}!".format(nome))
print("Prazer em te conhecer {:=^20}!".format(nome))


n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

d = n1 / n2

print("A divisão é: {:.3f'}".format(d))  # Formatação casas decimais float
