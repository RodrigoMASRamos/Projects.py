# Desafio 064 - Tratando vários valores v1.0
#
# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles
# (desconsiderando o flag).

num = 0
qnt_num = 0
s = 0
while num < 999:
    num = int(input('Digite o valor de um número qualquer (ou 999 para sair do programa): '))
    qnt_num = qnt_num + 1
    s = num + s
    if num == 999: # Foi o jeito que eu encontrei para contornar o problema da flag, mas deve haver uma forma melhor.
        s = s - num
        qnt_num -= 1
print(f'Foram digitados {qnt_num} números, e a soma de todos eles é igual a {s}')


''' CÓDIGO GUANABARA

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
''' # CÓDIGO GUANABARA