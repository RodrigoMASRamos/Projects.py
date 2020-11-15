# Exercício Python #049 - Tabuada v.2.0
#
# Refaça o DESAFIO 009.upper(), mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um
# LAÇO FOR.

count = 0
n = str(input('\033[0;30mDigite um número inteiro qualquer, e o computador lhe mostrará a sua tabuada: \033[m')).strip()
n = int(n)
for x in range(0,11):
    print(f'{n:2} x {count:2} = {n * count:2}')
    count += 1
print('Foi. Deu certo?')

# Também é valido o jeito do Professor Gustavo Guanabara, como está abaixo. O exemplo abaixo explora melhor a
# variavel de controle:
'''for x in range(0,11):
    print(f'{n:2} x {x} = {n * x:2}')'''