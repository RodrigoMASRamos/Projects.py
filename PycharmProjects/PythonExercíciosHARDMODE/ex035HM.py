# ex035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo
print('\033[0;32m-=-\033[m' * 20)
print('\033[1;30mEste programa irá calcular se \033[1;31m3 retas \033[1;30mpodem ou não formar um '
      '\033[1;32mtriângulo \033[1;30matravés dos seus \033[1;34mcomprimentos.\033[m')
print('\033[1;32m-=-\033[m' * 20)
r1_ = input('\033[0;30mDigite o valor da primeira reta: \033[m').strip()
r2_ = input('\033[0;30mDigite o valor da segunda reta: \033[m').strip()
r3_ = input('\033[0;30mDigite o valor da terceira reta: \033[m').strip()

r1 = float(r1_)
r2 = float(r2_)
r3 = float(r3_)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\033[0;30mCom estas retas, \033[0;31mÉ SIM \033[0;30mpossível formar um \033[1;32mtriângulo!')
else:
    print('\033[0;30mCom estas retas, infelizmente \033[0;31mNÃO É \033[0;30mpossível formar um \033[1;32mtriângulo...')