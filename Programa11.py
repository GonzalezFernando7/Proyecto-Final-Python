print("Programa 11. Regla de tres simple \n")

def Programa11():
    i1 = input("Escribir el valor a: ")
    i2 = input("Escribir el valor b: ")
    i3 = input("Escribir el valor c: ")

    a = float(i1)
    b = float(i2)
    c = float(i3)

    d = (b * c) / a

    dR = round(d, 2)

    print("El valor es de", dR)

    print("\n Final del Programa")

Programa11()
