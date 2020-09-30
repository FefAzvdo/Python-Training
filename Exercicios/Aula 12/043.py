import random

escolha = int(input("""
JO KEN PÔ !!
      [0] - PEDRA
      [1] - PAPEL
      [2] - TESOURA

      ESCOLHA: """))

opcoes = ["PEDRA :", "PAPEL", "TESOURA"]

escolhido_pelo_pc = opcoes[random.randint(0, 2)]
escolhido_por_vc = opcoes[escolha]

print("O PC escolheu:", escolhido_pelo_pc)
print("VOCÊ escolheu:", escolhido_por_vc)


if escolhido_por_vc == "PEDRA" and escolhido_pelo_pc == "PEDRA":
    print("EMPATE !")
elif escolhido_por_vc == "PEDRA" and escolhido_pelo_pc == "PAPEL":
    print("PERDEU !")
elif escolhido_por_vc == "PEDRA" and escolhido_pelo_pc == "TESOURA":
    print("GANHOU")
elif escolhido_por_vc == "PAPEL" and escolhido_pelo_pc == "PEDRA":
    print("GANHOU !")
elif escolhido_por_vc == "PAPEL" and escolhido_pelo_pc == "PAPEL":
    print("EMPATE !")
elif escolhido_por_vc == "PAPEL" and escolhido_pelo_pc == "TESOURA":
    print("PERDEU")
elif escolhido_por_vc == "TESOURA" and escolhido_pelo_pc == "PEDRA":
    print("PERDEU !")
elif escolhido_por_vc == "TESOURA" and escolhido_pelo_pc == "PAPEL":
    print("GANHOU !")
elif escolhido_por_vc == "TESOURA" and escolhido_pelo_pc == "TESOURA":
    print("EMPATE")
