# Exercício Python #053 - Detector de Palíndromo
#
# Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.
#   Ex:
#       APOS A SOPA
#       A SACADA DA CASA
#       A TORRE DA DERROTA
#       O LOBO AMA BOLO
#       ANOTARAM A DATA DA MARATONA
# OBS: Eu não fazia IDEIA de como resolver esse exercicio *COM LAÇOS. Estude MUITO mais tratamento de String e os
# laços for.
# Para fins auto-didáticos, esse exercício NÃO estará colorido. Terá APENAS anotações (MUITAS ANOTAÇÕES).
# Tente fazer o exercício novamente e ESCREVA suas dúvidas e poste em um fórum.
# EDIT: PROBLEMA DE APRENDIZADO ENCONTRADO: ESTUDE MAIS O "JOIN"!!!
#
# SOLUÇÃO COMENTADA do Prof° Gustavo Guanabara:

frase = str(input ('Digite uma frase: ')).strip().upper # .strip() removera os espaços excedentes no final
                                                        # .upper() jogará todas as letras para o CAPS LOCK
# (isso é necessário para a comparação final.
palavras = frase.split()
junto = ''.join(palavras) # É UM METODO. Entre as aspas, está especificado O QUE juntará as listas e, entre (),
# qual lista será alvo do método
inverso = '' # Note que o espaço está vazio. Isso ocorre porque o laço formará a frase ao contrário
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra] # Letra é a variavel do for. Os numeros correspondentes vão selecionar letras.
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

'''
Abaixo segue o MACETE DE FATIAMENTO EM PYTHON do professor Gustavo Guanabara:

frase = str(input ('Digite uma frase: ')).strip().upper
palavras = frase.split()
junto = ''.join(palavras)
inverso = 'junto[::-1]'
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

'''