paises = set([])


for i in range(5):
    print("Introduce el nombre de 5 paises")
    usuario = input() + ','
    paises.add(usuario)

orga = sorted(paises)

for i in orga:
    print(i, end="")





