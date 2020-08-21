# Glosáriozinho:
# for = para
# Variavél c  que pode ser chamada de qualquer nome, e se eu entendi bem, ela é o *proprio laço*.
# range(x,y) = indica o intervalo da repetição
# Nota: NÃO SE ESQUEÇA DOS DOIS PONTOS FINAIS! ( :)
'''for c in range(0,6): # Começa no 0, caso contrário, irá realizar o comando apenas 5x. Ele meio que ignora o ultimo num.
    print('Oi')
    print(c) # Será "printada" a prórpia estrutura, iniciando a contagem dos intervalos com a regra acima (# lin 6)
             # Caso eu queira "inverter" a contagem, adicionar -1.
                    # Exemplo: for c in range(0, 6, -1)
print('FIM Teste 1')
print('Além disso, você pode com essa estrutura também indicar os espaços a serem pulados:')
for c1 in range(0, 7, 2):
    print('Viu só?')'''

# Também pode ser usada uma outra variavel (desde que seja um número) no limite do comando range. Exemplo:
numero_inicial = int(input('Digite um número inteiro qualquer: '))
numero_final = int(input('Agora, digite um outro numero: '))
numero_passos = int(input('Digite mais um número: '))

for c2 in range(numero_inicial, numero_final, numero_passos):
    print(c2)
    # Pode-se utilizar inputs também

