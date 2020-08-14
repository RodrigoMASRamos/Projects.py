#ex018: Faça um programa que leia um ângulo qualquer a mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin,cos,tan, radians, trunc

print('\033[1;30mEste programa irá ler um ângulo qualquer e mostrar o valor de seu seno, cosseno e tangente. \033[m')
print('\033[0;35m-=-=-=\033[m' * 14)
astr = input('\033[0;30mDigite o valor do ângulo: \033[m').strip()
a = float(astr)


print('\033[0;35m-=-=-=\033[m' * 14)


# A função "trunc(14:67)" abaixo, revela somente a parte inteira de um número.

print(f'\033[0;30mO \033[0;35mSENO \033[0;30mdo ângulo \033[1;36m{trunc(a)}° \033[0;30mé igual a '
      f'\033[1;35m{sin(radians(a)):.2f}\033[0;30m.')

print(f'\033[0;30mO \033[0;35mCOSSENO \033[0;30mdo ângulo \033[1;36m{trunc(a)}° \033[0;30mé igual a '
      f'\033[1;35m{cos(radians(a)):.2f}\033[0;30m.')

print(f'\033[0;30mA \033[0;35mTANGENTE \033[0;30mdo ângulo \033[1;36m{trunc(a)}° \033[0;30mé igual a '
      f'\033[1;35m{tan(radians(a)):.2f}\033[0;30m.')

print('\033[0;35m-=-=-=\033[m' * 14)

