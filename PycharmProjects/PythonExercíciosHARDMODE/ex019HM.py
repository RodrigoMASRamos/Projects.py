# ex019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

from random import choice

n1 = input('\033[0;30mDigite o primeiro nome: \033[m').strip()
n2 = input('\033[0;30mDigite o segundo nome: \033[m').strip()
n3 = input('\033[0;30mDigite o terceiro nome: \033[m').strip()
n4 = input('\033[0;30mDigite o quarto nome: \033[m').strip()
l = [n1,n2,n3,n4]

print('\033[0;36m-=-=-=-=\033[m' * 5)
print(f'\033[0;34mO aluno escolhido foi \033[4;30m{choice(l)}\033[0;34m.')
