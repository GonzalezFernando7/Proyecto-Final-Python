def Programa40():
    print("Programa 40. Programa que muestra si el valor es positivo, negativo o cero\n")
    valor = float(input("Escribe un valor: "))
    
    if valor > 0:
        clasificacion = "El valor es positivo"
    elif valor < 0:
        clasificacion = "El valor es negativo"
    else:
        clasificacion = "El valor es cero"
    
    print(clasificacion)
    
    print("\nFinal del Programa")

Programa40()

