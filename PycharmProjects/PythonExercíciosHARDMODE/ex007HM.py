# ex007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
print('\033[1;32mEste programa lerá as duas notas de um aluno e irá mostrar a média.\033[m')
n1s = input('\033[0;30mDigite a primeira nota: \033[m').strip()
n2s = input('\033[0;30mAgora, digite a segunda nota: \033[0;30m')
n1 = float(n1s)
n2 = float(n2s)
# print(len('A média das notas 20.0 e 10.0 é 15.0'))
print('\033[0;32m=-=-=-\033[m' * 6)
print(f'\033[0;30mA média das notas \033[1;34m{n1}\033[0;30m e \033[1;34m{n2} \033[0;30mé \033[1;36m{(n1 + n2) / 2}'
      f'\033[m')
print('\033[0;32m=-=-=-\033[m' * 6)
