# ex033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('\033[1;30mEste programa irá ler \033[1;35mtrês números \033[1;30me indicar qual é o \033[1;32mmaior '
      '\033[1;30me o \033[1;31mmenor.\033[m')

n1_ = input('\033[0;30mDigite o primeiro número: \033[m').strip()
n2_ = input('\033[0;30mDigite o segundo número: \033[m').strip()
n3_ = input('\033[0;30mAgora, digite o terceiro número: \033[m').strip()

n1 = float(n1_)
n2 = float(n2_)
n3 = float(n3_)

maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3

print(f'\033[0;30mO \033[1;32mmaior \033[0;30mnúmero é \033[1;32m{maior}\033[0;30m, e o \033[1;31mmenor '
      f'\033[0;30mnúmero é \033[1;31m{menor}\033[0;30m.\033[m')
