'''Escribir un programa que defina una variable entera, sume un valor con decimales, muestre el resultado por pantalla
y verifique el tipo de dato del resultado de la operacion comparado si es string, boolean, int, float'''




'''Escribir un programa que imprima por pantalla el resultado de todas las combinaciones del algebra de boole'''




'''Escribir un programa que valide el tipo de dato de 3 variables. Si las 3 son numericas que las sume y muestre el resultado
Si al menos 1 es texto que multiplique el valor de las 3 variables
Si las 3 son texto que concatene el valor de las 3 variables'''

variable1=5
variable2="6"
variable3=7

if isinstance(variable1,int) and isinstance(variable2,int) and isinstance(variable3,int):
    print(variable1+variable2+variable3)
elif isinstance(variable1,str) and isinstance(variable2,str) and isinstance(variable3,str):
    print(variable1+variable2+variable3)
elif isinstance(variable1,str) or isinstance(variable2,str) or isinstance(variable3,str):
    print(variable1*variable2*variable3)