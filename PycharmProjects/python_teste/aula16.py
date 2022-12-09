# () <- Tupla (opcional)
# [] <- Lista
# {} <- Dicionário
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2:])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) # Note que exibiu em LISTA
print(lanche)

print(lanche.index('Suco'))