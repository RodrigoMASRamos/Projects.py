# ex029: Escreva um programa que leia a velocidade de uma carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

print('\033[1;30mEste programa irá calcular o valor da \033[1;31mmulta \033[1;30mcaso o carro passe de determinada '
      '\033[1;33mvelocidade. \033[1;30mA multa custará \033[1;32mR$7.00 '
      '\033[1;30mpor cada Km acima do limite permitido.')
print('\033[0;36m-=-\033[m' * 50)
vc_ = input('\033[0;30mDigite a velocidade do carro: \033[m').strip()

vc = float(vc_)

if vc > 80:
    vcn = vc - 80
    mul = vcn * 7.00
    print(f'\033[1;31mMULTADO! \033[0;30mO carro ultrapassou a velocidade limite de \033[1;32m80 km/h, '
          f'\033[0;30me por isso, \033[0;31mlevará uma multa de \033[1;31mR${mul:.2f} '
          f'\033[0;30mpelos \033[1;32m{vcn:.2f}km/h \033[0;30mexcedentes... ╯︿╰')

else:
    print('\033[1;32mMuito bem! \033[0;30mO carro está na \033[1;32mvelocidade limite \033[0;30me \033[1;31mnão '
          '\033[0;30mserá multado! ヾ(￣▽￣) Boa~Viagem~\033[m')

