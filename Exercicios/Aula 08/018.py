import random

a1 = input("Digite o 1º aluno: ")
a2 = input("Digite o 2º aluno: ")
a3 = input("Digite o 3º aluno: ")
a4 = input("Digite o 4º aluno: ")
a5 = input("Digite o 5º aluno: ")

alunos = [a1, a2, a3, a4, a5]

random.shuffle(alunos)
print("====================================")
print(f"1º sorteado: {alunos[0]}")
print(f"2º sorteado: {alunos[1]}")
print(f"3º sorteado: {alunos[2]}")
print(f"4º sorteado: {alunos[3]}")
print(f"5º sorteado: {alunos[4]}")
