# Exercício Python #039 - Alistamento Militar
#
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele AINDA VAI SE
# ALISTAR ao serviço militar, se é a HORA DE SE ALISTAR ou se já PASSOU DO TEMPO do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Tive dificuldades para realizar esse exercício. Estude mais!
# Além disso, o código ficou complexo demais. A resolução contem dicas importantes, REFAÇA esse exercício ANTES do
# Hard Mode

from datetime import date

print('Este programa irá ler o ano de nascimento de um jovem e informar se ele ainda irá se alistar, se é hora de se '
      'alistar ou se o prazo para o alistamento já passou.')

a_ = input('Digite o ano de nascimento do jovem: ').strip()

a = int(a_)
aa = date.today().year
i = aa - a
t = (i - 18) * 1

if aa - a == 18:
    print('É HORA DE SE ALISTAR! O jovem completou 18 anos, e deve servir as forças armadas!')

elif aa - a < 18:
    print(f'Ainda não chegou a hora de se alistar. O jovem em questão é muito novo ({i}), e ainda faltam {t * -1} anos '
          f'para o alistamento')
elif aa - a > 18:
    print(f'O prazo para se alistar já passou há {t} anos, e o jovem daquele tempo tem hoje {i} anos de vida.')
