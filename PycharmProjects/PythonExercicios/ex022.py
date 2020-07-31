#Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas e minúsculas.
#   - Quantas letras ao todo(sem considerar espaços).
#   - Quantas  letras tem o primeiro nome.
name = str(input('Digite o seu nome:').strip())
print('O seu nome com todas as letras maiúsculas é',name.upper()+'.')
print('Já o seu nome com todas as letras minúsculas é',name.lower()+'.')
print('O seu nome completo possui', len(name) - name.count(' '), 'letras')
print('Já o seu primeiro nome possui',name.find(' '),'letras')