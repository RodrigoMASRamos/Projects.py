# ex014: Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
print('\033[1;30mEste programa irá ler a temperatura digitada e ira converte-la.\033[m')
cstr = input('\033[0;32mDigite a temperatura em graus celsius: ')
c = float(cstr)
f = (9 * (c / 5)) + 32

print('\033[0;36m°.°.°.°.°.°' * 6)
print(f'\033[1;30m{c}°C \033[0;34mconvertidos em \033[1;30m°F \033[0;34mé igual a \033[1;30m{f}°F.')
print('\033[0;36m°.°.°.°.°.°' * 6)
