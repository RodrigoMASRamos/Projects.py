# Exercício Python #036 - Aprovando Empréstimo
#
# Escreva um programa para aprova o empréstimo bancário para a compra de uma casa. Pergunte o VALOR DA CASA, o SALÁRIO
# do comprador e em QUANTOS ANOS ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

c_ = input('Digite o valor da casa que deseja comprar: R$').strip()
s_ = input('Agora, digite o valor do seu salário: R$').strip()
a = int(input('Em quantos anos deseja pagar a casa? '))

c = float(c_)
s = float(s_)

pst = c / (a * 12)
tpcs = (30 / 100) * s

print(f'Para pagar uma casa com o valor de R${c:.2f} em {a} anos, cada prestação terá o valor de R${pst:.2f}. ')
#o end = ' ' irá fazer com que a linha continue

if pst > tpcs:
    print(f'Sinto muito, mas como a prestação mensal excede 30% de seu salário(R${tpcs:.2f}), o empréstimo terá de ser '
          f'negado.')
else:
    print('O emprestimo foi aprovado com sucesso.')