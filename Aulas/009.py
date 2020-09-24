# Manipulação de strings

frase = "Curso em Vídeo Python"

# Fatiamento

# Posição 0 e posição 9
print(frase[0], frase[9])

# Fatia da posição 9 até a posição 13
print(frase[9:14])

# Fatia da posição 15 até a posição 20
print(frase[15:21])

# Fatia da posição 0 até a posição 20 pulando de 2 em 2
print(frase[0:21:2])

# Fatia do começo até a posição 4
print(frase[:5])

# Fatia do 15 até o final
print(frase[15:])

# Fatia do 9 até o final pulando de 3 em 3
print(frase[9::3])

print("============================================")
print("============================================")

# Número de caractéres
print("len(frase) => ", len(frase))

# Número de ocorrências letra 'o' (Case sensitive)
print("frase.count('o') =>", frase.count('o'))

# Posição primeira ocorrência
print("frase.find('deo') =>", frase.find('deo'))

# Retorna True se existir a palavra na frase
print('Curso' in frase)

# Substitui um trexo da frase por outro trexo
print("frase.replace('Python', 'Android') =>",
      frase.replace('Python', 'Android'))

# Retorna a frase toda em maiúsculo
print("frase.upper() =>", frase.upper())

# Retorna a frase toda em minúsculo
print("frase.lower() =>", frase.lower())

# Apenas a primeira letra da str fica em maiúscula, o resto todo em minúscula
print("frase.capitalize() =>", frase.capitalize())

# Cada palavra da string fica em maiúscula
print("frase.title() =>", frase.title())

frase = "   Aprenda Python  "

# Remove espaços desnecessários no começo e no final da str
print("frase.strip() =>", frase.strip())

# Remove espaços desnecessários no final da str
print("frase.rstrip() =>", frase.rstrip())

# Remove espaços desnecessários no começo da str
print("frase.lstrip() =>", frase.lstrip())

frase = "Curso em Vídeo Phython"

# Retorna uma lista com cada palavra da frase em uma posição dessa lista
print("frase.split() =>", frase.split())

stringSplitada = frase.split()

# Une as frases da lista colocando um - para juntalas
print("'-'.join(stringSplitada) =>", "-".join(stringSplitada))

# Aspas duplas triplas no print, permitem um print com quebra de linha
print("""aaaaaaaaaaaaaa aaaaaaaaaaaaaa aa aa aaaaaaaaaaa aa aa aaaaaaaaaaaaaaaaaaa aaaaaaaaa aa a 
aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaaa aa aa aaaaaaaaaaa aa aa aaaaaaaaaaaaaaaaaaa aaaaaaaaa aa a 
aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaaa aa aa aaaaaaaaaaa aa aa aaaaaaaaaaaaaaaaaaa aaaaaaaaa aa a 
aaaaaaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaaaa aa aa aaaaaaaaaaa aa aa aaaaaaaaaaaaaaaaaaa aaaaaaaaa aa a 
aaaaaaaaaaaaaaaaa""")

frase = 'trqghuklethmpk çmlhyejkuli uyéhg gtvoliqwacvdbno'
print(frase[2::3].upper())
