print("Programa 17. Convertir unidades de medida \n")

def Programa17():
    kilogramos = float(input("Ingresa la cantidad de kg: "))
    gramos = kilogramos * 1000
    print("La cantidad en gramos es:", gramos)

    gramos = float(input("Ingresa la cantidad de g: "))
    kilogramos = gramos * 0.001
    print("La cantidad en kilogramos es:", kilogramos)

    metros = float(input("Ingresa la cantidad de m: "))
    centimetros = metros * 100
    print("La cantidad en centímetros es:", centimetros)

    centimetros = float(input("Ingresa la cantidad de cm: "))
    metros = centimetros * 0.01
    print("La cantidad en metros es:", metros)

    print("\n Final del Programa")

Programa17()