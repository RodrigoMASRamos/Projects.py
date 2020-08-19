# Exercício Python #038 - Comparando números
# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
#
#       - O PRIMEIRO VALOR é MAIOR
#       - O SEGUNDO VALOR é MAIOR
#       - NÃO EXISTE valor maior, os dois são IGUAIS

print('\033[1;30mEste programa irá ler \033[1;35mdois números inteiros \033[1;30me \033[1;34mcompara-los\033[1;30m, '
      'dizendo qual deles é o \033[1;36mmenor \033[1;30me qual deles é o \033[1;31mmaior\033[1;30m.\033[m')
print('\033[0;32m-=-\033[m' * 37)
n1_ = input('\033[0;30mDigite o valor do \033[1;34mprimeiro número inteiro: \033[m').strip()
n2_ = input('\033[0;30mDigite o valor do \033[1;34msegundo número inteiro: \033[m').strip()

n1 = int(n1_)
n2 = int(n2_)

# Há uma maneira mais simples de fazer o mesmo exercicio sem utilizar condições aninhadas. Tal resolução está no
# mundo 1 em algum dos exercícios de Python

if n2 < n1:
    menor = n2
    maior = n1
    print(f'\033[0;30mO \033[1;31mmaior \033[0;30mnúmero é \033[1;31m{maior} \033[0;30me o \033[1;36mmenor '
          f'\033[0;30mnúmero é \033[1;36m{menor}.\033[m')

elif n1 < n2:
    menor = n1
    maior = n2
    print(f'\033[0;30mO \033[1;31mmaior \033[0;30mnúmero é \033[1;31m{maior} \033[0;30me o \033[1;36mmenor '
          f'\033[0;30mnúmero é \033[1;36m{menor}\033[m.\033[m')

else:
    print(f'\033[0;30mOs \033[1;34mnúmeros \033[0;30mdigitados \033[1;34m({n1} e {n2}) \033[0;30msão '
          f'\033[1;34mIGUAIS.\033[m')