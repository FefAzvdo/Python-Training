import datetime

now = datetime.datetime.now()
ano_atual = now.year

lista_maiores = []
lista_menores = []

for c in range(0, 7):
    ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = ano_atual - ano_de_nascimento
    print("Idade: ", idade)
    if(idade >= 21):
        lista_maiores.append(idade)
    else:
        lista_menores.append(idade)

print("Total de pessoas maiores: ", len(lista_maiores))
print("Total de pessoas menores: ", len(lista_menores))
