# Desafio 059 - Criando um Menu de Opções
#
# Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
#
#   [1] somar
#   [2] multiplicar
#   [3] maior
#   [4] novos números
#   [5] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
#
# OBS: Tive dificuldade em resolver esse exercício (EM especial com a opção "5"). Estude mais!
#
# PS: O programa foi quanto aos tipos primitivos.

''' CÓDIGO ANTIGO E DEFEITUOSO

op = ''
v1 = int(input('Digite o Primeiro Valor: '))
v2 = int(input('Digite o Segundo Valor: '))
while op != 5: # O "5" aqui está sendo lido como NÚMERO
    print('Operações a serem realizadas')
    print(''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    '')
    op = input('Digite o valor da operação desejada: ') # O "5" aqui, caso seja digitado, é lido como STR pelo input
print('Programa Finalizado.')                           # (AO MENOS QUE SEJA ESPECIFICADO O CONTRÁRIO!)

# O programa não estava sendo executado corretamente porcausa da DIFERENÇA dos tipos primitivos das variáveis!'''

""" CÓDIGO ANTIGO MAS PRECISA DO INPUT PARA O WHILE NÃO SER REPETIDO INFINITAMENTE
v1_ = input('Digite um valor inteiro qualquer: ').strip()
v2_ = input('Digite o segundo valor inteiro: ').strip()
v1 = int(v1_)
v2 = int(v2_)

op = int(input('''Escolha a operação a ser realizada:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Digite o valor correspondente aqui: '''))
while op != 5:
    if op == 1:
        soma = v1 + v2
        print(f'A soma de {v1} e {v2} é igual a {soma}.')
        op = int(input('Deseja sair do programa ou realizar outra operação? Digite o número correspondente: '))
    if op == 2:
        multiplicação = v1 * v2
        print(f'A multiplicação entre {v1} e {v2} é igual a {multiplicação}.')
        op = int(input('Deseja sair do programa ou realizar outra operação? Digite o número correspondente: '))
    if op == 3:
        maior = v1
        if v2 > v1:
            maior = v2
        print(f'Ente {v1} e {v2}, o MAIOR número é {maior}.')
        op = int(input('Deseja sair do programa ou realizar outra operação? Digite o número correspondente: '))
    if op == 4:
        v1_ = input('Digite um NOVO valor inteiro: ').strip()
        v2_ = input('Digite o segundo valor inteiro: ').strip()
        v1 = int(v1_)
        v2 = int(v2_)

        op = int(input('''Escolha a operação a ser realizada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa

        Digite o valor correspondente aqui: '''))
print('Encerrando o programa...')
""" # CÓDIGO ANTIGO, MAS PRECISA DO INPUT PARA O WHILE NÃO SER REPETIDO INFINITAMENTE

from time import sleep
v1_ = input('Digite um valor inteiro qualquer: ').strip()
v2_ = input('Digite o segundo valor inteiro: ').strip()
v1 = int(v1_)
v2 = int(v2_)
op = 0
while op != 5: # Para previnir o problema do código anterior ("While" infinito sem input em cada "if"), o input está
               # DENTRO DA ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO.
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''') # O uso de três aspas simples dispensa indetação.
    print('-==-' * 10)
    op_ = str(input('Digite o número da opção a ser realizada: '))
    op = int(op_)
    if op == 1:
        print(f'A soma de {v1} + {v2} é igual a {v1 + v2}')
    elif op == 2:
        print(f'A multiplicação entre {v1} e {v2} é igual a {v1 * v2}.')
    elif op == 3:
        if v1 > v2:
            maior = v1
            print(f'Entre {v1} e {v2}, o maior número é {maior}!')
        elif v2 > v1:
            maior = v2
            print(f'Entre {v1} e {v2}, o maior número é {maior}!')
        else:
            print(f'Os números {v1} e {v2} são iguais!')
    elif op == 4:
        v1_ = input('Digite um NOVO valor inteiro qualquer: ').strip()
        v2_ = input('Digite o segundo NOVO valor inteiro: ').strip()
        v1 = int(v1_)
        v2 = int(v2_)
        op = 0
    else:
        print('Encerrando o Programa...')
        sleep(3)
print('Programa finalizado.') # Aparentemente, o programa está perfeito. MAS eu faria mais alguns testes.

""" CÓDIGO GUANABARA
    from time import sleep
    
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    opção = 0
    while opção != 5:
        print('''    [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    opção = str(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: ))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
""" # Código do Prof° Gustavo Guanabara!
