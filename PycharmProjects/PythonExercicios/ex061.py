# Desafio 061 - Progressão Aritmética v2.0
#
# Refaça o DESAFIO 051.upper(),lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da
# progressão usando a estrutura WHILE.
#
# OBS: Sério, estude mais matemática! Sofri um pouco pra fazer esse exercício (precisei olhar códigos antigos).

''' Exercício 051 (Sem formatação).

print('-=-' * 10)
print('PROGRESSÃO ARITIMÉRICA (P.A)')
print('-=-' * 10)

t1 = str(input('Digite o PRIMEIRO TERMO da P.A: ')).strip()
r = str(input('Agora, digite a RAZÃO da P.A: ')).strip()
t1 = int(str(t1))
r = int(str(r))
a10 = t1 + (10 - 1) * r # Fórmula da P.A ADAPTADA para a linguagem PYTHON

print(' ' * 20)

print('Abaixo,seguem os 10 primeiros termos da Progressão Aritimética: ')
for p_a in range(t1 ,a10 + r, r): # Está escrito a10 + r porque o Python ignora o último termo.
    print(f'{p_a}', end=' ')
print('\nFIM!')
'''

# Fórmula da PA: a10 = t1 + (10 - 1) * r # Fórmula da P.A ADAPTADA para a linguagem PYTHON

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
print('FIM!')

''' CÓDIGO GUANABARA
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ->', end='')
    termo += razão
    cont += 1
print('FIM') 
''' # Código do Prof° Gustavo Guanabara
