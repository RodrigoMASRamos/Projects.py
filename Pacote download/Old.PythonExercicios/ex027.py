n = str(input('Digite o seu nome completo: ')).strip()
print('Muito prazer em te conhecer,',n,'!')
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
