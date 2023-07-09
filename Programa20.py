print("Programa 20. Calcula el salario neto de un empleado\n")

def Programa20():
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


Programa20()
