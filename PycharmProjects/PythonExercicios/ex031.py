#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
#Km para viagens de até 200km e R$0,45 para viagens mais longas.
d = input('Digite a distância da viagem em Km. Após isso, lhe informarei o preço da passagem: ').strip()
d = float(d)
if d > 200:
    Sbase = 200 * 0.45
    Stotal = Sbase
    print(f'O preço total (incluindo o adicional) necessário a ser pago é de R${Stotal:.2f}')
else:
    Sbase = d * 0.50
    print(f'O preço total necessário a ser pago é de R${Sbase:.2f}')