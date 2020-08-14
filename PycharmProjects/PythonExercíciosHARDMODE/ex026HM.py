# ex026: Faça um programa que leia uma frase pelo teclado e mostre:
#    - Quantas vezes aparece a letra ‘A’
#    - Em que posição ela aparece a primeira vez
#    - Em que posição ela aparece a última vez

f = input('\033[1;30mDigite uma frase qualquer: \033[m').strip().lower()

print(f'\033[0;30mA letra \033[1;35m"A" \033[0;30maparece \033[0;36m{f.count("a")} \033[0;30mvezes.')

print(f'\033[0;30mA letra \033[1;35m"A" \033[0;30maparece pela \033[4;34mPRIMEIRA \033[0;30mvez na '
      f'\033[0;36m{f.find("a") + 1}° \033[0;30mposição.')

print(f'\033[0;30mA letra \033[1;35m"A" \033[0;30maparece pela \033[4;34mULTIMA \033[0;30mvez na '
      f'\033[0;36m{f.rfind("a") + 1}° \033[0;30mposição.') # O .rfind() é igual ao .find() normal, mas no sentido
                                                           # "right", ou seja, começa de tras pra fente
                                                           #(direita para a esquerda)


