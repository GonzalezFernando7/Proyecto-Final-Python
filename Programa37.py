def Programa37():
    print("Programa 37. Proyecto en Clases\n")

    value = 1
    while value <= 5:
        print(value)
        print("Programa que indica cuál de los tres valores es mayor")
        a = float(input("Escriba el valor: "))
        b = float(input("Escriba el valor: "))
        c = float(input("Escriba el valor: "))

        if a > b and a > c:
            print("El número mayor es a =", a)
        if b > a and b > c:
            print("El número mayor es b =", b)
        if c > a and c > b:
            print("El número mayor es c =", c)

        value += 1

    print("\nFinal del Programa")

Programa37()