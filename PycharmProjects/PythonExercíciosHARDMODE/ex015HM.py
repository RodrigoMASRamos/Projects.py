# ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15
# por Km rodado.
print('\033[1;30mEste programa irá ler a quantidade de Km percorridos e os dias que o carro foi alugado, para assim,'
      ' calcular o preço.\033[m')
print('\033[0;31m-=-=-=-=\033[m' * 20)

kmstr = input('\033[0;30mDigite a quantidade de km rodados: \033[m').strip()
dstr = input('\033[0;30mAgora, digite a quantidade de dias que o carro foi alugado: \033[m').strip()

km = float(kmstr)
d = int(dstr)
pkm = km * 0.15
pd = d * 60
pt = pd + pkm

print('\033[1;31m-=-=-=-=\033[m' * 20)
print(f'\033[0;30mA quantidade total a ser paga é de \033[1;32mR${pt:.2f}\033[0;30m, sendo 0\33[1;32mR${pkm:.2f} '
      f'\033[0;30mpelos \033[4;30mquilômetros rodados \033[0;30me \033[1;32mR${pd:.2f} \033[0;30mpor '
      f'\033[4;30mdias em que o carro foi alugado.')
print('\033[0;31m-=-=-=-=\033[m' * 20)