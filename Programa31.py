def Programa31():
    print("Programa 31.\n")

    for x in range(1, 6):
        print("Evaluación", x)
        nota = float(input("Escribe la nota: "))

        if nota >= 90 and nota <= 100:
            print("Su evaluación es A")
        elif nota >= 80 and nota <= 89:
            print("Su evaluación es B")
        elif nota >= 70 and nota <= 79:
            print("Su evaluación es C")
        elif nota >= 60 and nota <= 69:
            print("Su evaluación es D")
        else:
            print("Su evaluación es F")

    print("\nFinal del programa")

Programa31()