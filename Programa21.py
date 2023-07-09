print("Programa 21. Calcule si una persona paga impuestos\n")

def Programa21():
    salario = float(input("Escriba el salario: "))

    if salario <= 3000:
        impuesto = salario * 1.07
        print("Esta persona debe abonar", impuesto)
    else:
        print("No debe abonar impuestos")

    print("\nFin del programa")


Programa21()