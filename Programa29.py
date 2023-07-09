def Programa29():
    print("Programa 28. Programa que evalúa calificaciones\n")

    value = 1

    while value <= 5:
        print(value)
        evaluacion = float(input("Escriba la nota: "))

        if evaluacion >= 90 and evaluacion <= 100:
            print("Su evaluación es A")
        elif evaluacion >= 80 and evaluacion <= 89:
            print("Su evaluación es B")
        elif evaluacion >= 70 and evaluacion <= 79:
            print("Su evaluación es C")
        elif evaluacion >= 60 and evaluacion <= 69:
            print("Su evaluación es D")
        else:
            print("Su evaluación es F")

        print("\nFinal del programa")
        
        value += 1

Programa29()
