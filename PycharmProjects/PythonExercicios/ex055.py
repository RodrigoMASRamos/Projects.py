# Exercício Python #055 - Maior e menor da sequência
#
# Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lidos.
#
# Soube que precisava trabalhar com condicionais, mas eu não sabia como. Melhore seu raciocinio lógico!
#
# EDIT: Havia um problema de logico antigo se eu n abusasse dos ifs, descubra o motivo!

print('Este programa irá ler o PESO de CINCO PESSOAS, e no final, mostrará o MENOR e o MAIOR peso lidos.')

menor = 0
maior = 0
for c in range(1,6):
    p_ = str(input(f'Digite o valor do {c}° peso(substitua a vírgula pelo ponto): ')).strip()
    p = float(p_)
    if c == 1:
        menor = p
        maior = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O MENOR valor de peso digitado foi {menor}, enquanto o MAIOR foi {maior}.')