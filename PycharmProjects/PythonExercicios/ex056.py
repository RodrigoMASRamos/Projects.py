# Exercício Python #056 - Analisador completo
#
# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre:
#   - A MÉDIA DE IDADE do grupo.              - Quantas mulheres têm MENOS DE 20 anos.
#   - Qual é o nome do homem MAIS VELHO
#
#

print('Este programa irá ler o NOME, IDADE e SEXO de 4 pessoas, e fazer uma ANÁLISE COMPLETA.')

média1 = 0
qnt_m = 0
veio = 0
for c in range(1,5):
    nome = input(f'Digite o nome da {c}_a pessoa: ').strip()
    sexo = input('Agora, digite o seu sexo: ').strip().upper()
    ida_ = input('Por fim, a sua idade: ').strip()
    idade = int(ida_)

    média1 += idade

    p = [nome,sexo,idade]
    if c == 1 and sexo == 'MASCULINO':
        veio = nome
        idade_veio = idade
    elif sexo == 'MASCULINO' and idade > idade_veio:
        veio = nome
        idade_veio = idade
    if sexo == 'FEMININO' and idade <= 20:
        qnt_m += 1

média = média1 / 4

print(f'A quantidade de mulheres que possuem MENOS(ou) de 20 anos é de: {qnt_m} pessoa(s)')
print(f'O nome do HOMEM MAIS VELHO é {veio}, e ele possui {idade_veio} anos.')
print(f'A média de idade do grupo é de {média} anos de vida.')