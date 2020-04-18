'''lets print only the multiples of a given number'''

def printMultiples(multiples,upToNumber=100):
    for x in range(1,upToNumber+1):
        if x%multiples == 0:
            print(x)



printMultiples(7)

'''imprimir las letras que no sean i y o'''

def excludeLetters(palabra,letters="io"):
    for letra in palabra:
        if letra in letters:
            continue
        print(letra)


cadena = "Pablito clavó un clavito, que clavito clavó pablito?"

excludeLetters(cadena,"afgw")

'''sumar impares de la primer cadena con pares de la segunda'''
cadena1 = "1234"
cadena2 = "5678"

even = lambda y:y%2==0

result = 0
for l1 in cadena1:
    l1 = int(l1)
    if even(l1):
        continue
    for l2 in cadena2:
        l2 = int(l2)
        #si el pri
        if not even(l2):
            continue
        result += l1+l2

print(result)