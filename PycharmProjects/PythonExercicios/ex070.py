# Desafio 070 - Estatísticas em produtos
#
# Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa deverá perguntar se o USUÁRIO vai continuar.
# No final, mostre:
#
#   A) Qual é o TOTAL GASTO na compra.
#   B) Quantos produtos custam MAIS de R$1000.
#   C) Qual é o NOME do produto mais BARATO.

tot_gasto = 0
qnt_1000 = 0
barato = ''
preço_barato = 0
print('===' * 10)
print('LOJA "CURSO DA PECHINCHA"')
print('===' * 10)
while True:
    nome = input('Digite o nome do produto: ').strip()
    preço = float(input('Digite seu preço: R$'))
    if tot_gasto == 0:
        preço_barato = preço
        barato = nome
    tot_gasto += preço
    if preço < preço_barato:
        preço_barato = preço
        barato = nome
    elif preço > 1000.00:
        qnt_1000 += 1
    resp = input('Deseja continuar?[S/N]: ').capitalize().strip()[0]
    if resp == 'N':
        break
print(f'No total, foram gastos R${tot_gasto}')
print(f'Há {qnt_1000} produtos que custam MAIS de R$1000')
print(f'O produto mais barato é {barato}, e seu preço é igual a R${preço_barato}')