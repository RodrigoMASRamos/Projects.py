#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#
'''O exercício não especifica que a string precisa ser SILVA somente, e por isso, Silvanei seria validado como True.
Corri-ja isso no PythonExercíciosHARDMODE
Se precisar de uma dica, veja os comentários da resolução desse exercício no YT'''
#
n = input('Digite o nome completo de uma pessoa: ').strip().upper()
print('SILVA'in n)