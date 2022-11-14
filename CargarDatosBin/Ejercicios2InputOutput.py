import pickle

class Vehiculo:
    marca = ""
    precio = 0.0
    color = ""

    def __init__(self, marca, precio, color):
        self.marca = marca
        self.precio = precio
        self.color = color

    def getMarca(self):
        return self.marca


veh = Vehiculo("Mercedes", 100.000, "blanco")
f = open("ejercicioSobrescritura.bin", "wb")
pickle.dump(veh, f)
f.close()

f = open("ejercicioSobrescritura.bin", "rb")
vari = pickle.load(f)
f.close()

print(type(vari))
print(vari.marca, vari.precio, vari.color)

