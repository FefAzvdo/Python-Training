# Trabalhando com cores no terminal

# Style
# 0 - None
# 1 - Bold
# 4 - Underline
# 7 - Negative

# Text
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul escuro
# 35 - Roxo
# 36 - Azul Claro
# 37 - Cinza

# Background
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul escuro
# 45 - Roxo
# 46 - Azul Claro
# 47 - Cinza


def colorize(style=0, text=99, background=99, message=''):
    print(f"\033[{style};{text};{background}m{message}\033[m")


msg = "Essa é a mensagem colorida"
colorize(1, 99, 99, msg)


# def f(a, b, *args):
#     arguments = (a, b) + args
#     print(arguments)


# f(1, 2, 3, 4, 5)
