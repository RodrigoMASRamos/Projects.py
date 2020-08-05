#ex008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
print('\033[1;30mEste programa converterá o valor que você digitar em metros para outras unidades de medida.\033[m')
mstr = input('\033[1;34mDigite o valor em métros, porém sem a unidade de medida (sem o "m" no final): \033[m')
m = float(mstr)
cm = m * 100
mm = m * 1000
print('\033[0;36m-=-=-=\033[m' * 10)
if m == 1.0:
    print(f'\033[0;34mO valor de \033[4;30m{m} metro\033[0;34m em \033[4;30mcentímetros\033[0;34m é de \033[4;30m{cm:.2f}cm.\033[m')
    print(f'\033[0;34mO valor de \033[4;30m{m} metro\033[0;34m em \033[4;30mmilímetros\033[0;34m é de \033[4;30m{mm:.2f}mm.\033[m')
    print('\033[0;36m-=-=-=\033[m' * 10)
if m >= 2:
    print(
        f'\033[0;34mO valor de \033[4;30m{m} metros\033[0;34m em \033[4;30mcentímetros\033[0;34m é de \033[4;30m{cm:.2f}cm.\033[m')
    print(
        f'\033[0;34mO valor de \033[4;30m{m} metros\033[0;34m em \033[4;30mmilímetros\033[0;34m é de \033[4;30m{mm:.2f}mm.\033[m')
    print('\033[0;36m-=-=-=\033[m' * 10)