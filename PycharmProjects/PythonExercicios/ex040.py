# Exercício Python #040 - Aquele clássico da Média
#
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
#
#       - Média abaixo de 5.0: REPROVADO.upper()
#       - Média entre 5.0 e 6.9: RECUPERAÇÃO.upper()
#       - Média 7.0 ou superior: APROVADO

print('\033[1;30mEste programa irá ler as \033[1;34mduas notas \033[1;30mde um aluno e \033[1;30mcalcular '
      '\033[1;30ma sua média, revelando se ele será \033[1;32maprovado, \033[1;31mretido, \033[1;30mou se ficará de '
      '\033[1;33mrecuperação.\033[m')

n1_ = input('\033[0;30mDigite o valor da \033[1;34mprimeira nota: \033[m').strip()
n2_ = input('\033[0;30mAgora, digite o valor da \033[1;34msegunda nota: \033[m').strip()

n1 = float(n1_)
n2 = float(n2_)
m = (n1 + n2) / 2

if m < 5.0:
    print(f'\033[0;30mInfelizmente, o aluno tirou uma média \033[1;31mABAIXO DE 5.0 pontos ({m:.1f})\033[0;30m, e por '
          f'isto será \033[1;31mREPROVADO.\033[m')

elif m > 5.0 and m < 6.9:
    print(f'\033[0;30mO aluno teve um \033[1;33mbaixo rendimento, \033[0;30mmas como teve uma \033[1;33mmédia entre 5.0'
          f' e 6.9 pontos ({m:.1f})\033[0;30m, ele está de \033[1;33mRECUPERAÇÃO.\033[m')

else:
    print(f'\033[0;30mO aluno teve uma média \033[1;32mMAIOR \033[0;30mdo que \033[1;32m7.0 pontos ({m:.1f}) '
          f'\033[0;30me foi \033[1;32mAPROVADO\033[0;30m. \033[4;30mMeus parabéns!!!\033[m')