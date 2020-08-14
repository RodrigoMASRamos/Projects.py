# ex021: Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer
mixer.init()
mixer.music.load('ex021hd.mp3')
mixer.music.play()
input(' ')

#CÓDIGO DA RESOLUÇÃO (SEM ALTERAÇÕES):
'''
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
 input('Agora você escuta?')'''

# O pygame sofreu alterações, e por isso, a resolução apresentada pelo Guanabara não funciona mais.
# Abaixo está a resolução antiga:
