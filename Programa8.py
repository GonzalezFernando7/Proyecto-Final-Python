print("Programa 8. Resuelve ecuaciones \n")

def Programa8():
    x1 = input("escribe el valor de x:")
    x = float(x1)
    
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) - 5 - (8 * x) + 2
    E = (((5 * x) + 78) / 28)
    F = (((6 * x) - 7) /4) + (((3 * 7)-5)/7)
    
    print("el resultado de A es",round(A,2))
    print("el resultado de B es",round(B,2))
    print("el resultado de C es",round(C,2))
    print("el resultado de D es",round(D,2))
    print("el resultado de E es",round(E,2))
    print("el resultado de F es",round(F,2))
    
    print("\n Final del Programa")

Programa8()