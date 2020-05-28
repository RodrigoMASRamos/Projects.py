# Termo Geral da P.G
#n = posição
#q = razão
#a= termo
#An0 = A(n-1)
# Razão= q = An / An0
#        q = An / A(n-1)
#Termo geral da PG:
#                   An = A1*q^n-1

import math
An = float(input('Digite o número do termo: '))
n = int(input('Agora, digite a posição desse mesmo termo: '))
An0 = float(input('Por fim, digite o termo antecessor a esse: '))
q = An / An0
print(f'A razão equivale a:{q}.')
