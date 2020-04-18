'''escribir un programa que tome 4 parametros y encuentre el menor numero entre los 4'''

"Opcion 1"

def minimo(parametro1,parametro2,parametro3,parametro4):
    lista = [parametro1,parametro2,parametro3,parametro4]
    return min(lista)
'''print(minimo(1,2,3,4))'''



"Opcion 2"
def minim(para1,para2,para3,para4):
    if para1<para2:
        if para1<para3:
            if para1<para4:
                return para1
            return para4
    if para2<para3:
        if para2<para4:
            return para2
        return para4
    elif para3<para4:
        return para3
    return para4

'''print(minim(1,2,3,4))
print(minim(1,4,1,1))
print(minim(2,4,1,1))
print(minim(2,1,1,3))
print(minim(3,4,1,2))
print(minim(3,1,1,4))
print(minim(4,2,1,1))
print(minim(4,2,1,1))'''


'''escribir un programa que dado un año diga si es bisiesto. Los años son bisiestos cuando
Año bisiesto es el divisible entre 4, salvo que sea año secular -último de cada siglo, terminado en «00»-
, en cuyo caso también ha de ser divisible entre 400.
'''

def bisiestoSecular(ano):
    divPorCuatro = ano%4
    divPorCien = ano%100
    divPorCuatrocientos= ano%400
    if divPorCien==0:
        if divPorCuatrocientos == 0:
            return "Bisiesto"
        return "Secular"
    if divPorCuatro == 0 and not divPorCien == 0:
        return "Bisiesto"
    else:
        return "Metetelo en el ANO"

'''
print(bisiestoSecular(1994))
print(bisiestoSecular(1996))
print(bisiestoSecular(1998))
print(bisiestoSecular(2000))
print(bisiestoSecular(2100))
print(bisiestoSecular(2200))
'''

'''Escribir un programa que, considerando que el primero de enero es Lunes, dado un número de dia del año (entre 1 y 365) calcule que
dia de la semana es.'''

def diaDeLaSemana(dia):
    dias = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
    return dias[(dia%7)]

'''print(diaDeLaSemana(1))
print(diaDeLaSemana(2))
print(diaDeLaSemana(3))
print(diaDeLaSemana(4))
print(diaDeLaSemana(5))
print(diaDeLaSemana(6))
print(diaDeLaSemana(7))'''

'''​ Utilizar​ ​ el​ ​ programa​ ​ del​ ​ ejercicio​ ​ 2 ​ ​ de​ ​ la​ ​ clase​ ​ 3 ​ ​ para​ ​ generar​ ​ una​ ​ tabla​ ​ de​ ​ conversión​ ​ de
temperaturas,​ ​ desde​ ​ 0◦F​ ​ hasta​ ​ 120​ ​ ◦F,​ ​ de​ ​ 10​ ​ en​ ​ 10.'''

def fahrenheitACelsius(F):
    return ((F-32)*5/9)


'''print("F","\t\t"," C")'''
for x in range(0,121,10):
    fahrenheitACelsius(x)
    '''print(x,"  \t",float(round(fahrenheitACelsius(x),1)))'''




'''Escribir​ ​ un​ ​ programa​ ​ que​ ​ imprima​ ​ por​ ​ pantalla​ ​ todas​ ​ las​ ​ fichas​ ​ de​ ​ dominó,​ ​ de​ ​ una​ ​ por
línea​ ​ y ​ ​ sin​ ​ repetir.'''

for x in range(1,7,1):
    for y in range(1,7,1):
        ''' print(x,y)'''



'''Escribir​ ​ un​ ​ programa​ ​ que​ ​ reciba​ ​ como​ ​ entrada​ ​ un​ ​ entero​ ​ representando​ ​ un
año​ ​ (por​ ​ ejemplo​ ​ 751,​ ​ 1999,​ ​ o ​ ​ 2158),​ ​ y ​ ​ muestre​ ​ por​ ​ pantalla​ ​ el​ ​ mismo​ ​ año​ ​ escrito​ ​ en​ ​ números
romanos'''

enteros = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
romanos = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
n=0
romano=""
anio=int(input("Anio: "))
while anio>0:
    if anio-enteros[n]>=0:
        anio=anio-enteros[n]
        romano=(romano)+(romanos[n])
    else:
        n= n + 1
print(romano)




'''Escribir​ ​ un​ ​ programa​ ​ que​ ​ le​ ​ pida​ ​ al​ ​ usuario​ ​(utilizar la funcion input) que​ ​ ingrese​ ​ una​ ​ sucesión​ ​ de​ ​ números
naturales​ ​ (primero​ ​ uno,​ ​ luego​ ​ otro,​ ​ y ​ ​ así​ ​ hasta​ ​ que​ ​ el​ ​ usuario​ ​ ingrese​ ​ ’-1’​ ​ como​ ​ condición​ ​ de
salida).​ ​ Al​ ​ final,​ ​ el​ ​ programa​ ​ debe​ ​ imprimir​ ​ cuántos​ ​ números​ ​ fueron​ ​ ingresados,​ ​ la​ ​ suma​ ​ total
de​ ​ los​ ​ valores​ ​ y ​ ​ el​ ​ promedio.'''

'''
numero=(int(input("Numero: ")))
suma=0
n=0
while numero!=-1:
    suma=suma+numero
    n=n+1
    promedio=suma/n
    numero=(int(input("Numero: ")))

print(str("numeros: ") + n)
print(str("suma: ") + suma)
print(str("promedio: ") + promedio)

'''

'''a)​ ​ Escribir​ ​ una​ ​ función​ ​ que​ ​ devuelva​ ​ la​ ​ suma​ ​ de​ ​ todos​ ​ los​ ​ divisores​ ​ de​ ​ un​ ​ número​ ​ n ​ ​ , ​ ​ sin
incluirlo.
    b)​ ​ Usando​ ​ la​ ​ función​ ​ anterior,​ ​ escribir​ ​ una​ ​ función​ ​ que​ ​ imprima​ ​ los​ ​ primeros​ ​ m ​ ​ números
tales​ ​ que​ ​ la​ ​ suma​ ​ de​ ​ sus​ ​ divisores​ ​ sea​ ​ igual​ ​ a ​ ​ sí​ ​ mismo​ ​ (es​ ​ decir​ ​ los​ ​ primeros​ ​ m ​ ​ números
perfectos).
    c)​ ​ Usando​ ​ la​ ​ primera​ ​ función,​ ​ escribir​ ​ una​ ​ función​ ​ que​ ​ imprima​ ​ las​ ​ primeras​ ​ m ​ ​ parejas
de​ ​ números​ ​ ( ​ ​ a ​ ​ , ​ ​ b ​ ​ ),​ ​ tales​ ​ que​ ​ la​ ​ suma​ ​ de​ ​ los​ ​ divisores​ ​ de​ ​ a ​ ​ es​ ​ igual​ ​ a ​ ​ b ​ ​ y ​ ​ la​ ​ suma​ ​'''


def facadivisor(numero):
    suma = 0
    divisor = 1
    for x in range(0,(numero-1),1):
        if numero%divisor == 0:
            suma = suma+divisor
            divisor = divisor+1
        else:
            divisor = divisor+1
    print(suma)
print(facadivisor(int(input("inserte numero: "))))

#def divisoresIgualANum(m):
 #   for x in range(0,m,1):
  #      if facadivisor(x) == x:
   #         print(x)
#print(divisoresIgualANum(10))


''' ​ Escribir​ ​ funciones​ ​ que​ ​ dada​ ​ una​ ​ cadena​ ​ de​ ​ caracteres:
a)​ ​ Imprima​ ​ los​ ​ dos​ ​ primeros​ ​ caracteres.
    b)​ ​ Imprima​ ​ los​ ​ tres​ ​ últimos​ ​ caracteres.
    c)​ ​ Imprima​ ​ dicha​ ​ cadena​ ​ cada​ ​ dos​ ​ caracteres.​ ​ Ej.:​ ​ 'recta'​ ​ debería​ ​ imprimir​ ​ 'rca'
d)​ ​ Dicha​ ​ cadena​ ​ en​ ​ sentido​ ​ inverso.​ ​ Ej.:​ ​ 'hola​ ​ mundo!'​ ​ debe​ ​ imprimir​ ​ '!odnum​ ​ aloh'
e)​ ​ Imprima​ ​ la​ ​ cadena​ ​ en​ ​ un​ ​ sentido​ ​ y ​ ​ en​ ​ sentido​ ​ inverso.​ ​ Ej:​ ​ 'reflejo'​ ​ imprime
'reflejoojelfer'​ ​ .'''



'''​ ​ ​ Escribir​ ​ funciones​ ​ que​ ​ dada​ ​ una​ ​ cadena​ ​ y ​ ​ un​ ​ caracter:
a)​ ​ Inserte​ ​ el​ ​ caracter​ ​ entre​ ​ cada​ ​ letra​ ​ de​ ​ la​ ​ cadena.​ ​ Ej:​ ​ 'separar'​ ​ y ​ ​ ','​ ​ debería​ ​ devolver
's,e,p,a,r,a,r'
b)​ ​ Reemplace​ ​ todos​ ​ los​ ​ espacios​ ​ por​ ​ el​ ​ caracter.​ ​ Ej:​ ​ 'mi​ ​ archivo​ ​ de​ ​ texto.txt'​ ​ y ​ ​ '_'
debería​ ​ devolver​ ​ 'mi_archivo_de_texto.txt'
c)​ ​ Reemplace​ ​ todos​ ​ los​ ​ dígitos​ ​ en​ ​ la​ ​ cadena​ ​ por​ ​ el​ ​ caracter.​ ​ Ej:​ ​ 'su​ ​ clave​ ​ es:​ ​ 1540'​ ​ y
'X'​ ​ debería​ ​ devolver​ ​ 'su​ ​ clave​ ​ es:​ ​ XXXX'
d)​ ​ Inserte​ ​ el​ ​ caracter​ ​ cada​ ​ 3 ​ ​ dígitos​ ​ en​ ​ la​ ​ cadena.​ ​ Ej.​ ​ '2552552550'​ ​ y ​ ​ '.'​ ​ debería​ ​ devolver
'255.255.255.0' '''


'''Escribir​ ​ una​ ​ función​ ​ que​ ​ reciba​ ​ una​ ​ cadena​ ​ que​ ​ contiene​ ​ un​ ​ largo​ ​ número​ ​ entero​ ​ y ​ ​ devuelva
una​ ​ cadena​ ​ con​ ​ el​ ​ número​ ​ y ​ ​ las​ ​ separaciones​ ​ de​ ​ miles.​ ​ Por​ ​ ejemplo,​ ​ si​ ​ recibe
'1234567890'​ ​ , ​ ​ debe​ ​ devolver​ ​ '1.234.567.890'​ ​ .'''