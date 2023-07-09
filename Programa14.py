print("Programa 14. Calcula el costo total de una compra \n")

def Programa14():
    PG95 = input("Escriba el precio de la gasolina: ")
    CLG = input("Escriba la cantidad de litros: ")

    precio_de_gasolina = float(PG95)
    cantidad_de_litros = float(CLG)

    costo_sin_impuesto = precio_de_gasolina * cantidad_de_litros
    costo_total = costo_sin_impuesto * 1.07

    print("El costo total es de", round(costo_total, 2))
    print("\nFinal del Programa")

Programa14()
