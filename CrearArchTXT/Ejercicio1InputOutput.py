

f = open("El fichero.txt", "w")
f.write("Intentando escribir un fichero\n")
f.write("dos veces\n")
f.close()


def agregar():
    f = open("El fichero.txt", "a")
    datos = f.write("Agregando nuevo contenido al fichero\n")
    return datos

agregar()

