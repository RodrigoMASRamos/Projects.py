#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Digite a quantidade de números pedida e eu lhe mostrarei qual deles é o maior!')
# Tive problemas com esse exercício e só consegui resolve-lo com a resolução. Estude mais!
a = input('Primeiro valor: ').strip()
b = input('Segundo valor: ').strip()
c = input('Terceiro valor: ').strip()
a = float(a)
b = float(b)
c = float(c)
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor número é {menor:.2f}')
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é {maior:.2f}')
