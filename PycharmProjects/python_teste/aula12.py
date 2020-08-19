# Obs: O codigo abaixo diferiu(não em lógica de algorítmos abordados) um pouco do que foi abordado em aula para fins
# de entretenimento e homenagens ;)

# \033[m

n = str(input('Digite seu nome: ')).strip()
if n == 'Rodrigo':
    print('Criador do código detectado, seremos eternamente gratos!')
elif n in 'Santa Santo':        # Possuo uma duvida com este código, ela estará anotada logo abaixo.
                                # Nota: Aparentemente, não é necessário especificar o "== True", pois o Python
                                # considera isso por padrão.
    print('Venerável Santo(a)!')
elif n == 'Joana' or n == 'Terezinha' or n == 'Bento' or n == 'Pio':
    print('Oh, bem aventurado servo(a) de Deus!')
elif n == 'Gustavo Guanabara':
    print('Mestre do meu criador!')
else:
    print(f'{n} é o seu nome? Meh...')


'''
DÚVIDA, LINHA 9:

Não pude deixar de notar que, na linha 9, caso eu escreva 

    elif n in 'Santa Santo':
 
 O programa irá aplicar o "in" tanto para a palavra Santa como para a palavra Santo, ainda que estejam(aparentemente) 
 na mesma cadeia de caracteres
 
 MAS ISSO NÃO OCORRE CASO EU INVERTA A ORDEM! Como em:
 
    elif 'Santa Santo' in n
    
Se eu não me engano, o comando é executado(não possui erro de sintaxe), mas não funciona corretamente. A pergunta é:

POR QUE?
'''