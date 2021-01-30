# Desafio 067 - Tabuada v3.0
#
# Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário.
# O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.

while True:
    num_ = str(input('Digite um número inteiro para ver sua tabuada (ou um número negativo para parar): ')).strip()
    if '-' in num_:
        break
    num = int(num_) # Abaixo, esqueci como formatar para a esquerda hehehe
    print(f'''    {num} x {1} = {num * 1} 
    {num} x {2} = {num * 2}
    {num} x {3} = {num * 3}
    {num} x {4} = {num * 4}
    {num} x {5} = {num * 5}
    {num} x {6} = {num * 6}
    {num} x {7} = {num * 7}
    {num} x {8} = {num * 8}
    {num} x {9} = {num * 9}
    {num} x {10} = {num * 10}''')
print(f'PROGRAMA ENCERRADO! O valor digitado ({num_}) é negativo.')
