# Exercício Python #048 - Soma ímpares múltiplos de três
#
# Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram no
# intervalo de 1 até 500

sum = 0
cont = 0

for x3 in range(3,500,3):
    if x3 % 2 != 0:
        sum += x3 # No Python é a mesma coisa que Variavel = Variavel + 1
        cont += 1 # No Python é a mesma coisa que Variavel = Variavel + 1

print("\033[0;31m\/\/\033[0;31m" * 20)
print(f'\033[0;30mA soma é de todos os \033[1;31m{cont} \033[0;30mvalores requisitados é igual a \033[1;31m{sum}'
      f'\033[0;30m.\033[m')
print("\033[0;31m\/\/\033[m" * 20)


