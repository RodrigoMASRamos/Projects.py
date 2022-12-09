import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz}.')
print(f'A raiz de {num} é igual a {math.ceil(raiz)}.')
print(f'A raiz de {num} é igual a {math.floor(raiz)}')
print(f'A raiz de {num} é igual a {raiz:.2f}')
from math import sqrt
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz}.')
import random
num2 = random.random()
print(num2)
num3 = random.randint(1, 10)
print (num3)
import emoji
print(emoji.emojize('Olá, Mundo!:sunglasses:',use_aliases=True))