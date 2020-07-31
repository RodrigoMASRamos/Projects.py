#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O progframa deverá escrever na tela se o usuário
# venceu ou perdeu.
from random import randint
nUser = input ('O computador vai pensar em um número inteiro de 0 a 5. Adivinhe qual é: ').strip()
nUser = int(nUser)
nPC = int (randint(0,5))
if nUser == nPC:
    print('Incrivel, você acertou! Tome esse emoji como recompensa: (～￣▽￣)～')
else:
    print(f'Lamento, você errou, o computador pensou em {nPC} (っ °Д °;)っ')
