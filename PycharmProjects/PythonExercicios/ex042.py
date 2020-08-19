# Exercício Python #042 - Analisando Triângulos v2.0
# Refaça o DESAFIO 35.upper() dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#       - EQUILÁTERO: Todos os lados iguais
#       - ISÓSCELES: Dois lados iguais
#       - ESCALENO: Todos os lados diferentes

print('\033[0;35m-==-\033[m' * 25)
print('\033[1;30mDigite o valor pedido de três retas e eu lhe direi se elas podem ou não formar um triângulo!\033[m')
print('\033[1;30mAlém disso, eu lhe direi se é um triângulo \033[1;32mEQUILÁTERO, \033[1;33mISÓSCELES \033[0;30mou '
      '\033[1;31mESCALENO!\033[m')
print('\033[0;35m-==-\033[m' * 25)

r1 = input('\033[0;30mDigite o comprimento da primeira reta (ignore a unidade de medida): ').strip()
r2 = input('Agora, digite o comprimento da segunta reta: ').strip()
r3 = input('Mais uma vez, digite o comprimento da terceira reta: \033[m').strip()

r1 = float(r1)
r2 = float(r2)
r3 = float(r3)

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print(f'\033[0;30mAs retas \033[1;34m{r1}, {r2}, {r3} \033[0;32mPODEM SIM \033[0;30mformar um triângulo!\033[m')
    if r1 == r2 and r2 == r3: # Também vale r1 == r2 == r3
        print('\033[0;30mA propósito, se trata de um triângulo \033[1;32mEQUILÁTERO (Todos os lados são iguais)'
              '.\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[0;30mO triângulo que será formado é um triângulo \033[1;33mISÓSCELES! (dois lados são iguais)'
              '.\033[m')
    else:
        print('\033[0;30mO triângulo que será formado é um triângulo \033[1;31mESCALENO! '
              '(Todos os lados são DIFERENTES)\033[m')

else:
    print(f'\033[1;31mInfelizmente, \033[0;30mas retas \033[0;34m{r1} , {r2}, {r3} \033[1;31mNÃO PODEM '
          f'\033[0;30mformar um triângulo...\033[m')
