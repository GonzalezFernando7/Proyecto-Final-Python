print("Programa 23. Calcular si es mayor o menor de edad\n")

def Programa23():
    edad = float(input("Escribir la edad: "))

    if edad >= 18:
        print('Eres adulto')
    elif edad < 18:
        print('Eres menor de edad')

    print("\nFin del programa")

Programa23()