# Desafio 060 - Cálculo de Fatorial
#
# Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL.
#
# Ex:
#   5! =  5 x 4 x 3 x 2 x 1 = 120
# Tive BASTANTE dificuldade em resolver esse exercício, provavelmente por causa da matemática e do if em uma linha.
# Note que o código está MUUUITO parecido com o do professor. Estude mais esse exercício, de verdade....
# PS: Também ESTUDE MATEMÁTICA!

''' CÓDIGO ANTIGO E DEFEITUOSO

n_ = input('Digite um número qualquer(por favor, rapido! Tenho pressa, preciso ver anime): ')
n = float(n_)
nf = n
nl = [0]
while nf != 1:
    nl += [n - 1]
    nf = nf - 1
    n = n - 1
    print(nf)
print(nl)
print(nf)
fatorial = nl[0]
print(f'A fatorial do número {n} é igual a {}.')
'''

from time import sleep

num_ = str(input('Digite um número qualquer: ')).strip()
num = float(num_)
c = num
f = 1  # Meu erro foi colocar 0 aqui. Para uma multiplicação inicial limpa, é necessario o 1, pois x * 1 = x!
print(f'Calculando {num:.2f}!')
sleep(5)

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')  # Não precisa(nem dá certo nesse caso) colocar um print dentro do outro.
    f *= c  # f = f * c                       # Minha grande dificuldade foi com o "if" em uma linha. Treine ele mais!
    c -= 1  # c = c - 1
print(f)

'''CÓDIGO GUANABARA           
    
# FORMA 1 (Utilizando a Biblioteca Math)
    from math import factorial
    n = int(input('Digite um número para calcular seu Fatorial: '))
    f = factorial(n)
    print(f'O fatorial de {n} é {f}.)
    
# FORMA 2 (Utilizando a pura lógica)
    n = int(input('Digite um número para calcular seu Fatorial: '))
    c = n
    f = 1
    print(f'Calculando {n}! =', end='')
    while c > 0:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    print(f'O fatorial de {n} é {f}.)
      
''' # Código do Prof° Gustavo Guanabara!
