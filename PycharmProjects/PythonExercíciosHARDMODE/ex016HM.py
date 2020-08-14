#ex016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ex: Digite um número: 6.127
#      O número 6.127 tem a parte Inteira 6.
from math import trunc

print('\033[1;30mEsse programa lhe mostrará a parte inteira do número digitado.\033[m')
print('\033[0;35m\/\/\/\/\/\/\033[m' * 5)

n = (input('\033[0;30mDigite um número real qualquer: \033[m')).strip()

ni = float(n)

print('\033[1;34m-_-_-_-_-_-_\033[m'* 5)
print(f'\033[0;30mA parte inteira do número \033[1;36m{n} \033[0;30mé \033[1;36m{trunc(ni)}\033[0;30m.')
print('\033[0;34m-_-_-_-_-_-_\033[m'* 5)


# A resolução abaixo é mais simples para ser realizada, mas optei pela resposta acima pela aplicação dos modulos e
# bibliotecas abordadas em aula.

'''print('\033[1;30mEsse programa lhe mostrará a parte inteira do número digitado.\033[m')
print('\033[0;35m\/\/\/\/\/\/\033[m' * 5)
n = float(input('\033[0;30mDigite um número real qualquer: \033[m'))

ni = int(n)
print('\033[1;34m-_-_-_-_-_-_\033[m'* 5)
print(f'\033[0;30mA parte inteira do número \033[1;36m{n} \033[0;30mé \033[1;36m{ni}\033[0;30m.')
print('\033[0;34m-_-_-_-_-_-_\033[m'* 5)'''