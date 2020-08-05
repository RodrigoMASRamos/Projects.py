# ex002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas
import pygame

nome = input('Olá! Qual é o seu nome? ').strip()
print(f'Olá, {nome}! Seja muito bem vindo(a)!')
nome = str(nome.upper())

# A

if nome == 'ARCHER':
    print('I am the Bone of my sword.')

if nome == 'ARROW' or nome == 'ARQUEIRO VERDE' or nome == 'GREEN ARROW' or nome == 'OLIVER QUEEN' or nome == 'OLLY':
    citado = "Ra's al Ghul"
    print(f'"Oliver Queen é um homem destinado a ficar só." - {citado}')

if nome == 'AKUMA':
    print('Seria esse o verdadeiro mestre do Ansatsuken?')

# B

if nome == 'BATMAN' or nome == 'BRUCE WAYNE':
    print('Nananana... Batman! ')

# C

if nome == 'CHARADA' or nome == 'EDWARD NYGMA' or nome == 'NYGMA':
    resposta = input('O que pertence a você, mas os outros utilizam mais? ').strip().lower()
    if 'nome' in resposta is True:
        print('nome' in resposta)
        print('Você realmente é o Charada!')
    else:
        print ('nome' in resposta)
        print('NÃÃÃÃÃÃO!')

if nome == 'CHUN - LI' or nome == 'CHUN LI':
    print('Policial mestra em Kung - Fu detectada!')


# D

if nome == 'DARIUS':
    print('Não conte para ninguém, mas... Eu sirvo a Noxus!')
# E

# F

if nome == 'FLASH' or nome == 'BARRY' or nome == 'BARRY ALLEN':
    print('"Corro, não paro, me movo: sinto que posso de tudo quando acelerar!"')

if nome == 'FLASH REVERSO' or nome == 'REVERSE FLASH' or nome == 'Eobard Thawne' or nome == 'Thawne':
    print('Seria esse um paradoxo vivo? Você só vai nascer no ano de 2151!')

# G

# H

# I

# J

if nome == 'JOKER' or nome == 'CORINGA':
    print('Era uma vez, um louco palhacinho...')
# K

if nome == 'KINDRED':
    resposta = input('Complete a frase: Nunca um... ').strip().capitalize()
    if resposta == 'Sem o outro':
        print('A ovelha ficou contente com sua resposta.')
    else:
        print('Lamentavel, o lobo vai te caçar hoje a noite!')
# L

if nome == 'LILI' or nome == 'QUEEN':
    print('Waifu a vista! Me tragam uma pokebola!')
    pygame.init()
    pygame.mixer.music.load("ex002HM-1.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()

if nome == 'L' or nome == 'LIGHT YAGAMI' or nome == 'LIGHT' or nome == 'YAGAMI' or nome == 'KIRA':
    print('Não pode ser... Você é a JUSTIÇA!?')

if nome == 'LENA' or nome == 'TRACER' or nome == 'OXTON' or nome == 'LENA OXTON':
    print('Pense como a Tracer, com seu coração s2')

# M

if nome == 'MAKISE KURISU' or nome == 'KURISU MAKISE' or nome == 'KURISU' or nome == 'MAKISE':
    print('Supera cara. Ela já está morta.')

if nome == 'MAYURI' or nome == 'MAYURI SHIINA' or nome == 'SHIINA MAYURI' or nome == 'MAYUSHII' or nome == 'MAYUSHI':
    print('Tu-tu ru!!!')

if nome == 'MINATO' or nome == 'MINATO NAMIKASE' or nome == 'NAMIKASE MINATO':
    print('Veloz como um trovão, é melhor eu ficar esperto!')
# N

if nome == 'NEAR' or nome == 'MELLO':
    print('A missão foi completada, com Mello e Near!')
# O

if nome == 'OKABE RINTAROU' or nome == 'OKABE RINTARO' or nome == 'RINTARO' or nome == 'OKABE' or nome == 'RINTARO ' \
                                                                                                          'OKABE':
    print('Você escreveu errado, é HOHOUIN KYOUMA!')
# P

# Q

# R

if nome == 'RICARDO' or nome == 'RICARDINHO' or nome == 'RICARDO M.A.S. RAMOS' or nome == 'RICARDO MAS RAMOS' or \
        nome == 'RICARDO M.A.S RAMOS':
    print('Mas... você ainda não acabou Demon Slayer. Volta pro Apex!')


if nome == 'RIVENZINHA' or nome == 'RIVENZINHA':
    print('O universo se emociona com a perfeição da luz!')

if nome == 'ROBERTO' or nome == 'ROBERTO DA SILVA RAMOS' or nome == 'ROBERTO SILVA RAMOS' or nome == 'ROBERTO RAMOS':
    print('Meu Avô!')

if nome == 'RODRIGO' or nome == 'RODRIGO M.A.S. RAMOS' or 'RODRIGO' in nome is True:
    print('Criador do código detectado! Seremos eternamente gratos!')
    print('Ao trilhar uma longa estrada, é mais fácil prosseguir do que dar meia-volta')

if nome == 'ROSANA' or nome == 'ROSANA MENDES' or nome == 'ROSANA MENDES DE ALMEIDA' or nome == 'ROSANA MENDES DE ' \
                                                                                                'ALMEIDA SILVA RAMOS':
    print('Minha Avó!')

# S

if nome == 'SASUKE' or nome == 'SASUKE UCHIRA' or nome == 'UCHIRA SASUKE':
    print('Você não vai gritar "NARUTOOOO!", vai?')
if nome == 'SORA' or nome == 'NICOLAS':
    print('Olha só, se não é o amante de twin-tails...')

# T
if nome == 'TALON':
    print('Por favor, não me mate! Você não quer perder mais uma lâmina, quer?')

# U


# V
if nome == 'VAYNE':
    print('"Me falaram para andar nas sombras, agora eu me tornei o novo batman..."')

# W


# X


# Y


# Z
