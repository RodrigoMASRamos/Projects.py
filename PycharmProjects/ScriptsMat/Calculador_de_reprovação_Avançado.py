# Desenvolva um programa que leia a média dos 4 bimestres de um aluno e diga se ele já passou de ano ou não.

média_1s = 0
média_2s = 0
for n in range (1,5):
    nota_ = input(f'Digite a nota de sua média no {n}° bimestre (caso ainda não saiba a nota, digite "0"): ').strip()
    nota = float(nota_)

    if n == 1 or n == 2:
        nota_p = nota * 2
        média_1s += nota_p

    elif n == 3 or n == 4:
        nota_p = nota * 3
        média_2s += nota_p

    else:
        print('ERRO! DE ALGUMA FORMA, O NÚMERO DO LAÇO É DIFERENTE DE 1-4!')
media_t = média_1s + média_2s

if media_t >= 60:
    print(f'Parabéns! Você já passou de ano nesta matéria! '
          f'\nIsso porque no 1° semestre você obteve um total de {média_1s}, e no 2° Semestre você obteve um total de '
          f'{média_2s}!'
          f'\nAo realizar a soma, a nota total foi {media_t}(>=60!)')
else:
    print(f'Infelizmente, você ainda não passou de ano nesta matéria... '
          f'\nIsto porque no 1° semestre você obteve um total de {média_1s}, e no 2° Semestre você obteve um total '
          f'de {média_2s}.'
          f'\nAo realizar a soma, a nota total foi {media_t} ( < 60).')
    print(' ' * 40)
    _resto = 60 - media_t
    x = _resto / 3
    print(f'Mas nada de tristeza! Para passar de ano, basta tirar {x} pontos como nota!')
