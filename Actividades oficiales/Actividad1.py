from datetime import datetime
año_actual = datetime.now().year

def nombre_empleado():
    nombre = input("Nombre del empleado: ")
    return nombre

def tipo_de_empleado():
    empleado = int(input("""Tipos de empleados:
    1. Asalariado
    2. Comisionado
    3. Por horas
    Tipo de empleado (1,2,3): """))
    return empleado

def calculo_sueldo(empleado,nombre):
    if empleado == 1:
        año = int(input("Inserte el año de contratación:" ))
        print(nombre, ", su sueldo es ", 1000+(100*(año_actual - año)))

    elif empleado == 2: 
        ventas = int(input("Inserte su total de ventas: "))
        print (nombre, ", su sueldo es ", 800 + (10*ventas))

    elif empleado == 3: 
        horas = int(input ("Inserte sus horas trabajadas: " ))
        print (nombre,", sus sueldo es ", 8/horas)

empleado = nombre_empleado()
tipo = tipo_de_empleado()
calculo_sueldo(tipo,empleado)