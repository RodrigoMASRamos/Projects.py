#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
v1 = float(input('Digite o salário do funcionario: R$ '))
aumt = (15 / 100) * v1
v2 = v1 + aumt
print('Com um aumento de 15%, o salário do novo funcionario seria de: R$',v2)
