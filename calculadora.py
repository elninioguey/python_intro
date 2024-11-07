import math 


#HACER CALCULADORA CON FUNCIONES, DEF Y RETURN


operacion = int(input("""tipo de operaciones: 
1. Suma
2. Resta
3. Multiplicación
4. División
5. Cerrar
Seleccione el tipo de operación (1,2,3,4,5): """))

operando1 = float(input("Seleccione el primer operando: "))
operando2 = float(input("Seleccione el segundo operando: "))


if operacion == 1:
    print (operando1,"+",operando2,"=", operando1+operando2)

elif operacion == 2: 
    print (operando1,"-",operando2,"=",operando1-operando2)

elif operacion == 3: 
    print (operando1, "*",operando2,"=",operando1*operando2)    
