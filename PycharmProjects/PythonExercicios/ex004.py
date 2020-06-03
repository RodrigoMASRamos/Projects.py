#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
#sobre ele.
b = input('Digite *qualquer* coisa: ')
print('O tipo primitivo é:', type(b))
print('Só tem espaços?',b.isspace())
print('É um número?',b.isnumeric())
print('É alfabetico?',b.isalpha())
print('É alfanumérico?',b.isalnum())
print('Está escrito em MAIUSCULAS?',b.isupper())
print('Está escrito em minusculas?',b.islower())
print('Está Captalizado?',b.istitle())

