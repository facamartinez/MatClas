'''Escribir una función que implemente el operador XOR del algebra de Boole'''

def xor(x,y):
    if x==True and y==True:
        return False
    elif x==False and y==False:
        return False
    else:
        return True

'''print(xor(bool(0),bool(0)))'''

def xor(x,y):
    if x and y:
        return False
    elif not x and not y:
        return False
    else:
        return True

'''print(xor(bool(0),bool(0)))'''



'''Escribir​ ​ un​ ​ programa​ ​ qu5e​ ​ le​ ​ pregunte​ ​ al​ ​ usuario​ ​ una​ ​ cantidad​ ​ de​ ​ pesos,​ ​ una​ ​ tasa​ ​ de​ ​ interés
y​ ​ un​ ​ número​ ​ de​ ​ años​ ​ y ​ ​ muestre​ ​ como​ ​ resultado​ ​ el​ ​ monto​ ​ final​ ​ a ​ ​ obtener.​ ​ La​ ​ fórmula​ ​ a ​ ​ utilizar
es:
Cn​ ​ = ​ ​ C ​ ​ × ​ ​ (1​ ​ + ​ ​ x/100)n
Donde​ ​ C ​ ​ es​ ​ el​ ​ capital​ ​ inicial,​ ​ x ​ ​ es​ ​ la​ ​ tasa​ ​ de​ ​ interés​ ​ y ​ ​ n ​ ​ es​ ​ el​ ​ número​ ​ de​ ​ años​ ​ a ​ ​ calcular.'''


'''pesos = int(input("capital a invertir:"))
interes = float(input("interes:"))
anios = float(input("años:"))'''
def raffi(pesos,interes,anios):
    return (pesos*(1+interes/100)**anios)
'''print(raffi(pesos,interes,anios))'''



def resultadoInversion(C,i,n):
    return (C*(1+i/100)**n)
'''print(resultadoInversion(int(input("capital a invertir:")),int(input("Tasa de interes:")),int(input("Años a colocar:"))))
'''


'''Escribir​ ​ un​ ​ programa​ ​ que​ ​ convierta​ ​ un​ ​ valor​ ​ dado​ ​ en​ ​ grados​ ​ Fahrenheit​ ​ a ​ ​ grados​ ​ Celsius.
Recordar​ ​ que​ ​ la​ ​ fórmula​ ​ para​ ​ la​ ​ conversión​ ​ es:​ ​ F ​ ​ = ​ ​ (9/5)​ ​ C ​ ​ + ​ ​ 32'''


def fahrenheitACelsius(F):
    return ((F-32)*5/9)
'''print(fahrenheitACelsius(int(input("Grados Fahrenheit:"))))'''


'''​ Implementar​ ​ algoritmos​ ​ que​ ​ permitan:
a)​ ​ Calcular​ ​ el​ ​ perímetro​ ​ y ​ ​ área​ ​ de​ ​ un​ ​ rectángulo​ ​ dada​ ​ su​ ​ base​ ​ y ​ ​ su​ ​ altura.
b)​ ​ Calcular​ ​ el​ ​ perímetro​ ​ y ​ ​ área​ ​ de​ ​ un​ ​ círculo​ ​ dado​ ​ su​ ​ radio.
c)​ ​ Calcular​ ​ el​ ​ volumen​ ​ de​ ​ una​ ​ esfera​ ​ dado​ ​ su​ ​ radio.
d)​ ​ Calcular​ ​ el​ ​ área​ ​ de​ ​ un​ ​ rectángulo​ ​ (alineado​ ​ con​ ​ los​ ​ ejes​ ​ x ​ ​ e ​ ​ y)​ ​ dadas​ ​ sus
coordenadas​ ​ x1,x2,y1,y2.
e)​ ​ Dados​ ​ los​ ​ catetos​ ​ de​ ​ un​ ​ triángulo​ ​ rectángulo,​ ​ calcular​ ​ su​ ​ hipotenusa'''
import math

'''base=int(input("Base del rectangulo:"))
altura=(int(input("Altura del rectangulo:")))
'''
def perimetroRect(base,altura):
    return base*2+altura*2
'''print("El perimetro es " + str(perimetroRect(base,altura)))
'''
def areaRect(base,altura):
    return (base*altura)
'''print("El area del rectangulo es " + str(areaRect(base,altura)))
'''
'''radioCirculo=int(input("Radio del circulo:"))
'''
def perimetroCirc(radioCirculo):
    return radioCirculo*2*math.pi
'''print("El perimetro es " + str(perimetroCirc(radioCirculo)))
'''
def areaCirc(x):
    return (x**2*math.pi)
'''print("El area del Circulo es " + str(areaCirc(radioCirculo)))
'''
def volEsf(x):
    return (4//3*math.pi*x**3)
'''print("El Volumen de la esfera es " + str(volEsf(radioCirculo)))
'''
def areaRect2(x1,x2,y1,y2):
    return (x2-x1)*(y2-y1)
'''print("El area del rectangulo es " + str(areaRect2(int(input("Coordenada x1:")),int(input("Coordenada x2:")),int(input("Coordenada y1:")),int(input("Coordenada y2:")))))
'''
def hipotenusa(x,y):
    return float(math.sqrt(x**2 + y**2))
'''print("La Hipotenusa del rectangulo es " + str(hipotenusa(float(input("Medida del Cateto A:")),float(input("Medida del Cateto B:")))))'''