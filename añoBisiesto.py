def añoBiciesto(año):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        return "Año bisiesto"
    else:
        return "Año no biciesto"

print(añoBiciesto(2024))