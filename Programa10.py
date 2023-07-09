print("Programa 10. Programa de conversión de unidades \n")

def Programa10():
    metros = float(input("Escriba la cantidad de metros: "))

    pies = metros * 3.28084
    pulgadas = metros * 39.3701
    yardas = metros * 1.09361

    DRQ = round(pies, 2)
    DRC = round(pulgadas, 2)
    DRL = round(yardas, 2)

    print("Metros son equivalentes a", DRQ, "pies")
    print("Metros son equivalentes a", DRC, "pulgadas")
    print("Metros son equivalentes a", DRL, "yardas")

    print("\nFinal del Programa")

Programa10()
