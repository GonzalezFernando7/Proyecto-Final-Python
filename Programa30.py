def Programa30():
     print("Programa 27. Determinar si el número es positivo, negativo o cero\n")
     
     value = 1
     while value <= 3:
        print(value)
        cantidad = float(input("Escriba el valor: "))
        if cantidad > 0:
            print("La cantidad es positiva")
        elif cantidad < 0:
            print("La cantidad es negativa")
        else:
            print("La cantidad es cero")
    
        print("\nFinal del Programa")
        
        value += 1

Programa30()