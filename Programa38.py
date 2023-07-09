print("Programa 38. Calcular la suma de Numeros Pares \n")

def Programa38():
    numero = 20
    suma = 0

    while numero > 0:
        if numero % 2 == 0:
            suma += numero
        numero -= 1

    print("La suma de los números pares hasta 20 es:", suma)
    
    print("\n Final del Programa")

Programa38()