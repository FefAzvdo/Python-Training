nome = input("Qual é o seu nome ?")

if nome == 'Fernando':
    print("Que nome bonito!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print("Seu nome é bem popular no Brasil")
elif nome == "Asdrubonildo":
    print("Nossa, que nome horroroso")
elif nome in 'Ana Cláudia Jéssica Juliana':
    print("Que belo nome feminino")
else:
    print("Seu nome é bem normal")

print(f"Tenha um bom dia {nome}")
