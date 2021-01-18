# Desafio 063 - Sequência de Fibonacci v1.0
#
# Escreva um programa que leia um NÚMERO N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# SEQUÊNCIA DE FIBONACCI.
#
# Ex:
#   0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#
# Tive bastente dificuldade com esse exercício... Esse mundo tá fod@. Estude mais while! Pensei em
# fazer um contador, acho que nisso acertei...
#
# IDEIA PARA MODO HARD: O NÚMERO DIGITADO TAMBÉM É A QUANTIDADE DE NÚMEROS MOSTRADOS DA SEQUENCIA DE FIBONACCI
# DESTE MESMO NÚMERO!

''' MEU 1° CÓDIGO ANTIGO E DEFEITUOSO (POR FAVOR, RASTREIE ELE)

print('-=-' * 10)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 10)
num = int(input('Digite um número inteiro da quantidade dos elementos da sequência: '))
c = 3
t1 = 0
t2 = 1
while c != num:
    print(f'{t1}  ->  {t2}', end='')
    t3 = t1 + t2
    print(f'  -> {t3}', end='')
    t1 = t2
    t2 = t3
    c = c + 1

#    0 - 1 - 1 - 2 - 3 - 5
#       t1  t2  t3
'''

print('-=-' * 10)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 10)
num = int(input('Digite um número inteiro da quantidade dos elementos da sequência: '))
c = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='') # Aparentemente, essa linha estar dentro do while que era o grande problema...
while c <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c = c + 1

#    0 - 1 - 1 - 2 - 3 - 5
#       t1  t2  t3

''' CÓDIGO GUANABARA

print('-'*30)
print('Sequência de FIbonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont =3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * 30)
''' # CÓDIGO GUANABARA