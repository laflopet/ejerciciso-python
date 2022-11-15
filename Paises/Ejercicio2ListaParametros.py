from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def impares(x):
    if x % 2 != 0:
        return x

def suma(a, b):
    return a + b

impar = filter(impares, numeros)
resultado = reduce(suma, list(impar))
print(resultado)