print("Programa 19. Calcula la compra de 5 artículos \n")

def Programa19():
    precio1 = float(input("Precio del artículo: "))
    precio2 = float(input("Precio del artículo: "))
    precio3 = float(input("Precio del artículo: "))
    precio4 = float(input("Precio del artículo: "))
    precio5 = float(input("Precio del artículo: "))

    total_sin_impuesto = precio1 + precio2 + precio3 + precio4 + precio5
    total_con_impuesto = total_sin_impuesto * 1.07
    promedio_de_compra = total_sin_impuesto / 5

    total_sin_impuesto_redondeado = round(total_sin_impuesto, 2)
    total_con_impuesto_redondeado = round(total_con_impuesto, 2)
    promedio_de_compra_redondeado = round(promedio_de_compra, 2)

    print("El total sin impuesto es:", total_sin_impuesto_redondeado)
    print("El total con impuesto es:", total_con_impuesto_redondeado)
    print("El promedio de compra es:", promedio_de_compra_redondeado)
    print("\nFinal del Programa")

Programa19()
