# Desafio 069 - Análise de dados do grupo
#
# Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada, o programa deverá perguntar
# se o USUÁRIO quer ou não continuar. No final, mostre:
#
#   A) Quantas pessoas tem mais de 18 ANOS.
#   B) Quantos HOMENS foram cadastrados.
#   C) Quantas MULHERES tem menos de 20 ANOS.
resp_while = ''

cont_18 = 0
cont_men = 0
cont_won20 = 0
while True:
    age = int(input('Digite a idade: '))
    gender = input('Digite o sexo[M/F]: ').strip().capitalize()[0]
    if age >= 18:
        cont_18 += 1
    if gender == 'M':
        cont_men += 1
    if gender == 'F' and age < 20:
        cont_won20 += 1
    resp_while = input('Deseja continuar? [S/N]: ').strip().capitalize()[0]
    if resp_while == 'N':
        break
print(f'''No total, há {cont_18} pessoas com mais de 18 anos.
Foram cadastrados {cont_men} homens.
Há {cont_won20} mulheres com menos de 20 anos.''')
