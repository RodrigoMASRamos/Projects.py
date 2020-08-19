# Exercício Python #044 - Gerenciador de Pagamentos
#
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE
# PAGAMENTO:
#
#   - À vista DINHEIRO/CHEQUE:
#   10% de desconto
#
#   - À vista no CARTÃO: 5% de      # Em até 2x NO CARTÃO: Preço normal     # 3x OU MAIS no cartão: 20% de juros
#   desconto

print('Este programa irá calcular o valor a ser pago por um produto, considerando o seu preço normal e '
      'condição de pagamento')

print('\033[1;33m-==-\033[m' * 5,'\033[1;34m|LOJAS PYTHON|\033[m','\033[1;32m-==-\033[m' * 5)
# print('{:-==^10}'.format('|LOJAS PYTHON|')) # Por algum motivo, esta linha de código não funciona como na resolução

p_ = input('\033[1;30mDigite o preço das compras: \033[1;32mR$\033[m').strip()
print('\033[0;30mQual é a \033[1;34mforma de pagamento \033[0;30mque deseja? \033[m')
print('\033[1;30m-==-\033[m' * 15)

# É possivel economizar prints com 3 aspas dentro do comando.
print('''\033[0;30mFORMAS DE PAGAMENTO\033[m                        
\033[0;33m[1] \033[0;30m| À vista no DINHEIRO/CHEQUE com 10% de desconto.
\033[0;32m[2] \033[0;30m| À vista no CARTÃO com 5% de desconto.
\033[0;33m[3] \033[0;30m| Em até 2x no CARTÃO.
\033[0;32m[4] \033[0;30m| Em até 3x ou mais no cartão com 20% de juros.''')
print('\033[1;30m-==-\033[m' * 15)
op_ = input('\033[0;30mPor favor, digite o número da opção desejada: \033[m').strip()

p = float(p_)
op = int(op_)

if op == 1:
    d = (10/100) * p
    v = p - d
    print(f'\033[0;30mCom esta opção de pagamento, você terá \033[0;32m10% de desconto(R${d:.2f})! \033[0;30mNo total,'
          f' o valor de sua compra será de: \033[0;32mR${v:.2f}')

else:
    if op == 2:
        d = (5/100) * p
        v = p - d
        print(f'\033[0;30mCom esta opção de pagamento, você terá \033[0;32m5% de desconto(R${d:.2f})! '
              f'\033[0;30mNo total, o valor de sua compra será de: \033[0;32mR${v:.2f}')
    elif op == 3:
        parcela = p / 2
        print(f'\033[0;30mCom esta opção de pagamento, você pagará pelo \033[1;30mpreço normal da compra, '
              f'\033[0;30misto é, \033[0;32mR${p:.2f}\033[m')
        print(f'\033[0;30mSua parcela será de \033[0;32mR${parcela:.2f}\033[m')
    elif op == 4:
        j = (20 / 100) * p
        v = p + j
        nparc = int(input('\033[0;30mEm quantas parcelas deseja pagar? \033[m'))
        parcela = v / nparc
        print(f'\033[0;30mCom esta opção de pagamento, você pagará pela compra com uma taxa de \033[1;31m20% de '
              f'juros({j:.2f}). \033[0;30mO total do valor da compra será de \033[1;32mR${v:.2f}')
        print(f'\033[0;30mSua compra será parcelada em \033[0;34m{nparc}x, \033[0;30me cada parcela será de '
              f'\033[1;32mR${parcela:.2f}')

if op != 1 and op != 2 and op != 3 and op != 4:
    print('\033[1;31mERRO! Tente novamente, opção inválida de pagamento.\033[m')
