'''cont = 1
while True: # Nesta fatídica condição, o While será executado ETERNAMENTE! Somente o break poderá para-lo!
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

# TESTANDO BREAK COM IF DE FLAG

n =s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
