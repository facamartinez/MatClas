try:
    variable = "100"
    variable = float(variable)
    variable/1
except ValueError as e:
    #print(str(e))
    print("Error transformando variable a float")
except ZeroDivisionError as error:
    print("No se puede dividir por cero")
except Exception as error:
    print("Error general")
#finally:
#    print("Siempre voy a pasar por este bloque")

#try catch anidados

def cargarUsuario(nombre):
    if nombre == "Bort":
        raise ValueError("No admitimos usuarios llamados Bort")
    else:
        print("Bienvenido",nombre)

usuarios = ["matias","Bort","jorge","juan"]
for usuario in usuarios:
    try:
        cargarUsuario(usuario)
    except ValueError as e:
        pass
        #print("No se pudo cargar el usuario:",usuario)