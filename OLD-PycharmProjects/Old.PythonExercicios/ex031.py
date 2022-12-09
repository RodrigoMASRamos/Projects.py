#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
#Km para viagens de até 200km e R$0,45 para viagens mais longas.
km = float(input('Quantos quilômetros terá a viagem?'))
if km < 200:
    ppkm = 0.50
    print(f'O preço de sua viagem será de R${km*ppkm}')
else:
    ppkm = 0.45
    print(f'O preço de sua viagem será de R${km*ppkm}, com desconto de R$0,5 centavos por ser uma viagem longa.')