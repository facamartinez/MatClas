char = "-"

#function with default parameters
def printLine(character="*",numberOfTimes=10):
    print(character*numberOfTimes)

#function with required parameters
def printShortLine(character):
    printLine(character,25)

def printLongLine(character):
    printLine(character,100)


#I can call a function that uses another function
printShortLine(char)
printLongLine(char)
printLine()
printLine(numberOfTimes=50)
printLine(character="~",numberOfTimes=100)

#required positional parameter error
printShortLine()

'''Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Arbitrary Arguments are often shortened to *args in Python documentations.

Example
If the number of arguments is unknown, add a * before the parameter name:'''

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


'''Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:'''

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")