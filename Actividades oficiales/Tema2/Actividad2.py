import math

def insertar_ingreso():
    ingreso = float(input("cantidad a ingresar (€): "))

    while ingreso < 0:
        ingreso = float(input("La cantidad debe ser positiva (€): "))
    return ingreso

def insertar_interes():
    interes = float(input("Tipo de interés (%): "))

    while interes < 0: 
        interes = float(input("El interés debe ser positivo (%): "))
    return interes

def insertar_años():
    años = float(input("Años de depósito: "))

    while años < 0: 
        años = float(input("El número de años debe ser positivo: "))
    return años

def calculo_final(ingreso,interes,años):
    print("Ingreso (€):", ingreso)
    print ("Interés (%):", interes)
    print ("Años:", años)
    print ("Total:", ingreso*pow((1+(interes/100)), años))

print ("-"*40)
ingreso = insertar_ingreso()
print ("-"*40)

interes = insertar_interes()
print ("-"*40)

años = insertar_años()
print ("-"*40)

calculo_final(ingreso,interes,años)
print ("-"*40)