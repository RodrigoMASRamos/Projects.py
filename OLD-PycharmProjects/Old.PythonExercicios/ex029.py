velocidade = float(input('Qual é a velocidade atual do carro?'))
qntrs = (velocidade - 80.00)*7.00
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deverá pagar R${qntrs:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança!')
#velocidade = float(input('Qual é a velocidade atual do carro?'))
#    multa = (velocidade - 80.00) * 7.00
#    if velocidade > 80:
#        print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
#        print(f'Você deverá pagar R${multa:.2f}')
#    else:
#        print('Tenha um bom dia! Dirija com segurança!')