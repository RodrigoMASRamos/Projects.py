# Exercício Python #046 - Contagem regressiva
#
# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;31m-=-\033[m' * 20)
print('\033[0;35mPEW! BOOOM! PEW! JINX ADORA EXPLOSÕES!\033[m')
print('\033[1;31m-=-\033[m' * 20)