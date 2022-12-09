# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250.00,calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.
slro = float(input('Digite salário de quem receberá o aumento: '))
if slro > 1.250:
    amt = (10/100)*slro
    slrott = amt + slro
    print(f'Como o seu salário é superior a R$1.250, o seu aumento será de R$ {amt}, ganhando assim, R$ {slrott}')
else:
    amt = (15*slro)/100
    slrott = amt + slro
    print(f'O seu aumento será de R$ {amt}, ganhando assim, R$ {slrott}')