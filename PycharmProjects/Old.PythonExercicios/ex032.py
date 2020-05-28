# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input('Digite um ano para descobrir se ele é bissexto: '))
if ano % 4 == 0:
    ano % 100 != 0
    print(f'O ano {ano} é BISSEXTO ')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')