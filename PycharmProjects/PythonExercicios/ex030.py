#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
num = input('Digite um número inteiro, e eu vou lhe dizer se ele é par ou impar: ').strip()
num = int(num)
if num % 2 == 0:
    print(f'O número {num} é um número par.')
else:
    print(f'O número {num} é um número impar.')