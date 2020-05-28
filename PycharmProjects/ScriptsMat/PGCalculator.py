# Termo Geral da P.G
#n = posição
#q = razão
#a= termo
#An0 = A(n-1)
# Razão= q = An / An0
#        q = An / A(n-1)
#Termo geral da PG:
#                   An = A1*q^n-1

import math

A1 = float(input('Digite o primeiro termo(A1): '))
n = int(input('Agora, digite a posição do termo que você deseja descobrir: '))
q = str(input('Você possui a razão(q)? Digite S/N: '))
if q == 'S':
    q = float(input('Maravilha! Me conte qual é: '))
    An = A1*q**(n-1)
    print(f'O termo geral é:{An}')
else:
    q == 'N'
    An = float(input('Que pena. Me conte qual é o termo geral para descobrirmos a razão: '))
    An0 = float(input('Agora, me conte qual é o termo que vem antes deste: '))
    q = An / (An - An0)
    print(f'Segundo os calculos desso programa, a razão (q) vale: {q}. ')

