def printName():
    #this is a global variable since it's not defined inside my function
    print(name)

name = "Matias"

printName()

def printAnotherName():
    #this is a local variable that only exists inside the function
    name = "John"
    print(name)

name = "Robert"
printAnotherName()
print(name)


def f():
    print(s)

    # This program will NOT show error
    # if we comment below line.
    s = "Me too."

    print(s)
    global s

# Global scope
s = "I love Python"
f()
print(s)