name = "Matias"

def sayHello(unParametro):
    variable1=6
    print("Hello",unParametro)

sayHello(name)

def sayHello2(name):
    name = "John"
    print("Hello",name)

sayHello2(name)
print(name)

def multiplicar(numero1,numero2=2,numero3=6):
    return numero1*numero2*numero3

valor=8
print(multiplicar(valor))
print(multiplicar(valor,7))
print(multiplicar(valor,numero3=7))
print(valor)

valor = multiplicar(valor,4)
print(valor)