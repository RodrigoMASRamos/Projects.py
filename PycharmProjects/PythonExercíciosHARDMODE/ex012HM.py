# ex012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
print('\033[1;30mEste algoritmo irá ler o preço de um determinado produto e mostrar o seu novo peço, com 5% de desconto'
      '.\033[m')
print('\033[0;34m-=-=-=-\033[m' * 6)
pstr = input('\033[0;30mDigite o preço do produto: R$\033[m').strip()
p = float(pstr)
d = (5/100) * p
pt = p - d

print(f'\033[0;30mO desconto total será de \033[1;32mR${d:.2f}\033[m, \033[4;30mjá o preço com o desconto será de\033[m \033[1;32m{pt:.2f}.\033[m')
