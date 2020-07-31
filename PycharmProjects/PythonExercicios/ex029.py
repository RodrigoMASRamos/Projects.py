#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele ]
#foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
vcar = input('Digite a velocidade do carro em km. Se ele ultrapassar 80 km/h, será multado: ').strip()
vcar = float(vcar)
vlim = float(80)
if vcar > vlim:
    vt = vcar - vlim
    multa = float(vt * 7)
    print(f'Sinto muito, infelizmente você terá de pagar uma multa de R${multa:.2f}')
else:
    print('Muito bem, você está dentro do limite...')
