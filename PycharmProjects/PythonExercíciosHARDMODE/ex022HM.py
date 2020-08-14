# ex022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome.

# Tive diversas dificuldades com este exercício, em especial com a linha 12. A resposta é que dentro de mais
# de uma função no .format, não se pode utilizar(por algum motivo), as aspas simples, mas somente as aspas duplas.

n = str(input('\033[1;30mDigite o nome completo de uma pessoa: \033[m')).strip().lower()
print('\033[0;36m-=-=-=-' * 11)

a = n.count(' ')
b = len(n)
print(f'\033[0;30mO nome completo dessa pessoa em \033[1;36mMAIÚSCULAS \033[0;30mé: \033[0;34m{n.upper()}\033[0;30m.')
print(f'\033[0;30mO nome completo dessa pessoa em \033[1;31mminúsculas \033[0;30mé: \033[0;34m{n.lower()}\033[0;30m.')
print(f'\033[0;30mO nome escrito possui \033[1;35m{len(n)} \033[0;30mcaractéres, sendo que \033[1;35m{n.count(" ")}'
      f' \033[0;30msão espaços e \033[1;35m{len(n) - n.count(" ")} \033[0;30msão letras.')
print(f'\033[0;30mO primeiro nome desta pessoa possui \033[1;32m{n.find(" ")} \033[0;30mletras.')