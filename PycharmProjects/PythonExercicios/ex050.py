# Exercício Python #050 - Soma dos pares
#
# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES. Se o valor
# digitado for ÍMPAR, desconsidere-o.

c_ = 0
s = 0

for c in range(5,-1,-1):

    n = str(input('\033[0;30mDigite um número inteiro e este programa lhe mostrará '
                  'a soma \033[1;30mAPENAS \033[0;30mdaqueles que forem \033[1;30mPARES: \033[m')).strip()

    print(f'\033[0;30mEssa pergunta ainda será feita \033[1;31m{c}x\033[m.\033[m ')
    n = int(str(n))

    if n % 2 == 0:
        print('\033[0;30mO número digitado é \033[0;34mPAR\033[0;30m.\033[m')
        s += n
        c_ += 1

    elif n % 2 != 0:
        print('\033[0;30mO número digitado é \033[0;31mIMPAR\033[0;30m.\033[m')

    else:
        print('\033[1;31mNão foi possível executar o programa corretamente.\033[m')

print(f'A soma de todos os {c_} números PARES é igual a {s}.')