# ex028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.
from random import randint # Essa função "randomiza" um número inteiro qualquer entre os números pedidos.
from time import sleep # Esse método irá fazer o computador "dormir" e esperar um tempo determinado em segundos

print('\033[0;35m-=-\033[m' * 30)
print('\033[1;30mO computador irá pensar em um número inteiro aleatório de 0 a 5. Adivinhe qual é!\033[m')
print('\033[0;35m-=-\033[m' * 30)
print('\033[0;30mPENSANDO...\033[0;30m')
sleep(5)
nu_ = input('\033[0;30mQual foi o número que eu pensei? \033[m').strip()
nu = int(nu_)
nc = randint(0,5)
if nu == nc:
    print('\033[0;30mIncrível, você \033[1;32macertou! \033[0;30mEu \033[1;31mperdi \033[0;30mヽ(*。>Д<)o゜\033[m')
else:
    print(f'\033[0;31mHAHAHA, \033[0;30meu pensei em \033[0;34m{nc}\033[0;30m, e não em \033[0;36m{nu}\033[0;30m! '
          f'\033[1;31mEu venci!\033[0;30m(((o(*ﾟ▽ﾟ*)o)))')