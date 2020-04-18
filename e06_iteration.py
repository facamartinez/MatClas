# encoding: utf-8
import sys
# Usando el método items()
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}

for k, v in caballeros.items():
    print (k, v)

for v in caballeros.keys():
    print(v)

for v in caballeros.values():
    print(v)


# Usando la función enumerate()
for i, v in enumerate(['ta', 'te', 'ti']):
    print (i, v)



# Usando la función zip()
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']

for p, r in zip(preguntas, respuestas):
    print ('Cual es tu {0}?  {1}.'.format(p, r))

# Usando la función reversed()
for i in reversed(range(1, 10, 2)):
    print (i)

# Usando la función sorted()
canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
sorted(canasta)
canasta.sort()
for f in sorted(set(canasta)):
    print (f)
print (canasta)


NATI