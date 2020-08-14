#ex024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ‘SANTO’

cd = input('\033[1;30mDigite o nome de uma cidade, e eu direi se ela começa ou não com '
           'o nome "Santo": \033[m').strip().capitalize().split()
if cd[0] == 'Santo':
    print(f'\033[0;30mA cidade \033[1;30m{" ".join(cd)} \033[0;32mCOMEÇA \033[0;30mcom a palavra '
          f'\033[1;30m"Santo"\033[0;30m!\033[m')
else:
    print(f'\033[0;30mA cidade \033[1;30m{" ".join(cd)} \033[0;31mNÃO COMEÇA \033[0;30mcom a palavra '
          f'\033[1;30m"Santo"\033[0;30m...\033[m')


# Para economizar memória, eu utilizei o .split() em conjunto com o input, o que fez com que eu precisasse utilizar o
# join(essa era a intenção). Porém o Print saiu sem a formatação correta, corrija isso na proxima vez!
