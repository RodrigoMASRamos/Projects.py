#Faça um programa que leia uma frase pelo teclado e mostre:
#    - Quantas vezes aparece a letra "A"
#    - Em que posição ela aparece a primeira vez.
#    - Em que posição ela aparece a última vez.
'''Por alguma razão, a linha de código a seguir não funciona... Descubra o porquê antes de prosseguir para o HARDMODE

        print(f'Na frase {f}, a letra "A" aparece {f.count('A')}','vezes.')
                                                                                                                '''
f = input('Digite uma frase qualquer: ').strip().upper()
A_in_f = f.count('A')
fst_A = f.find('A') + 1
ult_A = f[0:].rfind('A') + 1
print(f'A letra "A" aparece {A_in_f} vezes.')
print(f'A letra "A" aparece pela primeira vez na posição {fst_A}.')
print(f'A letra "A" aparece pela última vez na posição {ult_A}')
