# Desafio 057 - Validação de Dados
#
# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.
#
# OBS: Tive dificuldade em resolver esse exercício... Estude mais!

''' MEU CÓDIGO ANTIGO (ERRADO)
sexo = ''
while sexo == '' or sexo != 'M' and 'm' and 'F' and 'f':  # Tentei fazer a validação de dados da forma errado, usando o
    sexo = input('Digite o sexo (M/F): ').strip().upper() # while qnd o usuário digitou o sexo corretamente, não
    if sexo != 'M' and 'm' and 'F' and 'f':               # incorretamente!
        sexo = str(input('Valor de Entrada inválido! Digite M/F: '))
    print(sexo)
'''

sexo = str(input('Digite o sexo de uma pessoa (M/F): ')).strip().capitalize()
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'Dado de entrada inválido(Você digitou {sexo})! Digite novamente(M/F): ')).strip().capitalize()
print(f'O sexo digitado foi {sexo}.')
