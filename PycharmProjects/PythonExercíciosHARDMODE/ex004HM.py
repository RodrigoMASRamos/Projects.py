# ex004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele

"""Obs: O programa apresenta erro de lógica. Veja a resolução para corrigir isso."""


branco = '\033[0;30m'
vermel = '\033[0;31m'
verde_ = '\033[0;32m'  # Falta memorizar este.
amarel = '\033[0;33m'
azul__ = '\033[0;34m'  # Falta memorizar este.
lilás_ = '\033[0;35m'
ciano_ = '\033[0;36m'  # Falta memorizar este.
cinza_ = '\033[0;37m'

brancoN = '\033[1;30m'
vermelN = '\033[1;31m'
verde_N = '\033[1;32m'  # Falta memorizar este.
amarelN = '\033[1;33m'
azul__N = '\033[1;34m'  # Falta memorizar este.
lilás_N = '\033[1;35m'
ciano_N = '\033[1;36m'  # Falta memorizar este.
cinza_N = '\033[1;37m'

brancoS = '\033[4;30m'
vermelS = '\033[4;31m'
verde_S = '\033[4;32m'  # Falta memorizar este.
amarelS = '\033[4;33m'
azul__S = '\033[4;34m'  # Falta memorizar este.
lilás_S = '\033[4;35m'
ciano_S = '\033[4;36m'  # Falta memorizar este.
cinza_S = '\033[4;37m'

brancoI = '\033[7;30m'
vermelI = '\033[7;31m'
verde_I = '\033[7;32m'  # Falta memorizar este.
amarelI = '\033[7;33m'
azul__I = '\033[7;34m'  # Falta memorizar este.
lilás_I = '\033[7;35m'
ciano_I = '\033[7;36m'  # Falta memorizar este.
cinza_I = '\033[7;37m'


algo = input(
    f'\033[1;30mDigite algo no teclado e eu lhe direi seu tipo primitivo e todas as informações possíveis sobre ele: '
    f'\033[m')
print(f'{branco}-==-\033[m' * 20)


print(f'{branco}O tipo primitivo de \033[1;30m({algo}){branco} é: \033[1;32m{type(algo)}.\033[m')


print(f'{branco}É composto somente por espaços? {amarelN}{algo.isspace()}.\033[m')
if algo.isspace() == True:
    print(f'{branco}O termo digitado (\033[1;30m{algo}\033[m){ciano_N}É{branco} composto somente por espaços.\033[m')
else:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) \033[1;31mNÃO É{branco} composto somente por espaços.\033[m')


print(f'{branco}É Alfabético? {amarelN}{algo.isalpha()}.\033[m')
if algo.isalpha() == True:
    print(f'{branco}O termo digitado (\033[1;30m{algo}{branco}){ciano_N} É{branco} Alfabético.\033[m')
else:
    print(f'{branco}O termo digitado (\033[1;30m{algo}{branco}){vermelN} NÃO É{branco} Alfabético.\033[m')


print(f'{branco}Está Capitalizado? {amarelN}{algo.istitle()}.\033[m')
if algo.istitle() == True:
    print(f'{branco}O termo digitado (\033[1;30m{algo}{branco}){ciano_N} ESTÁ {branco}Captalizado.')
else:
    print(f'{branco}O termo digitado (\033[1;30m{algo}{branco}){vermelN} NÃO ESTÁ {branco}Captalizado.')


print(f'{branco}Está escrito somente em MAIÚSCULAS? {amarelN}{algo.isupper()}.\033[m')
if algo.isupper() == True:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) {ciano_N}ESTÁ {branco}em CAIXA ALTA.\033[m')
else:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) {vermelN}NÃO ESTÁ {branco}em CAIXA ALTA.\033[m')


print(f'{branco}Está escrito somente em minúsculas? {amarelN}{algo.islower()}.\033[m')
if algo.islower() == True:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) {ciano_N}ESTÁ {branco}em caixa baixa.\033[m')
else:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) {vermelN}NÃO ESTÁ {branco}em caixa baixa.\033[m')


print(f'{branco}É numerico? {amarelN}{algo.isnumeric()}.\033[m')
if algo.isnumeric() == True:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) {ciano_N}É {branco}Numérico.\033[m')
else:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) {vermelN}NÃO É {branco}Numérico.\033[m')


print(f'{branco}É Alfabético e Numérico? {amarelN}{algo.isalnum()}.\033[m')
if algo.isalnum() == True:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}) {ciano_N}É {branco}Alfabético {ciano_}E {branco}Numérico')
else:
    print(f'{branco}O termo digitado ({brancoN}{algo}{branco}){vermelN} NÃO É {branco}Alfabético {ciano_}E {branco}Numérico')


print(f'{branco}O termo digitado {brancoN}{algo}{branco} possui {amarelN}{len(algo)}{branco} caractéres (incluindo os espaços).')
