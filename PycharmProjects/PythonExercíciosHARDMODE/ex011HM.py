# ex011:  Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de
# tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

print('\033[1;30mEste programa lhe mostrará a quantidade de tinta necessária para pintar uma parede.\033[m')
l1str = input('\033[0;30mDigite a largura de uma parede: \033[m').strip()
l2str = input('\033[0;30mDigite a altura desta mesma parede: \033[m').strip()

l1 = float(l1str)
l2 = float(l2str)
a = l1 * l2
q = a / 2

print('\033[0;34m-=-=-=-\033[m' * 12)
print(
    f'\033[0;30mPara pintar uma parede com área de \033[4;36m{a}m²\033[0;30m, você precisará de \033[4;36m{q} litros '
    f'de tinta.')
print('\033[0;34m-=-=-=-\033[m' * 12)
