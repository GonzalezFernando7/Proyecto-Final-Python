print("Programa 22. Calcule la temperatura\n")

def Programa22():
    temperatura = float(input("Escriba la temperatura: "))

    if temperatura < 20:
        if temperatura < 10:
            print("Nivel azul")
        else:
            print("Nivel verde")
    else:
        if temperatura < 30:
            print("Nivel naranja")
        else:
            print("Nivel rojo")

    print("\nFin del programa")


Programa22()

