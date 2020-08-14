#ex023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#      unidade: 4
#      dezena: 3
#      centena: 8
#      milhar: 1

# Não consegui resolver esse exercicio sozinho. Estude mais!

import math
nstr = input('\033[1;30mDigite o valor de um número de 0 a 9999: \033[m').strip()

n = float(nstr)
u = int(n % 10)
d = int(n // 10 % 10)
c = int(n // 100 % 10)
m = int(n // 1000 % 10) #Para compreender melhor a formula acima, execute o codigo por partes.

print(f'\033[0;31mUnidade = \033[1;30m{u}\033[m')
print(f'\033[0;32mDezena = \033[1;30m{d}\033[m')
print(f'\033[0;33mCentena = \033[1;30m{c}\033[m')
print(f'\033[0;34mMilhar = \033[1;30m{m}\033[m')

'''

n = float(nstr)
u = int(n % 10)
d_ = int(n // 10)
d = d_ % 10
c_ = int(n // 100)
c = c_ % 10
m_ = int(n // 1000)
m = m_ % 10

'''
