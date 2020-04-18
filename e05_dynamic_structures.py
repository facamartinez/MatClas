lista = [2, 4, 6]
#crea un nuevo vector con los valores del vector original multiplicados por 3
print ([3*x for x in lista])

#crea un nuevo vector con los valores del vector original mayores a 3 y multiplicados
print([3*x for x in lista if x > 3])


print([3*x for x in lista if x < 2])


print([[x,x**2] for x in lista])


vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

print([x*y for x in vec1 for y in vec2])

print([x+y for x in vec1 for y in vec2])

print([vec1[i]*vec2[i] for i in range(len(vec1))])

# Pueden aplicarse a expresiones complejas y funciones anidadas
print([str(round(355/113.0, i)) for i in range(1,6)])

# Listas por comprensión anidadas
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Para intercambiar filas y columnas
print([[fila[i] for fila in mat] for i in range(len(mat))])

matriz_nueva = []
for i in range(3):
    fila_nueva = []
    for fila in mat:
        fila_nueva.append(fila[i])
    matriz_nueva.append(fila_nueva)
print(matriz_nueva)


a = dict([(x, x ** 2) for x in (2, 4, 6)])  # use a list por comprensión
print (a)
print (a[2])
