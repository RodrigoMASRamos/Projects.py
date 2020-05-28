from random import shuffle
print("""Olá Majestade! Você é um glorioso e famoso Rei,
e seu conselheiro está prestes a decidir dentre quatro pessoas,
a ordem dos camponeses que falarão com você.""")
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto e o ultimo nome: '))
lista = [n1, n2, n3, n4]
ordem = shuffle(lista)
print(f'O seu confiável conselheiro estabeleceu a seguinte ordem: {ordem} .')


