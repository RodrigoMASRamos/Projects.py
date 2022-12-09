'''

num = [2, 5, 9, 1]
num[2] = 3 # O elemento que ocupa a segunda posição "9" passa a ser o número 3
num.append(7) # O elemento "7" foi adicionado ao final da lista
num.sort(reverse=True) # A ordem da lista mudou: Agora ela é armazenada de trás para frente
num.insert(2, 0) # O tamanho da lista aumentou, pois o número "0" foi inserido na 2da posição
num.pop(2) # O elemento que ocupava a posição 2 foi removido. Tratava-se do "0".
print(num) # A lista "num" é exibida na tela
print(f'Essa lista tem {len(num)} elementos.') # A quantidade de elementos é exibida na tela.
'''
'''
valores = []
for contador in range(0, 5):
    valores.append(int(input('Digite um valor: '))) # É possível utilizar a função input dentro de .append(), bem como
                                                    # dentro de outras funções
for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')
'''

a = [2, 3, 4, 7]
# b = a # Listas ligadas por referência. Qualquer modificação em uma alterará ambas
b = a[:]  # Assim como no fatiamento, recebeu uma CÓPIA de todos os itens de a, pois tanto o inicio como o fim não
# estão especificados.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
