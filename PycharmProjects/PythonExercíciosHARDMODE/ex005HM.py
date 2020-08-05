#ex005: faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n =input('\033[1;30mDigite o valor de um número inteiro e eu lhe mostrarei o seu sucessor e antecessor: \033[m').strip()
num = int(n)
snum = num + 1
anum = num - 1
print('\033[0;35m-=-=-=-\033[m' * 8)
print(f'\033[0;30mO antecessor de \033[1;34m{num}\033[0;30m é \033[1;31m{anum}\033[0;30m, e o sucessor de\n'
      f'\033[1;34m{num}\033[0;30m é \033[1;32m{snum}\033[m.')
print('\033[0;35m=-=-=-=\033[m' * 8)