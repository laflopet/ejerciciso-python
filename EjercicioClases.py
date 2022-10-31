class vehiculo:
    ruedas = 4
    puertas = 4

    def Color(self, color):
        print("El color del vehiculo es:", color)

    def Ruedas(self):
        print("Ruedas: ", end="")
        return self.ruedas

    def Puertas(self):
        print("Puertas: ", end="")
        return self.puertas

class coche(vehiculo):

    def Velocidad(self, velocidad):
        print("La velocidad del coche es:", velocidad,"km/h")

    def Cilindrada(self, cilindrada):
        print("La cilindrada del coche es de:", cilindrada,"cc")

p = coche()
p.Color("Verde")
print(p.Ruedas())
print(p.Puertas())
p.Velocidad(80)
p.Cilindrada(2000)

