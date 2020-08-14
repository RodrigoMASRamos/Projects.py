#ex027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#   primeiro = Ana
#   último = Souza
n = input('\033[1;30mDigite o nome completo de uma pessoa: \033[m').strip()
print(f'\033[1;36m{n}, \033[0;30mque nome bonito!\033[m')
ns = n.split()
print(f'\033[0;30mO seu primeiro nome é \033[1;35m{ns[0]}.\033[m')
print(f'\033[0;30mJá o seu último nome é \033[1;35m{ns[len(ns) - 1]}.\033[m')
# Em uma lista, len() irá mostrar as posições, enquanto o - 1
# fará com que será mostrada somente a ultima posição.

# A lógica do código esta correta, mas não compreendi direito a linha 9...