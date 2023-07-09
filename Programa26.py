print("Programa 26. Clasificación de Triángulos\n")

def Programa26():
    valorA = float(input("Escriba el valor A: "))
    valorB = float(input("Escriba el valor B: "))
    valorC = float(input("Escriba el valor C: "))

    if valorA == valorB == valorC:
        print("El triángulo es equilátero")
    elif valorA == valorB or valorA == valorC or valorB == valorC:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")

    print("\nFinal del Programa")

Programa26()


