primeiro_termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razão da P.A: "))

print(primeiro_termo, end=" > ")
for c in range(1, 10):
    primeiro_termo = primeiro_termo + razao
    print(primeiro_termo, end=" > ")
print("ACABOU")
