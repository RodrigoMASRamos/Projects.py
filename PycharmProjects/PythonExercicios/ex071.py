# Desafio 071 - Simulador de Caixa Eletrônico
#
# Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO. No início, pergunte ao usuário qual será o VALOR
# A SER SACADO(número inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão entregues
#
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
#
# NOTA: Exercício bem dificil... Não fazia ideia de como resolver. Treine ele mais!
# PS: O código permanece com bugs.

''' CÓDIGO ANTIGO E DEFEITUOSO 1

print('-=-' * 20)
print('Caixa eletrônico!')
print('-=-' * 20)

cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_01 = 0
valor = float(input('Digite o valor a ser sacado: R$'))

while True:
    if valor % 50 == 0:
        cont_50 = valor / 50
        valor = valor // 50
        print(f'Total de {cont_50} cédulas de R$50,00')
        break
    if valor % 20 == 0:
        cont_20 = valor / 20
        valor = valor // 20
        print(f'Total de {cont_20} cédulas de R$20,00')
    if valor % 10 == 0:
        cont_10 = valor / 10
        valor = valor // 10
        print(f'Total de {cont_10} cédulas de R$10,00')
    if valor % 1 == 0:
        cont_01 = valor / 1
        valor = valor // 1
        print(f'Total de {cont_01} cédulas de R$50,00')
    else:
        break
'''
# Tentei fazer o rastreamento no código acima, mas pela longa pausa não funcionou. De agora em diante, prometa a si
# mesmo que sempre fara o rastreamento com um máximo de três dias!

print('-=-' * 20)
print('Caixa eletrônico!')
print('-=-' * 20)

valor = float(input('Digite o valor a ser sacado: R$ '))
nota = 50

while True:
    if valor > nota:  # É importante NOMEAR uma variável por ser um LAÇO
        # print(f'O VALOR na função PRINT da linha 56 é {valor}, enquanto a NOTA é {nota}.')
        qnt_nota = valor // nota
        # print(f'A variável QNT_NOTA da linha 57 é {qnt_nota}')
        valor = valor % nota
        # print(f'A variável VALOR da linha 59 é {valor}.')

        print(f'O total de cédulas de R${nota:.2f} é igual a {int(qnt_nota)}.')
    else:  # O else é utilizado aqui (NÃO o IF ou ELIF) pelo bloco ser feito por condições INVERSAS.
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        if nota == 1 and valor < 10:  # Problema com essa linha de pensamento: O valor 131, por exemplo, não funciona.
            valor = valor - nota
            qnt_nota += 1
    qnt_nota = 0
    if valor == 0:
        break
'''
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''  # Código Guanabara

# Códigos dos alunos dos comentários [ATUALIZDO EM x/x/2021]
