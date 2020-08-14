# ex032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
print('\033[1;30mEste programa irá ler um ano digitado pelo usuário e dirá se o ano é ou não, bissexto.')
print('\033[0;35m-=-\033[m' * 25)
a_ = input('\033[0;30mDigite o ano que deseja analisar, coloque \033[1;36m7 '
           '\033[0;30mpara analisar o \033[1;34mano atual\033[0;30m: ').strip()
print('\033[0;35m-=-\033[m' * 25)

a = int(a_)
if a == 7:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'\033[0;30mO ano \033[1;34m{a} \033[1;32mÉ \033[1;30mBISSEXTO.\033[m')
else:
    print(f'\033[0;30mO ano \033[1;34m{a} \033[1;31mNÃO É \033[1;30mBISSEXTO.\033[m')