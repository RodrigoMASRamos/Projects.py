km = float(input('Quantos Km o carro alugado andou?'))
d = int(input('Por quantos dias ele foi alugado?'))
prckm = km * 0.15
prcd = d * 60
prct = prckm + prcd
print(f'O total a ser pago é de R$ {prct:.2f}')