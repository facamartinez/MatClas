#for lets you iterate a fixed amount of times

unaCadena = "esta es una cadena de texto"

for letter in unaCadena:
    print(letter)

def isVocal(letter):
    vocales = "aeiou"
    return letter in vocales

for letter in unaCadena:
    if not isVocal(letter):
        print(letter)

'''The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.'''

for x in range(6):
    print(x)


'''for anidados'''
'''mostrar la combinatoria de las letras de dos cadenas de caracteres'''

cadena1 = "1234"
cadena2 = "5678"

for l1 in cadena1:
    for l2 in cadena2:
        print(l1+l2)

isMultiplo = lambda y,z: y%z==0

def cantidadMultiplos(a,b):
    cantidad = 0
    for x in range(1,b):
        if isMultiplo(x,a):
            cantidad += 1
    return cantidad

print(cantidadMultiplos(4,100))