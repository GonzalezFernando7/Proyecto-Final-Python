print("Programa 18. Calcular Interés Compuesto \n")

def Programa18():
    Ci = float(input("Escriba la capital inicial: "))
    i = float(input("Escriba la tasa de interés: "))
    n = float(input("Escriba el número de periodos: "))

    Cf = Ci * (1 + i) ** n
    capital_final = round(Cf, 2)

    print("La capital final es:", capital_final)
    
    print("\nFinal del Programa")

Programa18()
