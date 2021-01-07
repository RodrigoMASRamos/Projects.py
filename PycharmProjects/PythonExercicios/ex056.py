# Exercício Python #056 - Analisador completo
#
# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre:
#   - A MÉDIA DE IDADE do grupo.              - Quantas mulheres têm MENOS DE 20 anos.
#   - Qual é o nome do homem MAIS VELHO
#

print('Este programa irá ler o NOME, IDADE e SEXO de 4 pessoas, e fazer uma ANÁLISE COMPLETA.')

média_ = 0
mais_velho = ''
idade_velho = 0
qnt_m = 0
for c in range (1,5):
    print(f'------ {c}ᵃ PESSOA ------')
    nome = input('Nome: ').strip()
    idade_ = input('Idade: ').strip()
    idade = int(idade_)
    sexo = input('Sexo: ').strip().capitalize()
    print(nome,idade,sexo)

    média_ += idade

    if c == 1 and sexo == 'Masculino':
        mais_velho = nome
        idade_velho = idade
    elif idade > idade_velho and sexo == 'Masculino':
        mais_velho = nome
        idade_velho = idade
    if sexo == 'Feminino' and idade <= 20:
        qnt_m += 1

média = float(média_ / 4)

print(f'A média da idade do grupo é de {média:.2f} anos.')
print(f'O nome do HOMEM MAIS VELHO é {mais_velho}, e sua idade é igual a {idade_velho} anos.')
print(f'A quantidade de mulheres com MENOS de 20 anos é igual a {qnt_m}.')


''' CÓDIGO ANTIGO (C/BUG)
média_ = 0
qnt_m = 0
veio = 0
for c in range(1,5):
    print(f'------ {c}° PESSOA ------')

    nome = input(f'Digite o nome da {c}_a pessoa: ').strip()
    ida_ = input('Agora, a sua idade: ').strip()
    sexo = input('Por fim, digite o seu sexo: ').strip().upper()
    idade = int(ida_)

    média_ += idade

    p = [nome,sexo,idade]
    if c == 1 and sexo == 'MASCULINO':
        veio = nome
        idade_veio = idade
    elif sexo == 'MASCULINO' and idade > idade_veio:
        veio = nome
        idade_veio = idade
    else:
        veio = "zero"
        idade_veio = 0
    if sexo == 'FEMININO' and idade <= 20:
        qnt_m += 1

média = média_ / 4

print(f'A quantidade de mulheres que possuem MENOS(ou) de 20 anos é de: {qnt_m} pessoa(s)')
print(f'O nome do HOMEM MAIS VELHO é {veio}, e ele possui {idade_veio} anos.')
print(f'A média de idade do grupo é de {média} anos de vida.')
'''