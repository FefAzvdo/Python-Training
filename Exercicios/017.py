import random

a1 = input("Digite o 1º aluno: ")
a2 = input("Digite o 2º aluno: ")
a3 = input("Digite o 3º aluno: ")
a4 = input("Digite o 4º aluno: ")
a5 = input("Digite o 5º aluno: ")

alunos = [a1, a2, a3, a4, a5]

# escolhido = alunos[random.randint(0, 4)]
escolhido = random.choice(alunos)

print(f"O aluno selecionado foi {escolhido}")
