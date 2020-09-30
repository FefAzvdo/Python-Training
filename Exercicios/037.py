import datetime

now = datetime.datetime.now()
ano_atual = now.year

ano_nascimento = int(input("Em que ano você nasceu ? "))

idade = ano_atual - ano_nascimento

if idade < 18:
    quantos_anos_faltam = 18 - idade
    print(
        f"Você ainda não pode se alistar, ainda faltam {quantos_anos_faltam} anos")
elif idade == 18:
    print("Esse é o ano do seu alistamento")
else:
    print("Já passou seu tempo de alistamento")
