# ex:017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e
# mostre o comprimento da hipotenusa.

from math import hypot
print('\033[1;30mEste programa irá calcular a hipotenusa de um triângulo.\033[m')

cos = input('\033[0;30mDigite o cateto oposto: \033[m')
cas = input('\033[0;30mAgora, digite o cateto adjacente: \033[m')

co = float(cos)
ca = float(cas)
hypot(co,ca) # A função hypot calcula a hipotenusa automaticamente para você

print('\033[1;34m+=+=+=+=+=+=' * 4)
print(f'\033[0;30mA hipotenusa do triangulo é igual a \033[1;31m{hypot(co,ca):.2f}\033[0;30m.')
print('\033[0;34m+=+=+=+=+=+=' * 4)



'''Abaixo, se encontra a maneira matemática(e mais complicada) de resolver este exercício:

print('Este programa irá calcular a hipotenusa de um triângulo.')

cos = input('\033[0;30mDigite o cateto oposto: \033[m')
cas = input('\033[0;30mAgora, digite o cateto adjacente: \033[m')

co = float(cos)
ca = float(cas)
hi = (ca ** 2 + co ** 2) ** 0.5
print(f'A hipotenusa do triangulo é igual a {hi:.2f}.')

'''
