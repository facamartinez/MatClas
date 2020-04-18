from Class_4.e02_for import isVocal

entero = 1

while entero <= 10:
    print("Iterando por {entero} vez".format(entero=entero))
    entero += 1

print(isVocal("a"))

'''Serie fibonacci'''

def fib(n):    # escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print (b),
        a, b = b, a+b


fib(50)


def cantidadMultiplos(a,b):
    cantidad = 1
    multiplo = a+a
    while multiplo < b:
       cantidad += 1
       multiplo += a
    return cantidad

print(cantidadMultiplos(4,100))