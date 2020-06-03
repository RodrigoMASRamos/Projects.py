#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
a = larg * alt
print(f'A área da parede {larg:.2f}x{alt:.2f} é de:{a:.2f}m²')
tinta = a / 2
print(f'Você precisará de {tinta:.2f} l de tinta para pintar a parede.')
