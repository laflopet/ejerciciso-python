import time

comphora = time.localtime().tm_hour
compminutos = time.localtime().tm_min
compseg = time.localtime().tm_sec

if comphora >= 19 or comphora >= 1 and comphora < 8:
    print("La hora es: ", comphora,":", compminutos,":", compseg, sep="")

if comphora >= 8 and comphora < 19:
    print("faltan ", 18 - comphora,":", 59 - compminutos,":", 59 - compseg," para salir del trabajo", sep="")
