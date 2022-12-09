# Desafio 073 - Tuplas com Times de Futebol
#
# Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da Tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de co-
# locação. Depois mostre:
#
#   A) Apenas os 5 PRIMEIROS colocados.
#   B) Os ÚLTIMOS 4 colocados da tabela.
#   C) Uma lista com os times em ORDEM ALFABÉTICA.
#   D) Em que POSIÇÃO na tabela está o time da CHAPECOENSE.

top20_brasileirao = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athetico Paranaense', 'Santos', 'São ' 
                    '  Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro',
                    'América Mineiro', 'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull '
                    'Bragantino')
print(f'No Campeonato Brasileiro de Futebol de 2022: ')
print(f'Os 5 primeiros colocados foram: {top20_brasileirao[:5]}')
print(f'Os últimos 4 colocados foram: {top20_brasileirao[-4:]}')
print(f'Os times em ordem Alfabética ficam ordenados dessa maneira: {sorted(top20_brasileirao)}')
print(f'O time {top20_brasileirao[16]} se classificou na {top20_brasileirao.index("Chapecoense") + 1}° posição')
