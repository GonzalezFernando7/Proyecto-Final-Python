print("Programa 7. Calcula el volumen de un prisma rectangular \n")

def Programa7():
    i1 = input("Escribir el valor de la Base1: ")
    i2 = input("Escribir el valor de la Base2: ")
    i3 = input("Escribir el valor de la Altura: ")

    Base1 = float(i1)
    Base2 = float(i2)
    Altura = float(i3)

    Area = (Base1 + Base2) * Altura / 2

    AR = round(Area, 2)

    print("El área del trapecio es:", AR)
    
    print("\n Final del Programa")

Programa7()
