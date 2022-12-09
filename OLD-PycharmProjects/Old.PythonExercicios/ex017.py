from math import hypot
co = float(input('Digite o valor do primeiro cateto: '))
ca = float(input ('Digite o valor do segundo cateto: '))
hi = hypot(co, ca)
print(f'A Hipotenusa será igual a {hi:.2f}')
