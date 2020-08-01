# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250.00,calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.
slr = float(input('Digite o valor do seu salário do funcionário e eu calcularei o aumento: R$'))
if slr > 1250:
    amnt = (10 / 100) * slr
    slrN = amnt + slr
    print(f'O novo salário será de R${slrN:.2f}.')
else:
    amnt = (15 / 100) * slr
    slrN = amnt + slr
    print(f'Dadas as condições, o novo salário será de R${slrN:.2f}.')