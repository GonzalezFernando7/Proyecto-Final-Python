print("Programa 16. Nota final en la asignatura\n")

def Programa16():
    c1 = float(input('Ingrese la primera nota: '))
    c2 = float(input('Ingrese la segunda nota: '))
    c3 = float(input('Ingrese la tercera nota: '))
    c4 = float(input('Ingrese la cuarta nota: '))
    c5 = float(input('Ingrese la quinta nota: '))

    nota_final = (c1 * 0.20) + (c2 * 0.15) + (c3 * 0.25) + (c4 * 0.10) + (c5 * 0.30)
    nota_redondeada = round(nota_final, 2)

    print("La nota final del estudiante es", nota_redondeada)
    print("\n Final del Programa")

Programa16()
