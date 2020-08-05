# ex010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$ 1,00 = R$ 3,27

dr_ = input(
    '\033[1;30mDigite quanto dinheiro uma pessoa tem na carteira e este programa irá dizer quantos dólares ela pode '
    'comprar (considerando o dólar em R$ 3,27): R$ \033[m').strip()

dr = float(dr_)
d = dr / 3.27

# print(d)

print('\033[0;36m-=-=-=-\033[m' * 12)

if dr <= 0 or dr <= 3.26:
    print(
        f'\033[0;31mInfelizmente, a pessoa não possui dinheiro suficiente para comprar \033[1;31mnenhum dólar :/\033[m')
if d == 1.0:
    print(f'\033[0;30mA pessoa poderá comprar \033[1;32m{d} dólar.\033[m')
if d > 1.0:
    print(f'\033[0;30mA pessoa poderá comprar \033[1;32m{d} dólares.\033[m')

print('\033[0;36m-=-=-=-\033[m' * 12)
