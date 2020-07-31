# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#
# Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza
'''Tive dificuldades com a ultima linha desse código. Estude mais a função Split e a aula 9!'''
nome = input('Digite um nome completo: ').strip()
n = nome.split()
print(f'O seu primeiro nome é {n[0]}')
print(f'Já o seu ultimo nome é {n[len(n)-1]}')