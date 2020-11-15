# Exercício Python #052 - Números primos
#
# Faça um pograma que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.
#
# Obs: eu NÃO consegui fazer esse exercício SEM ver a RESOLUÇÃO e de forma mais simples. Estude mais!!!

total = 0
n = input('\033[0;30mDigite um número \033[1;32mINTEIRO\033[0;30m. Este programa lhe indicará se ele é ou não, '
          'um \033[1;31mnúmero PRIMO: \033[m').strip()
n = int(str(n))

print('                                                                                    ')

print('\033[0;30mUm número \033[1;33mprimo \033[0;30mé divisivel somente \033[1;34mduas vezes. '
      '\033[0;30mOs números \033[1;34mAZUIS \033[0;30mindicam uma possivel divisão inteira,\nenquanto os '
      '\033[1;31mVERMELHOS \033[0;30mindicam o contrário.\033[m')

for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[1;34m{c}\033[m',end=' ') # O end serve para a linha prosseguir de forma horizontal, até o
        total += 1                            # surgimento do "\n", que aparece pela primeira vez na linha 29.
    else:
        print(f'\033[0;31m{c}\033[m',end=' ') # O sistema de cores do padrão ANSI vai colorir o c
                                              # com base em sua divisão inteira pelo número n.

if total == 2:
    print(f'\n\033[0;30mO número digitado é um número \033[0;31mPRIMO\033[0;30m, pois ele só é divisível por '
          f'\033[0;34m1 \033[0;30me por ele mesmo(nesse caso, \033[1;34m{n}\033[0;30m.)\033[m')

else:
    print(f'\n\033[0;30mComo o número digitado (\033[1;34m{n}\033[0;30m) é divisivel por mais de duas vezes ou uma '
          f'só vez (neste caso, \033[0;34m{total}\033[0;30m vez(es)), ele \033[1;31mNÃO \033[0;30mé um '
          f'\033[1;31mnúmero primo\033[0;30m.\033[m')