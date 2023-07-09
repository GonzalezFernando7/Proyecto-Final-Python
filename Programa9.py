print("Programa 9. Programa que resuelve ecuaciones \n")

def Programa9():
    a1 = input("Escriba el valor de a: ")
    a2 = input("Escriba el valor de b: ")
    a3 = input("Escriba el valor de c: ")

    a = float(a1)
    b = float(a2)
    c = float(a3)

    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c4 = (2 * a) + (3 * b) - (c ** 5)
    c5 = (2 * a) + (3 * b) - (c ** 2)

    print("El resultado de c1 es", round(c1, 2))
    print("El resultado de c2 es", round(c2, 2))
    print("El resultado de c3 es", round(c3, 2))
    print("El resultado de c4 es", round(c4, 2))
    print("El resultado de c5 es", round(c5, 2))

    print("\nFinal del Programa")
    
Programa9()
