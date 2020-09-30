mulheres_com_menos_de_20 = []
soma_idade = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0

for c in range(0, 4):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo: 'M' ou 'F' : ")

    soma_idade = soma_idade + idade

    if(sexo == 'F'):
        if(idade < 20):
            mulheres_com_menos_de_20.append(nome)
    else:
        if(idade_homem_mais_velho < idade):
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade

print("A média da idade do grupo é: ", soma_idade/4)
print("O nome do homem mais velho é: ", nome_homem_mais_velho)
print(f"Existem {len(mulheres_com_menos_de_20)} mulheres com menos de 20")
