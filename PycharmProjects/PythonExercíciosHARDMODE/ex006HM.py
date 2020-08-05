#ex006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
nstr = input(f'\033[1;30mDigite um número, e este algorítimo irá lhe informar o seu dobro, triplo e raiz quadrada: \033[m')
print('\033[0;32m-=-=-=-=-=\033[m' * 9)
# print(len('Digite um número, e este algorítimo irá lhe informar o seu dobro, triplo e raiz quadrada: '))
n = float(nstr)
print(f'\033[0;30mO dobro de \033[1;34m{n} \033[0;30mé \033[1;36m{n * 2}.')
print(f'\033[0;30mO triplo de \033[1;34m{n} \033[0;30mé \033[1;36m{n * 3}.')
print(f'\033[0;30mA raiz quadrada de \033[1;34m{n} \033[0;30mé \033[1;36m{n ** 0.5}')
print('\033[0;32m-=-=-=-=-=\033[m' * 9)