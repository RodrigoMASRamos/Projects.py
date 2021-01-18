# Desafio 062 - Super Progressão Aritmética v3.0
#
# Melhore o DESAFIO 061.upper(), perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 TERMOS.

''' CÓDIGO DO EX061

c = 0

print('-=-' * 10)
print('Progressão Aritimética 2.0!')
print('-=-' * 10)

t1_ = input('Digite o primeiro termo da P.A.: ').strip()
r_ = input('Agora, digite a razão da P.A.: ').strip()
t1 = float(t1_)
r = float(r_)
tx = t1
a10 = (t1 + (10 - 1) * r)
print(a10)

while c != 10:
    print(f'{tx:.2f} --> ', end='')
    tx += r
    c += 1
'''

"""CÓDIGO ANTIGO E DEFEITUOSO

from time import sleep
print('-=-' * 10)
print('Progressão Aritimética 3.0!')
print('-=-' * 10)

t1_ = input('Digite o primeiro termo da P.A.: ').strip()
r_ = input('Agora, digite a razão da P.A.: ').strip()
t1 = float(t1_)
r = float(r_)
tx = t1

c = 0
resp = 's'                 # PS: NÃO coloque is True na linha abaixo.
while 's' in resp is True: # Por alguma razão o while não estava sendo executado... Descubra o motivo!
    print(f'{tx:.2f} --> ', end='') 
    tx += r
    c += 1
    resp = input('\nDeseja mostrar mais termos? [S/N]:').strip().lower()[0]
print('CALCULANDO O TOTAL DE TERMOS...')
sleep(2.5)
print(' ' * 1)
print(f'O ultimo termo mostrado foi {tx}, e no total, foram mostrados {c} termos!')
""" # Código antigo e defeituoso

# O progama original (abaixo) APARENTA estar funcionando corretamente, MAS como houve QUEBRA DE RACIOCÍNIO, eu
# faria mais alguns testes e iria refazer o exercício.
#
# PS: O exércicio é um pouco diferente do que deveria ser (código do Prof° Guanabara abaixo). Use o padrão do video
# de resolução pro Hard Mode!

from time import sleep
print('-=-' * 10)
print('Progressão Aritimética 3.0!')
print('-=-' * 10)

t1_ = input('Digite o primeiro termo da P.A.: ').strip()
r_ = input('Agora, digite a razão da P.A.: ').strip()
t1 = float(t1_)
r = float(r_)
tx = t1

c = 1
resp = str('s')
print('-=-='* 20)
while 's' in resp:
    print(f'{tx:.2f} --> ', end='')
    tx += r
    c += 1
    resp = str(input('\nDeseja mostrar mais termos? [S/N]:')).strip().lower()[0]
    while resp != 's' and resp!= 'n':
        resp = str(input('\nResposta inválida! Deseja mostrar mais termos? Digite [S/N]: ')).strip().lower()[0]
tx -= r
c -= 1
print('CALCULANDO O TOTAL DE TERMOS...')
sleep(2.5)
print(' ' * 1)
print(f'O ultimo termo mostrado foi {tx}, e no total, foram mostrados {c} termos!')