from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você quiser: '))
sin = float(sin(radians(ang)))
cos = float(cos(radians(ang)))
tan = float(tan(radians(ang)))
print (f'O ângulo {ang:.2f} tem o seno de {sin:.2f}, o cosseno de {cos:.2f} e a tangente de {tan:.2f}. Tudo isso em radianos. ')

