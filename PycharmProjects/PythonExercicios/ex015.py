#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
d = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Por quantos quilômetros você rodou com o carro? '))
p1 = d * 60
p2 = km * 0.15
pt = p1 + p2
print(f'Você deverá pagar R${pt:.2f}')