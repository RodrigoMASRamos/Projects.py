#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

#n = int(input('Digite um número inteiro para descobrir se ele é par ou ímpar: '))
#n % 2
#if n % 2 == 0:
#    print('Esse número é um número PAR.')
#else:
#    print('Esse número é um número ÍMPAR.')

número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'O número {número} é PAR')
else:
    print(f'O número {número} é ÍMPAR')



