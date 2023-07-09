print("Programa 12. Calcula el interés a pagar \n")

def Programa12():
    prestamo = float(input("Escriba el valor del préstamo: "))
    tasa_anual = float(input("Escriba el valor de la tasa anual: "))
    plazo_meses = float(input("Escriba el valor del plazo en meses: "))

    tasa_decimal = tasa_anual / 100
    plazo_anios = plazo_meses / 12
    interes = prestamo * tasa_decimal * plazo_anios

    DR = round(interes, 2)

    print("El interés a pagar es:", DR)

    print("\n Final del Programa")

Programa12()
