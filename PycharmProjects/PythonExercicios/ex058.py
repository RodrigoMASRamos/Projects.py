# Desafio 058 - Jogo da Adivinhação v2.0
#
# Melhore o jogo do DESAFIO 028.upper() onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('Como no Desafio 028, o computador pensará em um número inteiro de 0 a 10. Descubra qual é.')
nPC = int(randint(0,10))
print('PENSANDO...')
sleep(3)
nUser_ = input('PRONTO! Em que número eu pensei? ').strip()
nUser = int(nUser_)

while nPC != nUser:
    nUser_ = input(f'Você errou ¯\_(ツ)_/¯! Eu pensei em {nPC}, não em {nUser}! Digite um novo valor: ').strip()
    nUser = int(nUser_)

print(f'Meus parabéns, você acertou... Eu pensei em {nPC}, e você digitou {nUser} (○｀ 3′○)')

'''
CÓDIGO GUANABARA

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
'''
