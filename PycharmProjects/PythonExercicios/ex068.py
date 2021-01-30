# Desafio 068 - Jogo do Par ou Ímpar
#
# Faça um programa que jogue PAR OU ÍMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
from random import randint
print('Então, você vai me desafiar novamente? (￣y▽,￣)╭ ')
sleep(2.0)
print('=-='*20)
num_wins = int(0)

while True:
    player_choice = input('Par ou Ímpar? [P/I] ').strip().upper()
    player_num = int(input('Digite um número inteiro entre 0 e 10: '))

    while player_choice != "P" and player_choice != "I":
        print('Você digitou errado...')
        player_choice = input('Par ou Ímpar? [P/I] \n').strip().upper() # DICA MODO HARD: CONFERIR SE O NUMERO DIGITADO
    if player_choice == 'P':                                            # É OU NÃO UM NÚMERO
        pc = 'I'
    else:
        pc = 'P'
    pc_num = randint(0,10)
    print(f'\nVocê escolheu "{player_choice}", e eu escolhi "{pc}"!')
    print(f'Seu número é {player_num}, e o meu é {pc_num}!')
    soma = int(pc_num + player_num)
    print(f'A soma dos nossos dois números é {soma}!')

    print('-' * 30)

    if player_choice == 'P' and soma % 2 == 0:
        winner = 'Player'
        print(f'Puxa vida, eu PERDI! ＞﹏＜\n')
        num_wins += 1
    elif player_choice == 'I' and soma % 2 != 0:
        winner = 'Player'
        print(f'Puxa vida, eu PERDI! ＞﹏＜\n')
        num_wins += 1
    else:
        winner = 'PC'
        print(f'HAHA, EU VENCI! ψ(｀∇´)ψ\n')
    if winner == 'PC':
        break
print('===' * 15)
print(f'No total, você ganhou {num_wins}x!')
