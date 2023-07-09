import time
def pausar(segundos):
    inicio = time.time()
    while time.time() - inicio < segundos:
        pass

def Programa1():
    print("Programa 1. Practica Inicial Python \n:")
    
    A = 7
    B = 0
    C = 0

    B = A
    C = B
    A = A

    print(A, B, C)
    print("\n Final del Programa")
    
    print("Programa1")
    pausar(3)


def Programa2():
    print("Programa 2. Practica Python \n:")

    A = 10
    B = 20
    AUX = 0

    AUX = A
    A = B
    B = AUX

    print(A, B, AUX)
    print("\n Final del Programa")
    
    print("Programa2")
    pausar(3)

def Programa3():
    print("Programa 3. Practica Python \n")

    A = float(input("Leer A: "))
    B = float(input("Leer B: "))
    C = float(input("Leer C: "))

    D = (A + B + C) / 3
    DR = round(D, 2)

    print("El resultado es:", DR)
    print("\nFin del Programa")
    
    print("Programa3")
    pausar(3)


    
def Programa4():
    print("Programa 4. Calcula el area de un rectangulo \n")
    
    base = 3
    altura = 4
    area = (base * altura) / 2
    print(area)
    
    print("\n Final del Programa")
    
    print("Programa4")
    pausar(3)
    
def Programa5():
    print("Programa 5. Calcula el perimetro de un rectangulo \n")

    i1 = input("Escriba el valor de AB: ")
    i2 = input("Escriba el valor de BC: ")
    i3 = input("Escriba el valor de CD: ")
    i4 = input("Escriba el valor de DA: ")

    AB = float(i1)
    BC = float(i2)
    CD = float(i3)
    DA = float(i4)

    P = AB + BC + CD + DA
    PR = round(P, 2)

    print("El perímetro del rectángulo es:", P)
    print("\n Final del Programa")
    
    print("Programa5")
    pausar(3)
    
def Programa6():
    print("Programa 6. Calcula el area de un trapecio \n")

    i1 = input("Escribir el valor de la Base1: ")
    i2 = input("Escribir el valor de la Base2: ")
    i3 = input("Escribir el valor de la Altura: ")

    Base1 = float(i1)
    Base2 = float(i2)
    Altura = float(i3)

    Area = (Base1 + Base2) * Altura / 2
    AR = round(Area, 2)

    print("El área del trapecio es:", AR)
    print("\n Final del Programa")
    
    print("Programa6")
    pausar(3)

def Programa7():
    print("Programa 7. Calcula el volumen de un prisma rectangular \n")

    i1 = input("Escribir el valor de la Base1: ")
    i2 = input("Escribir el valor de la Base2: ")
    i3 = input("Escribir el valor de la Altura: ")

    Base1 = float(i1)
    Base2 = float(i2)
    Altura = float(i3)

    Area = (Base1 + Base2) * Altura / 2
    AR = round(Area, 2)

    print("El área del trapecio es:", AR)
    print("\n Final del Programa")
    
    print("Programa7")
    pausar(3)
    
def Programa8():
    print("Programa 8. Resuelve ecuaciones \n")

    x1 = input("escribe el valor de x:")
    x = float(x1)
    
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) - 5 - (8 * x) + 2
    E = (((5 * x) + 78) / 28)
    F = (((6 * x) - 7) /4) + (((3 * 7)-5)/7)
    
    print("el resultado de A es",round(A,2))
    print("el resultado de B es",round(B,2))
    print("el resultado de C es",round(C,2))
    print("el resultado de D es",round(D,2))
    print("el resultado de E es",round(E,2))
    print("el resultado de F es",round(F,2))
    print("\n Final del Programa")
    
    print("Programa8")
    pausar(3)
    
def Programa9():
    print("Programa 9. Programa que resuelve ecuaciones \n")

    a1 = input("Escriba el valor de a: ")
    a2 = input("Escriba el valor de b: ")
    a3 = input("Escriba el valor de c: ")

    a = float(a1)
    b = float(a2)
    c = float(a3)

    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c4 = (2 * a) + (3 * b) - (c ** 5)
    c5 = (2 * a) + (3 * b) - (c ** 2)

    print("El resultado de c1 es", round(c1, 2))
    print("El resultado de c2 es", round(c2, 2))
    print("El resultado de c3 es", round(c3, 2))
    print("El resultado de c4 es", round(c4, 2))
    print("El resultado de c5 es", round(c5, 2))
    print("\nFinal del Programa")
    
    print("Programa9")
    pausar(3)
    
def Programa10():
    print("Programa 10. Programa de conversión de unidades \n")

    metros = float(input("Escriba la cantidad de metros: "))

    pies = metros * 3.28084
    pulgadas = metros * 39.3701
    yardas = metros * 1.09361

    DRQ = round(pies, 2)
    DRC = round(pulgadas, 2)
    DRL = round(yardas, 2)

    print("Metros son equivalentes a", DRQ, "pies")
    print("Metros son equivalentes a", DRC, "pulgadas")
    print("Metros son equivalentes a", DRL, "yardas")
    print("\nFinal del Programa")
    
    print("Programa10")
    pausar(3)
    
def Programa11():
    print("Programa 11. Regla de tres simple \n")

    i1 = input("Escribir el valor a: ")
    i2 = input("Escribir el valor b: ")
    i3 = input("Escribir el valor c: ")

    a = float(i1)
    b = float(i2)
    c = float(i3)

    d = (b * c) / a
    
    dR = round(d, 2)
    print("El valor es de", dR)
    print("\n Final del Programa")
    
    print("Programa11")
    pausar(3)
    
def Programa12():
    print("Programa 12. Calcula el interés a pagar \n")

    prestamo = float(input("Escriba el valor del préstamo: "))
    tasa_anual = float(input("Escriba el valor de la tasa anual: "))
    plazo_meses = float(input("Escriba el valor del plazo en meses: "))

    tasa_decimal = tasa_anual / 100
    plazo_anios = plazo_meses / 12
    interes = prestamo * tasa_decimal * plazo_anios

    DR = round(interes, 2)
    print("El interés a pagar es:", DR)
    print("\n Final del Programa")
    
    print("Programa12")
    pausar(3)
    
def Programa13():
    print("Programa 13. Calcula el salario neto \n")

    salario_bruto = float(input("ingresa su salario_bruto: "))
    seguro_social = salario_bruto * 0.097
    print("el seguro_social es:", seguro_social)
    round = (seguro_social,2)
    
    seguro_educativo = salario_bruto * 0.012
    print("el seguro_educativo es:", seguro_educativo)
    round = (seguro_educativo,2)
    
    prestamo_personal = 50
    print("el prestamo_personal es:", prestamo_personal)
    round = (prestamo_personal,2)
    
    salario_neto = salario_bruto - seguro_social - seguro_educativo - prestamo_personal
    print("el salario neto es:", salario_neto)
    print("\n Final del Programa")
    
    print("Programa13")
    pausar(3)
    
def Programa14():
    print("Programa 14. Calcula el costo total de una compra \n")

    PG95 = input("Escriba el precio de la gasolina: ")
    CLG = input("Escriba la cantidad de litros: ")

    precio_de_gasolina = float(PG95)
    cantidad_de_litros = float(CLG)

    costo_sin_impuesto = precio_de_gasolina * cantidad_de_litros
    costo_total = costo_sin_impuesto * 1.07

    print("El costo total es de", round(costo_total, 2))
    print("\nFinal del Programa")
    
    print("Programa14")
    pausar(3)
    
def Programa15():
    print("Programa 15. Precios totales de la compra con el impuesto incluido \n")

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
    
    print("Programa15")
    pausar(3)
    
def Programa16():
    print("Programa 16. Nota final en la asignatura\n")

    c1 = float(input('Ingrese la primera nota: '))
    c2 = float(input('Ingrese la segunda nota: '))
    c3 = float(input('Ingrese la tercera nota: '))
    c4 = float(input('Ingrese la cuarta nota: '))
    c5 = float(input('Ingrese la quinta nota: '))

    nota_final = (c1 * 0.20) + (c2 * 0.15) + (c3 * 0.25) + (c4 * 0.10) + (c5 * 0.30)
    nota_redondeada = round(nota_final, 2)

    print("La nota final del estudiante es", nota_redondeada)
    print("\n Final del Programa")
    
    print("Programa16")
    pausar(3)
    
def Programa17():
    print("Programa 17. Convertir unidades de medida \n")

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
    
    print("Programa17")
    pausar(3)
    
def Programa18():
    print("Programa 18. Calcular Interés Compuesto \n")

    Ci = float(input("Escriba la capital inicial: "))
    i = float(input("Escriba la tasa de interés: "))
    n = float(input("Escriba el número de periodos: "))

    Cf = Ci * (1 + i) ** n
    capital_final = round(Cf, 2)

    print("La capital final es:", capital_final)
    print("\nFinal del Programa")
    
    print("Programa18")
    pausar(3)
    
def Programa19():
    print("Programa 19. Calcula la compra de 5 artículos \n")

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
    
    print("Programa19")
    pausar(3)
    
def Programa20():
    print("Programa 20. Calcula el salario neto de un empleado\n")

    SalarioBruto = int(input("Ingresa su salario bruto: "))

    SeguroSocial = SalarioBruto * 0.08
    SeguroEducativo = SalarioBruto * 0.02
    impuesto = SalarioBruto * 0.15
    prestamo = 100

    SalarioNeto = SalarioBruto - SeguroSocial - SeguroEducativo - impuesto - prestamo

    print("La cantidad a pagar de su Seguro Social es de", SeguroSocial)
    print("La cantidad a pagar de su Seguro Educativo es de", SeguroEducativo)
    print("La cantidad a pagar de su impuesto es", impuesto)
    print("La cantidad a pagar de su préstamo es de", prestamo)
    print("El Salario Neto es de", SalarioNeto)
    print("\nFinal del Programa")
    
    print("Programa20")
    pausar(3)
    
def Programa21():
    print("Programa 21. Calcule si una persona paga impuestos\n")

    salario = float(input("Escriba el salario: "))

    if salario <= 3000:
        impuesto = salario * 1.07
        print("Esta persona debe abonar", impuesto)
    else:
        print("No debe abonar impuestos")
    print("\nFin del programa")
    
    print("Programa21")
    pausar(3)

def Programa22():
    print("Programa 22. Calcule la temperatura\n")

    temperatura = float(input("Escriba la temperatura: "))

    if temperatura < 20:
        if temperatura < 10:
            print("Nivel azul")
        else:
            print("Nivel verde")
    else:
        if temperatura < 30:
            print("Nivel naranja")
        else:
            print("Nivel rojo")
        print("\nFin del programa")
    
    print("Programa22")
    pausar(3)
    
def Programa23():
    print("Programa 23. Calcular si es mayor o menor de edad\n")

    edad = float(input("Escribir la edad: "))

    if edad >= 18:
        print('Eres adulto')
    elif edad < 18:
        print('Eres menor de edad')
    print("\nFin del programa")
    
    print("Programa23")
    pausar(3)

def Programa24():
    print("Programa 24. Calcular el mayor de 3 números\n")

    a = float(input("Escribir primer número: "))
    b = float(input("Escribir segundo número: "))
    c = float(input("Escribir tercer número: "))

    if a > b and a > c:
        print("El número mayor es a:", a)
    if b > a and b > c:
        print("El número mayor es b:", b)
    if c > a and c > b:
        print("El número mayor es c:", c)
        print("\nFin del programa")
    
    print("Programa24")
    pausar(3)
    
def Programa25():
    print("Programa 25. Calculadora de Descuentos\n")

    precio_del_producto = float(input("Escriba el Precio del producto: "))
    porcentaje_descuento = float(input("Escriba el Porcentaje de descuento: "))

    descuento = (porcentaje_descuento * precio_del_producto) / 100

    precio_final = precio_del_producto - descuento

    precio_final_redondeado = round(precio_final, 2)
    print("El Precio Final es", precio_final_redondeado)

    if precio_final < 50:
        print("!Oferta Especial!")
    print("\nFinal del Programa")
    
    print("Programa25")
    pausar(3)
    
def Programa26():
    print("Programa 26. Clasificación de Triángulos\n")

    valorA = float(input("Escriba el valor A: "))
    valorB = float(input("Escriba el valor B: "))
    valorC = float(input("Escriba el valor C: "))

    if valorA == valorB == valorC:
        print("El triángulo es equilátero")
    elif valorA == valorB or valorA == valorC or valorB == valorC:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
    print("\nFinal del Programa")
    
    print("Programa26")
    pausar(3)

def Programa27():
    print("Programa 27. Determinar si el número es positivo, negativo o cero\n")

    cantidad = float(input("Escriba el valor: "))

    if cantidad > 0:
        print("La cantidad es positiva")
    elif cantidad < 0:
        print("La cantidad es negativa")
    else:
        print("La cantidad es cero")
    print("\nFinal del Programa")
    
    print("Programa27")
    pausar(3)
    
def Programa28():
    print("Programa 28. Evalúa calificaciones\n")

    evaluacion = int(input("Escriba la nota: "))

    if evaluacion >= 90 and evaluacion <= 100:
        print("Su evaluación es A")
    elif evaluacion >= 80 and evaluacion <= 89:
        print("Su evaluación es B")
    elif evaluacion >= 70 and evaluacion <= 79:
        print("Su evaluación es C")
    elif evaluacion >= 60 and evaluacion <= 69:
        print("Su evaluación es D")
    else:
        print("Su evaluación es F")
    print("\nFinal del programa")
    
    print("Programa28")
    pausar(3)
    
def Programa29():
    print("Programa 28. Programa que evalúa calificaciones\n")
    value = 1
    
    while value <= 5:
        print(value)
        evaluacion = float(input("Escriba la nota: "))

        if evaluacion >= 90 and evaluacion <= 100:
            print("Su evaluación es A")
        elif evaluacion >= 80 and evaluacion <= 89:
            print("Su evaluación es B")
        elif evaluacion >= 70 and evaluacion <= 79:
            print("Su evaluación es C")
        elif evaluacion >= 60 and evaluacion <= 69:
            print("Su evaluación es D")
        else:
            print("Su evaluación es F")
        
        print("\nFinal del programa")
        value += 1
        
    print("Programa29")
    pausar(3)
    
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
        
        print("Programa30")
        pausar(3)

def Programa31():
    print("Programa 31.\n")

    for x in range(1, 6):
        print("Evaluación", x)
        nota = float(input("Escribe la nota: "))

        if nota >= 90 and nota <= 100:
            print("Su evaluación es A")
        elif nota >= 80 and nota <= 89:
            print("Su evaluación es B")
        elif nota >= 70 and nota <= 79:
            print("Su evaluación es C")
        elif nota >= 60 and nota <= 69:
            print("Su evaluación es D")
        else:
            print("Su evaluación es F")
        print("\nFinal del programa")
        
    print("Programa31")
    pausar(3)
    
def Programa32():
    print("Programa 32. Trata de mostrar 10 números\n")

    valor = 1
    while valor < 11:
        if valor == 7:
            break
        print(valor)
        valor += 1
    print("\nFin del Programa")
    
    print("Programa32")
    pausar(3)
    
def Programa33():
    print("Programa 33. Tabla de multiplicar\n")

    for i in range(1, 13):
        print("Tabla de multiplicar del", i)
        print("==========================")
        for j in range(1, 13):
            resultado = i * j
            print(i, "x", j, "=", resultado)
        print()
    print("\nFinal del Programa")
    
    print("Programa33")
    pausar(3)

def Programa34():
    print("Programa 34. Imprimir los números del 0 al 15\n")

    numero = 0
    while numero <= 15:
        print(numero)
        
        if numero % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
        numero += 1

    print("\nFinal del Programa")
    
    print("Programa34")
    pausar(3)

def Programa35():
    print("Programa 35. Lista de números del 1 al 10\n")

    for a in range(1, 11):
        if a > 5:
            print("Mayor a 5")
        elif a < 5:
            print("Menor a 5")
        else:
            print("Igual a 5")

        if a == 9:
            break
    print("\nFinal del Programa")
    
    print("Programa35")
    pausar(3)

def Programa36():
    print("Programa 36. Capturar 5 artículos y calcular el 7%\n")

    i = 0
    while i < 5:
        valor = float(input("Escribe el valor del artículo: "))
        impuesto = valor * 0.07
        print("El impuesto del artículo con valor", valor, "es:", impuesto)
        i += 1
    print("\nFinal del Programa")
    
    print("Programa36")
    pausar(3)

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
    
    print("Programa37")
    pausar(3)

def Programa38():
    print("Programa 38. Calcular la suma de Numeros Pares \n")
    numero = 20
    suma = 0

    while numero > 0:
        if numero % 2 == 0:
            suma += numero
        numero -= 1

    print("La suma de los números pares hasta 20 es:", suma)
    
    print("\n Final del Programa")

    print("Programa38")
    pausar(3)

def Programa39():
    print("Programa 39. Calcula el área de un triángulo\n")
    
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    
    area = (base * altura) / 2
    print("El área del triángulo es:", area)
    
    print("\nFinal del Programa")

    print("Programa39")
    pausar(3)

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

    print("Programa40")
    pausar(3)


def mostrar_menu():
    print("1. Programa1")
    print("2. Programa2")
    print("3. Programa3")
    print("4. Programa4")
    print("5. Programa5")
    print("6. Programa6")
    print("7. Programa7")
    print("8. Programa8")
    print("9. Programa9")
    print("10. Programa10")
    print("11. Programa11")
    print("12. Programa12")
    print("13. Programa13")
    print("14. Programa14")
    print("15. Programa15")
    print("16. Programa16")
    print("17. Programa17")
    print("18. Programa18")
    print("19. Programa19")
    print("20. Programa20")
    print("21. Programa21")
    print("22. Programa22")
    print("23. Programa23")
    print("24. Programa24")
    print("25. Programa25")
    print("26. Programa26")
    print("27. Programa27")
    print("28. Programa28")
    print("29. Programa29")
    print("30. Programa30")
    print("31. Programa31")
    print("32. Programa32")
    print("33. Programa33")
    print("34. Programa34")
    print("35. Programa35")
    print("36. Programa36")
    print("37. Programa37")
    print("38. Programa38")
    print("39. Programa39")
    print("40. Programa40")
                    
def main():
    contador = 0

    while contador < 6:
        mostrar_menu()
        opcion = int(input("Selecciona un programa (0 para salir): "))

        if opcion == 0:
            break

        if opcion == 1:
            Programa1()
        elif opcion == 2:
            Programa2()
        elif opcion == 3:
            Programa3()
        elif opcion == 4:
            Programa4()
        elif opcion == 5:
            Programa5()
        elif opcion == 6:
            Programa6()
        elif opcion == 7:
            Programa7()
        elif opcion == 8:
            Programa8()
        elif opcion == 9:
            Programa9()
        elif opcion == 10:
            Programa10()
        elif opcion == 11:
            Programa11()
        elif opcion == 12:
            Programa12()
        elif opcion == 13:
            Programa13()
        elif opcion == 14:
            Programa14()
        elif opcion == 15:
            Programa15()
        elif opcion == 16:
            Programa16()
        elif opcion == 17:
            Programa17()
        elif opcion == 18:
            Programa18()
        elif opcion == 19:
            Programa19()
        elif opcion == 20:
            Programa20()
        elif opcion == 21:
            Programa21()
        elif opcion == 22:
            Programa22()
        elif opcion == 23:
            Programa23()
        elif opcion == 24:
            Programa24()
        elif opcion == 25:
            Programa25()
        elif opcion == 26:
            Programa26()
        elif opcion == 27:
            Programa27()
        elif opcion == 28:
            Programa28()
        elif opcion == 29:
            Programa29()
        elif opcion == 30:
            Programa30()
        elif opcion == 31:
            Programa31()
        elif opcion == 32:
            Programa32()
        elif opcion == 33:
            Programa33()
        elif opcion == 34:
            Programa34()
        elif opcion == 35:
            Programa35()
        elif opcion == 36:
            Programa36()
        elif opcion == 37:
            Programa37()
        elif opcion == 38:
            Programa38()
        elif opcion == 39:
            Programa39()
        elif opcion == 40:
            Programa40()
        else:
            print("Opción inválida")

        contador += 1

main()



