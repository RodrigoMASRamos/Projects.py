#ex030: Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
n = int(input('\033[1;30mDigite o valor de um \033[1;35mnúmero inteiro \033[1;30me este programa lhe dirá se ele é '
              '\033[1;31mpar \033[1;30mou \033[1;34mimpar: '))
print('\033[0;36m-=-=-\033[0;36m' * 17)
if n % 2 == 0:
    print('\033[0;30mEste é um número \033[0;31mpar!')
else:
    print('\033[0;30mEste é um número \033[0;34mimpar!')