# Desafio 072 - Número por Extenso
#
# Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
# Seu programa deverá ler um número pelo teclado (ENTRE 0 E 20) e mostrá-lo por EXTENSO.

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'desoito', 'dezenove', 'vinte')

indice_num = int(input('Digite um número inteiro qualquer entre 0 e 20: '))
while indice_num < 0 or indice_num > 20:
    print('Tente novamente')
    indice_num = int(input('Digite um número inteiro qualquer entre 0 e 20: '))

print(f'O número escolhido foi "{números[indice_num]}".')