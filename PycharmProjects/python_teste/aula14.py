'''
c = 1
while c < 10: # Até a onde eu entendi, o 10° passo é justamente a interrupção.
    print(c)
    c = c + 1 # Chamamos isso de contador.
print('Fim')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')
