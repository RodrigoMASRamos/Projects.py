#ex003: Crie um programa que leia dois números e mostre a soma entre eles

'''
n1 = input('\033[1;30mDigite um número: \033[m').strip()
n1 = float(n1)
n2 = input('\033[1;30mAgora, digite outro número: \033[m').strip()
n2 = float(n2)
s = n1 + n2
print(f'\033[0;30mA soma de \033[1;36m{n1}\033[0;30m e \033[1;34m{n2}\033[0;30m é igual a \033[1;32m{s}\033[m.')
''' # HardMode v1.0

cont = 0
som = 0
num_num = int(input('Quantos números deseja digitar?'))
for c in range(1, num_num+1): # Lembre-se que ele IGNORA o último valor
    num = float(input('Digite um número qualquer: '))
    cont += 1
    som += num
print(f'Ao todo, foram digitados {cont} valores, e a soma de todos eles é igual a {som}')
print('FIM DO PROGRAMA')
