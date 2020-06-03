#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
v1 = float(input('Digite o preço do produto: R$ '))
descnt = (5 / 100) * v1
v2 = v1 - descnt
print('Com um desconto de 5%, o produto teria um valor de: R$',v2)
