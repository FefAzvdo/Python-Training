import datetime

now = datetime.datetime.now()
ano_atual = now.year

ano_nascimento = int(input("Em que ano você nasceu ? "))

idade = ano_atual - ano_nascimento

if idade < 9:
    print(f"Idade: {idade} MIRIM")
elif idade >= 9 and idade < 14:
    print(f"Idade: {idade} INFANTIL")
elif idade >= 14 and idade < 19:
    print(f"Idade: {idade} JUNIOR")
elif idade >= 19 and idade < 25:
    print(f"Idade: {idade} SÊNIOR")
else:
    print(f"Idade: {idade} MASTER")
