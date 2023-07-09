print("Programa 15. Precios totales de la compra con el impuesto incluido \n")

def Programa15():
    precio1 = float(input("Precio del artículo 1: "))
    precio2 = float(input("Precio del artículo 2: "))
    precio3 = float(input("Precio del artículo 3: "))

    precio_del_articulo1 = precio1 * 1.07
    precio_del_articulo2 = precio2 * 1.07
    precio_del_articulo3 = precio3 * 1.07

    costo_total = precio_del_articulo1 + precio_del_articulo2 + precio_del_articulo3

    costo_redondeado = round(costo_total, 2)

    print("El costo total es de", costo_redondeado)
    print("\n Final del Programa")

Programa15()