# Exercício Python #037 - Conversor de Bases Numéricas
#
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
#
#       - 1 para BINÁRIO
#       - 2 para OCTAL
#       - 3 para HEXADECIMAL
#
# OBS: 
n_ = str(input('Digite um NÚMERO INTEIRO qualquer:')).strip()

print('-=-' * 20)
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')
print('-=-' * 20)
b_ = str(input('Agora, escolha qual será a BASE DE CONVERSÃO de acordo com a tabela acima: ')).strip()

n = int(n_)
b = int(b_)

if b == 1: