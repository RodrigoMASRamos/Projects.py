# ex034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#
#           -   Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#           -   Para os inferiores ou iguais, o aumento é de 15%.


print('\033[1;30mEste programa irá \033[1;34mcalcular \033[1;30mo \033[1;32maumeto \033[1;30mdo salário de um '
      'funcionário.\033[m')
s_ = input('\033[0;30mDigite o \033[1;30mvalor atual \033[0;30mdo \033[1;32msalário '
           '\033[0;30mdo funcionário: \033[1;30mR$').strip()

s = float(s_)
if s <= 1250: #CUIDADO! Lembre-se que o .PONTO funciona como VIRGULA, e esse era o erro de lógica desse programa.
    amt = (15 / 100) * s
    st = s + amt
    print(f'\033[0;30mComo o \033[1;32msalário \033[0;30mdo funcionário é \033[1;31mINFERIOR \033[0;30mou igual a '
          f'\033[1;32mR$1.250,00 (R${s:.2f})\033[0;30m, o novo \033[1;32msalário \033[0;30mterá 15% de '
          f'\033[1;32maumento(R${amt:.2f}), \033[0;30me será de '
          f'\033[1;32mR${st:.2f}')
else:
    amt = (10 / 100) * s
    st = s + amt
    print(f'\033[0;30mComo o \033[1;32msalário \033[0;30mdo funcionário é \033[1;36mSUPERIOR a '
          f'\033[1;32mR$1.250,00 (R${s:.2f})\033[0;30m, o novo \033[1;32msalário \033[0;30mterá 10% de '
          f'\033[1;32maumento(R${amt}), \033[0;30me será de '
          f'\033[1;32mR${st:.2f}')

