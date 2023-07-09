print("Programa 25. Calculadora de Descuentos\n")

def Programa25():
    precio_del_producto = float(input("Escriba el Precio del producto: "))
    porcentaje_descuento = float(input("Escriba el Porcentaje de descuento: "))

    descuento = (porcentaje_descuento * precio_del_producto) / 100

    precio_final = precio_del_producto - descuento

    precio_final_redondeado = round(precio_final, 2)
    print("El Precio Final es", precio_final_redondeado)

    if precio_final < 50:
        print("!Oferta Especial!")

    print("\nFinal del Programa")


Programa25()
