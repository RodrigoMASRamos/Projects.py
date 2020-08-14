# ex031: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

# Obs: Esse programa foi MODIFICADO em relação ao enunciado original. A resolução do CeV pode não ser como esta...

print('\033[1;30mEste programa irá ler o \033[1;32mpreço \033[1;30mde uma passagem, cobrando até \033[1;32mR$0,50 '
      '\033[1;30mpor km de viagens de '
      '\033[1;34m200km \033[1;30me \033[1;32mR$0,45 \033[1;30mpara cada kilômetro adicional.')
d_ = input('\033[0;30mDigite a distância da viagem: \033[m').strip()
d = float(d_)
if d < 200:
    p = d * 0.50
    print(f'\033[0;30mComo a distância da viagem\033[0;34m({d}km) \033[0;30mé \033[1;36minferior \033[0;30ma '
          f'\033[0;34m200 km, \033[0;30mo '
          f'\033[0;32mpreço \033[0;30mda passagem será igual a \033[1;32mR${p:.2f}\033[0;30m.')
else:
    p1 = 200 * 0.50
    p2 = (d - 200) * 0.45
    p = p1 + p2
    print(f'\033[0;30mJá que a distância da viagem\033[0;34m({d}km) \033[0;30mé \033[1;31mmaior \033[0;30mdo que '
          f'\033[0;34m200 km, \033[0;30mo \033[0;32mpreço \033[0;30mda passagem será igual a '
          f'\033[1;32mR${p:.2f}\033[0;30m.')