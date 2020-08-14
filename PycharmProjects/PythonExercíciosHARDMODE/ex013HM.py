# ex013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
print(f'\033[1;30mEste algorítimo irá ler o salário de um funcionário e mostrar'
      f' o seu novo salário, com 15% de aumento.\033[m')
sstr = input('\033[0;30mDigite o salário do atual do funcionario: R$ \033[m').strip()

s = float(sstr)
am = (15/300) * s
st = s + am

print('\033[0;32m-=-=-=-\033[m' * 11)
print(f'\033[0;30mO novo salário do funcinário, com \033[4;32m15% de aumento \033[1;32m(R$ {am})\033[0;30m,é de: '
      f'\033[1;32mR$ {st}\033[0;30m.\033[m')
print('\033[0;32m-=-=-=-\033[m' * 11)
