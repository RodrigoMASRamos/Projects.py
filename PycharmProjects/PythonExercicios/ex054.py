# Exercício Python #054 - Grupo da Maioridade
#
# Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
#
# Obs: Considere a maioridade como 21

from datetime import date

print('Este programa irá ler o ANO DE NASCIMENTO de SETE PESSOAS. No final, ele mostrará quantas pessoas ainda NÃO'
      ' atingiram a maioridade e QUANTAS JÁ são maiores.')
ano_a = date.today().year
t_maior = 0
t_menor = 0

for c in range(1,8):
    ano = str(input(f'Digite o ANO DE NASCIMENTO da {c}_a pessoa: ')).strip()
    ano_ = int(ano)
    age = int(ano_a - ano_)
    if age >= 21:
        print(f'Essa pessoa é MAIOR de idade, pois possui {age} anos.')
        t_maior += 1
    else:
        print(f'Essa pessoa é MENOR de idade, pois possui {age} anos.')
        t_menor += 1
    print(' '*20)
print(f'No total, há {t_menor} pessoas menores de idade e {t_maior} pessoas maiores de idade.')
