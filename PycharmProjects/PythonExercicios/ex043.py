# Exercício Python #043 - Índice de Massa Corporal
#
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC.upper() e mostre seu status, de
# acordo com a tabela abaixo:
#
#       - Abaixo de 18.5: Abaixo do Peso            - 25 até 30: Sobrepeso
#       - Entre 18.5 e 25: Peso ideal               - 30 até 40: Obesidade
#                                                   - Acima de 40: Obesidade mórbida

print('\033[1;30mEste programa irá calcular o \033[1;34mIMC \033[1;30mde uma pessoa com os dados de seu \033[1;36mpeso '
      '\033[1;30me \033[1;36maltura. \033[m')
print('\033[1;34m-=-\033[m' * 27)

p_ = input('\033[0;30mDigite o \033[1;36mpeso \033[0;30m(sem a unidade de medida): \033[m').strip()
a_ = input('\033[0;30mAgora, digite a \033[1;36maltura \033[0;30m(sem a unidade de medida): \033[m').strip()

p = float(p_)
a = float(a_)
IMC = p / (a ** 2)

print('\033[1;34m-=-\033[m' * 27)

if IMC < 18.5:
    print(f'\033[0;30mO \033[0;34míndice de massa corporal \033[0;30mdesta pessoa está \033[1;31mABAIXO DO PESO.'
          f'\033[0;30m Seu \033[0;34mIMC \033[0;30mé \033[1;34m{IMC:.1f}, \033[0;30msendo que o \033[0;36mpeso '
          f'\033[0;30mé de \033[0;36m{p}kg \033[0;30me a \033[0;36maltura \033[0;30mé de \033[0;36m{a}m.')

elif IMC >= 18.5 and IMC < 25:
    print(f'\033[0;30mEsta pessoa está em seu \033[1;32mpeso ideal, \033[4;30mmeus parabéns! \033[0;30mSeu '
          f'\033[1;34mIMC \033[0;30mé \033[1;34m{IMC:.1f}, \033[0;30msendo que o \033[0;36mpeso \033[0;30mé de '
          f'\033[0;36m{p}kg \033[0;30me a \033[0;36maltura \033[0;30mé de \033[0;34m{a}m.\033[m')

elif IMC >= 25 and IMC < 30:
    print(f'\033[0;30mO \033[1;34míndice de massa corporal \033[0;30mdesta pessoa está \033[1;32mACIMA DO PESO. '
          f'\033[0;30mSeu \033[1;34mIMC \033[0;30mé \033[1;34m{IMC:.1f}, \033[0;30msendo que o \033[0;36mpeso '
          f'\033[0;30mé de \033[0;36m{p}kg \033[0;30me a \033[0;36maltura \033[0;30mé de \033[0;36m{a}m.')

elif IMC >= 30 and IMC < 40:
    print(f'\033[0;31mInfelizmente, \033[0;30mesta pessoa apresenta \033[4;30mOBESIDADE. \033[0;30mSeu \033[1;34mIMC '
          f'\033[0;30mé \033[1;34m{IMC:.1f}, \033[0;30msendo que o \033[0;36mpeso \033[0;30mé de \033[0;36m{p}kg '
          f'\033[0;30me a \033[0;36maltura \033[0;30mé de \033[0;36m{a}m.\033[m')


else:
    print(f'\033[4;31mSinto muito,\033[0;30m mas \033[0;31minfelizmente, \033[0;30mesta pessoa apresenta '
          f'\033[1;31mOBESIDADE MÓRBIDA \033[0;30me corre \033[1;31mRISCO DE VIDA!'
          f' \033[0;30mSeu \033[1;34mIMC \033[0;30mé \033[1;34m{IMC:.1f}, \033[0;30msendo que o \033[0;36mpeso '
          f'\033[0;30mé de \033[0;36m{p}kg \033[0;30me a \033[0;36maltura \033[0;30mé de \033[0;36m{a}m.\033[m')
