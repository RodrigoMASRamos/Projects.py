# Exercício Python #051 - Progressão Aritmética
#
# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
#
# OBS: Eu tentei realizar esse exercicio, fiz o codígo mas ele apresentou ERRO DE LÓGICA! Estude mais P.A e
# esse conteudo!

print('\033[0;35m-=-\033[m' * 10)
print('\033[1;36mPROGRESSÃO ARITIMÉRICA (P.A)\033[m')
print('\033[0;35m-=-\033[m' * 10)

t1 = str(input('\033[0;30mDigite o PRIMEIRO TERMO da P.A: \033[m')).strip()
r = str(input('\033[0;30mAgora, digite a RAZÃO da P.A: \033[m')).strip()
t1 = int(str(t1))
r = int(str(r))
a10 = t1 + (10 - 1) * r # Fórmula da P.A ADAPTADA para a linguagem PYTHON

print(' ' * 20)

print('\033[1;30mAbaixo,seguem os 10 primeiros termos da Progressão Aritimética: \033[m')
for p_a in range(t1 ,a10 + r, r): # Está escrito a10 + r porque o Python ignora o último termo.
    print(f'\033[0;34m{p_a}\033[m', end=' ')
print('\n\033[1;31mFIM!\033[m')
