# ex009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada

n1 = input('\033[1;30mDigite um número inteiro qualquer e este programa lhe mostrará a sua tabuada: \033[m').strip()

n = int(n1)

# Deve haver uma maneira mais simples do que eu fiz abaixo. Procure como(me refiro ao comando "print" ter sido escrito
# 10 vezes!

print('\033[1;36m-=-=-=\033[m' * 2)

print(f'\033[0;30m{n} \033[1;31mx \033[0;30m01 = \033[1;34m{n * 1:2}') # O :2 serve para alinhar as únidades.
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m02 = \033[1;34m{n * 2:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m03 = \033[1;34m{n * 3:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m04 = \033[1;34m{n * 4:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m05 = \033[1;34m{n * 5:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m06 = \033[1;34m{n * 6:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m07 = \033[1;34m{n * 7:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m08 = \033[1;34m{n * 8:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m09 = \033[1;34m{n * 9:2}')
print(f'\033[0;30m{n} \033[1;31mx \033[0;30m10 = \033[1;34m{n * 10:2}')

print('\033[1;36m-=-=-=\033[m' * 2)
