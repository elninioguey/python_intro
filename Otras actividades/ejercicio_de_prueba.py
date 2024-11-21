import math 


unidades = input("""¿Qué unidad desea utilizar? 
1. mm
2. cm
3. m
Escriba la opción: """)

ejercicio = int(input("""¿Que operación desea realizar?
1. Calcular la hipotenusa de un triángulo a partir de sus catetos.
2. Calcular un cateto de un triángulo a partir de el otro cateto y la hipotenusa
3. Calcular el área de un triángulo a partir un cateto y la hipotenusa
4. Calcular el área de un triángulo a partir de dos catetos.
Indica el número de la operación que desee: """))

if ejercicio == 1: 
    cateto1 = float(input("intruduzca el primer cateto: "))
    cateto2 = float(input("introduzca el segundo cateto: "))
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print ("El resultado es", hipotenusa)

elif ejercicio == 2:
    cateto = float(input("introduzca el valor del cateto: "))
    hipotenusa2 = float(input("Introduzca la hipotenusa: "))
    cateto = math.sqrt(cateto**2 - hipotenusa2**2)
    print ("El resultado es", cateto)   

print ("-"*40)
