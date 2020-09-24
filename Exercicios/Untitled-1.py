red = '\033[1;91m'
green = '\033[1;92m'
yellow = '\033[1;93m'
blue = '\033[1;94m'
magenta = '\033[1;95m'
cyan = '\033[1;96m'
fim = '\033[m'

print(f'Há 4 tipos de pagamento, cada um com diferentes perks:\n'
      f'À vista, \033[1;32mdinheiro\033[m ou \033[1;32mcheque\033[m: \033[4;36m10% de desconto\033[m\n'
      f'À vista, no \033[1;32mcartão\033[m: \033[4;36m5% de desconto\033[m\n'
      f'Parcelado em 2x, no \033[1;32mcartão\033[m: \033[4;34mPreço normal\033[m\n'
      f'Parcelado em 3x, no \033[1;32mcartão\033[m: \033[4;31m20% de juros\033[m.\n'
      f'\n'
      f'Para escolher cada tipo de pagamento escreva:\n{magenta}1{fim} para {yellow}dinheiro{fim} ou {yellow}cheque{fim} para {cyan}10% de desconto{fim},\n'
      f'{magenta}2{fim} para {yellow}débito em cartão{fim} para {cyan}5% de desconto{fim},\n{magenta}3{fim} para {yellow}parcelar em 2x{fim} para {blue}preço normal{fim},\n'
      f'{magenta}4{fim} para {yellow}parcelar em 3x ou mais{fim} para {red}20% de taxa por mês{fim}\n')
preço = float(input('Digite o preço do produto a ser comprado: '))
cond = int(input('Digite a condição de pagamento: '))
if cond == 1 and preço >= 0:
    preço1 = preço * (1 - .1)
    print(f'O valor do produto era R${preço:.2f}, teve um desconto de 10% pela condição de pagamento\n'
          f'e o novo valor a ser pago será de R${preço1:.2f}')
elif cond == 2 and preço >= 0:
    preço1 = preço * (1 - .05)
    print(f'O valor do produto era R${preço:2f}, teve um desconto de 5% pela condição de pagamento\n'
          f'e o novo valor a ser pago será de R${preço1:.2f}')
elif cond == 3 and preço >= 0:
    preço1 = preço
    print(f'O valor do produto era R${preço:.2f}, não teve um desconto pela condição de pagamento\n'
          f'e o valor a ser pago por mês será:\n'
          f'1 parcela: R${yellow}{preço1/2}{fim}\n'
          f'2 parcela: R${yellow}{preço1/2}{fim}')
elif cond == 4 and preço >= 0:
    print('\nVocê escolheu parcelado em 3 ou mais')
    mensal = int(input('Quantos meses deseja parcelar? '))
    if 3 <= mensal <= 12:
        print(f'{mensal}')
        if mensal == 3:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de:\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n')
        elif mensal == 4:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n')
        elif mensal == 5:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}')
        elif mensal == 6:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            preço6 = preço5 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}\n'
                  f'6 parcela: R${preço6:.2f}\n')
        elif mensal == 7:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            preço6 = preço5 * 1.2
            preço7 = preço6 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}\n'
                  f'6 parcela: R${preço6:.2f}\n'
                  f'7 parcela: R${preço7:.2f}')
        elif mensal == 8:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            preço6 = preço5 * 1.2
            preço7 = preço6 * 1.2
            preço8 = preço7 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}\n'
                  f'6 parcela: R${preço6:.2f}\n'
                  f'7 parcela: R${preço7:.2f}\n'
                  f'8 parcela: R${preço8:.2f}\n')
        elif mensal == 9:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            preço6 = preço5 * 1.2
            preço7 = preço6 * 1.2
            preço8 = preço7 * 1.2
            preço9 = preço8 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}\n'
                  f'6 parcela: R${preço6:.2f}\n'
                  f'7 parcela: R${preço7:.2f}\n'
                  f'8 parcela: R${preço8:.2f}\n'
                  f'9 parcela: R${preço9:.2f}')
        elif mensal == 10:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            preço6 = preço5 * 1.2
            preço7 = preço6 * 1.2
            preço8 = preço7 * 1.2
            preço9 = preço8 * 1.2
            preço10 = preço9 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}\n'
                  f'6 parcela: R${preço6:.2f}\n'
                  f'7 parcela: R${preço7:.2f}\n'
                  f'8 parcela: R${preço8:.2f}\n'
                  f'9 parcela: R${preço9:.2f}\n'
                  f'10 parcela: R${preço10:.2f}')
        elif mensal == 11:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            preço6 = preço5 * 1.2
            preço7 = preço6 * 1.2
            preço8 = preço7 * 1.2
            preço9 = preço8 * 1.2
            preço10 = preço9 * 1.2
            preço11 = preço10 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}\n'
                  f'6 parcela: R${preço6:.2f}\n'
                  f'7 parcela: R${preço7:.2f}\n'
                  f'8 parcela: R${preço8:.2f}\n'
                  f'9 parcela: R${preço9:.2f}\n'
                  f'10 parcela: R${preço10:.2f}\n'
                  f'11 parcela: R${preço11:.2f}')
        elif mensal == 12:
            preço1 = preço * 1.2 / mensal
            preço2 = preço1 * 1.2
            preço3 = preço2 * 1.2
            preço4 = preço3 * 1.2
            preço5 = preço4 * 1.2
            preço6 = preço5 * 1.2
            preço7 = preço6 * 1.2
            preço8 = preço7 * 1.2
            preço9 = preço8 * 1.2
            preço10 = preço9 * 1.2
            preço11 = preço10 * 1.2
            preço12 = preço11 * 1.2
            print(f'O valor do produto era {yellow}R${preço:.2f}{fim}, teve um {red}juros de 20%{fim} pela condição de pagamento\n'
                  f'e o novo valor a ser pago por parcela será de\n'
                  f'1 parcela: R${preço1:.2f}\n'
                  f'2 parcela: R${preço2:.2f}\n'
                  f'3 parcela: R${preço3:.2f}\n'
                  f'4 parcela: R${preço4:.2f}\n'
                  f'5 parcela: R${preço5:.2f}\n'
                  f'6 parcela: R${preço6:.2f}\n'
                  f'7 parcela: R${preço7:.2f}\n'
                  f'8 parcela: R${preço8:.2f}\n'
                  f'9 parcela: R${preço9:.2f}\n'
                  f'10 parcela: R${preço10:.2f}\n'
                  f'11 parcela: R${preço11:.2f}\n'
                  f'12 parcela: R${preço12:.2f}')
        else:
            print('Quantidade de meses inválida')
    else:
        print('Quantidade de meses inválida')
else:
    print('N sei')
