#ex025: Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome.
n_ = input('\033[1;30mDigite o nome de uma pessoa e este programa dirá se esse nome possui "SILVA" ou não: \033[m').strip()
n = n_.upper()
if 'SILVA' in n == True:
    print(f'\033[0;30mNo nome \033[0;34m{n_}\033[0;30m, \033[1;32mHÁ SIM \033[0;30ma palavra '
          f'\033[0;36m"SILVA"\033[0;30m!')
else:
    print(f'\033[0;30mNo nome \033[0;34m{n_}\033[0;30m, \033[1;31mNÃO HÁ \033[0;30ma palavra '
          f'\033[0;36m"SILVA"\033[0;30m...')

#Há uma brecha no codigo. Veja os comentários da resolução e corrija isso!