# ex:020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = input('\033[0;30mDigite o primeiro nome: \033[m').strip()
n2 = input('\033[0;30mDigite o segundo nome: \033[m').strip()
n3 = input('\033[0;30mDigite o terceiro nome: \033[m').strip()
n4 = input('\033[0;30mDigite o quarto nome: \033[m').strip()
l = [n1,n2,n3,n4]
shuffle(l)
print('\033[0;31m-=-=-=-=\033[m' * 10)
print(f'\033[0;36mA ordem de apresentação será, respectivamente: \033[4;30m{l}')
print('\033[0;31m-=-=-=-=\033[m' * 10)
