# Desafio 065 - Maior e Menor valores
#
# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os
# valores e qual foi o MAIOR e o MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# CONTINUAR a digitar valores.
''' CÓDIGO CONTABILIZANDO O FLAG

#Esse código ficou assim porque não teve um "input" com str para parar.
menor = maior = acum = cont = num = 0
while num != -1: # Meu código estava certo, mas não consegui evitar o flag no while, por isso ele está aqui...
    num = int(input('Digite um número qualquer. Digite -1 para parar: '))
    cont += 1
    acum += num
    if num > maior and num > menor:
        maior = num
    elif menor > num and maior > num:
        menor = num
média = acum / cont
print(f'A média entre todos os {cont} valores digitados é {média}, sendo {maior} o maior valor, '
      f'e {menor} o menor valor.')'''

'''CÓDIGO DEFEITUOSO

acum = cont = num = 0
maior = menor = 0
s_n = ''
while s_n != 'N':
    num = int(input('Digite um número qualquer: '))
    s_n = str(input('Deseja continuar [S/N]? ')).strip().upper()
    cont += 1
    acum += num
    if num > maior and num > menor:
        maior = num
    elif num < menor and num < maior:
        menor = num  # O problema desse código está aqui. "Se o num for menor que o menor, então num vira o menor.
média = acum / cont  # Mas isso nunca acontecerá, porque lá no começo, zero é o menor valor.
print(f'A média entre todos os {cont} valores digitados é {média}, sendo {maior} o maior valor, '
      f'e {menor} o menor valor.')
''' # Código defeituoso

acum = cont = num = 0
maior = menor = 0
s_n = ''
while s_n != 'N':
    num = int(input('Digite um número qualquer: '))
    s_n = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if num > maior and num >= menor:
        maior = num
    if cont == 0: # elif NÃO FUNCIONA aqui, e caga o código. Descubra o porquê!
        menor = maior
    elif num < menor and num <= maior:
        menor = num
    print(cont)
    cont += 1
    acum += num
    print(cont)
média = acum / cont
print(f'A média entre todos os {cont} valores digitados é {média}, sendo {maior} o maior valor, '
      f'e {menor} o menor valor.')

''' CÓDIGO GUANABARA

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
        núm = int(input('Digite um número: '))
        soma += núm
        quant += 1
        if quant == 1:
            maior = menor = num
        else:
            if núm > maior:
                maior = núm
            if núm < menor:
                menor = núm
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print(f'Você  digitou {quant} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
''' #Código do Prof° Guanabara
