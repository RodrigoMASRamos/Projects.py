# Desafio 066 - Vários números com flag
#
# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre quantos números foram digitados e qual foi a SOMA entre eles
# (desconsiderando o flag).
num = 0
soma_count = 0
soma_num = 0
while True:
    num = int(input('Digite um número inteiro (Ou 999 para parar): '))
    if num == 999:
        break
    soma_count += 1
    soma_num += num
print(f'Programa FINALIZADO! No total, foram digitados {soma_count} números (desconsiderando o flag) e a soma de todos'
      f' eles é igual a {soma_num}.')
