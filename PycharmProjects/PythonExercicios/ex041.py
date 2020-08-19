# Python Exercício #041 - Classificando Atletas
#
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
#       - Até 9 anos: MIRIM.upper()
#       - Até 14 anos: INFANTIL.upper()
#       - Até 19 anos: JUNIOR.upper()
#       - Até 25 anos: SÊNIOR.upper()
#       - Acima: MASTER.upper()

from datetime import date

print('\033[1;30mEste programa irá ler o ano do nascimento de um atleta e mostrará a sua categoria, de acordo com a '
      'idade.\033[m')
a_ = input('\033[0;30mDigite o \033[0;34mano de nascimento \033[0;30mdo \033[0;36matleta: \033[m').strip()
a = int(a_)
aa = date.today().year
i = aa - a

if i <= 9:
    print(f'\033[0;30mComo o \033[0;36matleta \033[0;30mnasceu em \033[0;36m{a} \033[0;30me em \033[0;36m{aa} '
          f'\033[0;30mele possui \033[0;36m{i} \033[0;30manos de vida,ele é classificado como um \033[0;34matleta MIRIM'
          f' por ter \033[0;36m9 anos de idade \033[0;30mou menos.\033[m')
elif i <= 14:
    print(f'\033[0;30mComo o \033[0;36matleta nasceu em \033[0;34m{a} \033[0;30me em \033[0;34m{aa} \033[0;30mele '
          f'possui \033[0;34m{i} anos de vida, \033[0;30mele é classificado como um \033[0;36matleta INFANTIL\033[0;30m'
          f' por ter entre \033[0;34m9 e 14 anos de idade.\033[m')
elif i <= 19:
    print(f'\033[0;30mComo o \033[0;36matleta nasceu em \033[0;34m{a} \033[0;30me em \033[0;34m{aa} '
          f'\033[0;30mele possui \033[0;34m{i} anos de vida, \033[0;30mele é classificado como um \033[0;36matleta '
          f'JUNIOR \033[0;30mpor ter entre \033[0;34m14 e 19 anos de idade. \033[m')
elif i <= 25:
    print(f'\033[0;30mComo o \033[0;36matleta \033[0;30mnasceu em \033[0;34m{a} \033[0;30me em \033[0;34m{aa} '
          f'\033[0;30mele possui \033[0;34m{i} anos de vida, \033[0;30mele é classificado como um '
          f'\033[0;36matleta SÊNIOR \033[0;30mpor ter entre \033[0;34m19 e 25 anos de idade.\033[m')

else:
    print(f'\033[0;30mComo o \033[0;36matleta nasceu em \033[0;34m{a} \033[0;30me em \033[0;34m{aa} \033[0;30mele '
          f'possui \033[0;34m{i} anos de vida,\033[0;30mele é classificado como um \033[0;36matleta MASTER '
          f'\033[0;30mpor ter mais de \033[0;34m25 anos de idade.\033[m')
