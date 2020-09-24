nome = input("Qual seu nome completo ? ")

print("Maiúsculas : ", nome.upper())
print("Minúsculas :", nome.lower())
print("Letras no nome (sem espaços)", len(nome.replace(' ', '')))
print("Letras no nome (com espaços)", len(nome))
print("Letras do 1º nome: ", len(nome.split()[0]))
