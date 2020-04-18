def multiplyByTwo(number):
    return multiplyTwoNumbers(number,2)

def multiplyTwoNumbers(number1,number2):
    return number1*number2


def noValue(number1,number2):
    resultado = number1*number2
    print(resultado)
    return resultado

print(noValue(5,10))

print(multiplyByTwo(5))

number = multiplyByTwo(5)

print(multiplyByTwo(number))

print(multiplyByTwo(multiplyByTwo(multiplyByTwo(18))))



