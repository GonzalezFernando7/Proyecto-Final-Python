print("Programa 5. Calcula el perimetro de un rectangulo \n")

def Programa5():
    i1 = input("Escriba el valor de AB: ")
    i2 = input("Escriba el valor de BC: ")
    i3 = input("Escriba el valor de CD: ")
    i4 = input("Escriba el valor de DA: ")

    AB = float(i1)
    BC = float(i2)
    CD = float(i3)
    DA = float(i4)

    P = AB + BC + CD + DA

    PR = round(P, 2)

    print("El perímetro del rectángulo es:", P)
    
    print("\n Final del Programa")

Programa5()
