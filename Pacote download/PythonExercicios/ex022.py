#Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas e minúsculas.
#   - Quantas letras ao todo(sem considerar espaços).
#   - Quantas  letras tem o primeiro nome.
nome = input('Digite o seu nome: ').strip()
nome1 = nome.split()
print(len(nome1)
print('Desconsiderando os espaços desnecessários, seu nome é',nome,'e possui ',len(nome),'letras')
print('O seu nome escrito por completo com letras MAIÚSCULAS É:',nome.upper())
print('O seu nome escrito por completo com letras minúsculas é:',nome.lower())