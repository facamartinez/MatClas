



number = 8


#usando elif
def oddOrEven(number):
    #voy a tomar el modulo de la division
    mod = number%2
    output = None
    if mod == 0:
        output = "even"
    elif mod == 1:
        output = "odd"
    elif mod == None:
        output = ""
    return output

print(oddOrEven(number))

def oddOrEven2(number):
    #voy a tomar el modulo de la division
    mod = number%2
    if mod == 0:
        return "even"
    else:
        return "odd"


def oddOrEven3(number):
    #voy a tomar el modulo de la division
    mod = number%2
    output = "odd"
    if mod == 0:
        output = "even"
    return output

def maximo(a,b,c):
    if a>b:
        if a>c:
            return a
        return c
    elif b>c:
        return b
    return c

print(maximo(1,2,3))
print(maximo(3,2,1))



'''Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

Example
One line if statement:'''
a=5
b=10
if a > b: print("a is greater than b")


'''Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

Example
One line if else statement:'''

a = 2
b = 330
print("A") if a > b else print("B")


'''This technique is known as Ternary Operators, or Conditional Expressions.

You can also have multiple else statements on the same line:

Example
One line if else statement, with 3 conditions:'''

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

