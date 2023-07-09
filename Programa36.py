def Programa36():
    print("Programa 36. Capturar 5 artículos y calcular el 7%\n")

    i = 0
    while i < 5:
        valor = float(input("Escribe el valor del artículo: "))
        impuesto = valor * 0.07
        print("El impuesto del artículo con valor", valor, "es:", impuesto)
        i += 1

    print("\nFinal del Programa")

Programa36()
