# Ano bissexto

# Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

# Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

# Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 != 0:
        print("É bissexto")
else:
    if ano % 400 != 0:
        print("Não é bissexto")
