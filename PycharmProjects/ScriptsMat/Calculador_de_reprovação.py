# Este programa irá LER as notas do bimestre, e dizer se você já passou de ano ou não

tot = 0
for n in range (1,5):
    b_ = input(f'Digite o valor da sua nota no {n}° bimestre (coloque "0" caso ainda não saiba a nota): ').strip()
    b = float(b_)
    tot += b

print(' ' * 20)
if tot >= 24:
    ex = tot - 24
    print(f'Por tirar no total {tot} pontos de nota, você passou de ano nesa matéria, meus parabéns!\n'
          f'Além disso, você tirou uma nota em excesso de {ex} pontos!')
else:
    print(f'Infelizmente, você ainda NÃO passou de ano nessa matéria, pois tirou uma nota total inferior a '
          f'24...({tot} pontos)')