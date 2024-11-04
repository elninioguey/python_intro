import math

ingreso = float(input("cantidad a ingresar (€): "))

while ingreso < 0:
    ingreso = float(input("La cantidad debe ser positiva (€): "))
    
print("----------------------------")
interes = float(input("Tipo de interés (%): "))

while interes < 0: 
    interes = float(input("El interés debe ser positivo (%): "))

print("----------------------------")
años = float(input("Años de depósito: "))

while años < 0: 
    años = float(input("El número de años debe ser positivo: "))

print("----------------------------")

print("Ingreso (€):", ingreso)
print ("Interés (%):", interes)
print ("Años:", años)
print ("Total:", ingreso*pow((1+(interes/100)), años))