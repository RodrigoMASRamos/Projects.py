pço = (float(input('Digite o preço de um produto: R$ ')))
pcntg = (pço/100) * 5
dcnt = pço - pcntg
print(f'O produto de R${pço:.2f} reais, com 5% de desconto, sairá por R${dcnt:.2f} reais.')