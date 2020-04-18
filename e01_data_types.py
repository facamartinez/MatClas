'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''
#single line comments allow me to document code execution

#Learning primitive datatypes
print(type(1))
print(type(1.0))
print(type("1"))
print(type(True))

#we can modify a variable type through standard library functions

print(type(float(1)))
print(type(str(1)))
print(type(int("1")))
print(type(bool("1")))
print(bool(0))
print(bool(1))


#we can check for a datatyape

print(isinstance(1,int))
print(isinstance(1,float))
print(isinstance(1.0,float))
print(isinstance(1,bool))