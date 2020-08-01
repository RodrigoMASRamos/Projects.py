# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.
'''Obs: esse exercício exige o conhecimento de uma regra matemática: cada uma das retas tem que ser menor que a soma do
comprimento das outras duas
        Ex: Reta1 < Reta 2 + Reta 3
Sabendo disso, abaixo está o programa:'''
print('-==-' * 20)
print('Digite o valor pedido de três retas e eu lhe direi se elas podem ou não formar um triângulo!')
print('-==-' * 20)
r1 = input('Digite o comprimento da primeira reta (ignore a unidade de medida): ').strip()
r2 = input('Agora, digite o comprimento da segunta reta: ').strip()
r3 = input('Mais uma vez, digite o comprimento da terceira reta: ').strip()
r1 = float(r1)
r2 = float(r2)
r3 = float(r3)
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print(f'As retas {r1}, {r2}, {r3} PODEM SIM formar um triângulo!')
else:
    print(f'Infelizmente, as retas {r1} , {r2}, {r3} NÃO PODEM formar um triângulo...')