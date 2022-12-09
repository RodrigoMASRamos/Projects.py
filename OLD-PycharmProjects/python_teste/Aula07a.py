n1 = int(input('Um valor: '))
n2 = int(input('Mais um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto vale {}, \n e a divisão vale {:.3f}'.format(s, m, d), end = '---')
print('a divisão inteira vale {}, e a potência é {}'.format(di, e))