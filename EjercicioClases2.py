class Alumno:
    nombre = "Pepito Perez"
    nota = 8

    def Nombre(self):
        return self.nombre


    def Nota(self):
        global nota
        nota = 8
        if nota > 6:
            print("Aprobado")
        else:
            print("Reprobado")
        print("Nota: ", end="")

        return self.nota

p = Alumno()
print(p.Nombre())
print(p.Nota())

