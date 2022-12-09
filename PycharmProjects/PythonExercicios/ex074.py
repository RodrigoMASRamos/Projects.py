# Desafio 074 - Maior e menor valores em Tupla
#
# Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.
# Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla.
#
# NOTA: A ideia é resolver este exercíco sem abordar listas, pois isso é só na proxima aula. Porém, eu resolvi com
# listas pela urgente necessidade de aprender ordenação bolha, e tuplas não podem ser ordenadas.
# Depois, tente fazer ordenação bolha com a função enumarate em um laço
#
''' CÓDIGO DO GUANABARA

from random import randint

numeros = ( randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10) ) # E se fosse 100 números? Tente
achar outra maneira!

print('Os valores sorteados foram: ', end='')
for n in numeros: # usa "n" como indice para exibir numeros[n]
    print(f'{n} ', end ='')

print(f'\nO maior valor sorteado foi {max(numeros)}') # max() <- Função que detecta MAIOR valor na Variavel.
print(f'O menor valor sorteador foi {min(numeros)}')  # min() <- Função que detecta MENOR valor na Variavel.
'''

from random import randint

bolha = None
indice = 0 # Também servirá como contador

lista_p_tupla = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
print(f'Os números sorteados, FORA DA ORDEM, foram: {lista_p_tupla}')

while indice < len(lista_p_tupla) - 1:
    if lista_p_tupla[indice] > lista_p_tupla[indice + 1]:
        bolha = lista_p_tupla[indice]
        lista_p_tupla[indice] = lista_p_tupla[indice + 1]
        lista_p_tupla[indice + 1] = bolha
    else:
        break
    indice += 1
print(f'Os números sorteados ORDENADOS são: {lista_p_tupla}')




