# Exercício Python #045 - GAME: Pedra Papel e Tesoura
#
# Crie um programa que faça o computador jogar JOKENPÔ com você.

# Aprenda a arrumar as cores nas respostas!

from random import choice
from random import randint  # Maneira utilizada na resolução deste exercício
from time import sleep

print('\033[1;31mATENÇÃO! ESTE É UM JOGO ALTAMENTE PERIGOSO ONDE NÃO HÁ CHANCES DE VITÓRIA PARA VOCÊ!\033[m')
Uc = input('\033[0;30mMe diga, \033[1;34mó grande jogador, \033[0;30mvocê escolhe \033[1;35mPEDRA, \033[1;31mPAPEL, '
           '\033[0;30mou \033[1;36mTESOURA? ').strip().upper()

PC = ['\033[1;35mPEDRA\033[m', '\033[1;31mPAPEL\033[m', '\033[1;36mTESOURA\033[m']
PCc = choice(PC)

sleep(0.5)
print('JO')

sleep(1)
print('KEN')

sleep(1)
print('PO!')

if PCc == 'PEDRA' and Uc == 'TESOURA' or PCc == 'TESOURA' and Uc == 'PAPEL' or PCc == 'PAPEL' and Uc == 'PEDRA':
    print(f'\033[1;31mHAHAHA! Eu venci! \033[0;30mEu escolhi \033[m{PCc} \033[0;30me você \033[m{Uc}\033[0;30m!')
elif PCc == Uc:
    print(f'\033[1;33mEMPATE! Vamos jogar novamente! Eu escolhi \033[m{PCc} \033[0;30me você \033[m{Uc}')
else:
    print(f'\033[0;34mT-T Infelizmente,\033[1;32mvocê venceu... \033[0;30mEu escolhi \033[m{PCc}, \033[0;30me você '
          f'escolheu \033[m{Uc}\033[0;30m...\033[m')