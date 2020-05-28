from random import choice
print('Agora, você irá digitar 4 nomes de Waifus que serão sorteadas! Pressione "Enter" para continuar. ')
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto e ultimo nome: '))
lista = [n1, n2, n3, n4]
escolhida = choice(lista)
print(f'Que rufem os tambores!E a escolhida é tum-tum-tum-tum... {escolhida}!!! ')