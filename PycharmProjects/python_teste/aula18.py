'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')  # Não é necessário colocar o nome da lista porque o laço já está
    # dentro da variável composta.
'''

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado)
    dado.clear() # Limpa os valores guardados na lista
print(galera)