#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quando dólares ela pode comprar.
#Considere US$1,00 = R$3,27
v1 = float(input('Quantos reais você tem? R$ '))
v2 = v1 / 3.27
print(f'Com R$ {v1:.2f}, você pode comprar US$ {v2:.2f}')