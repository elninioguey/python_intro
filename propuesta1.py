def introducir_nombre():
    nombre = input("Introduzca el nombre del comercial: ")
    return nombre

def ventas_por_dia(): 
    L = int(input("Ventas (L): "))
    M = int(input("Ventas (M): "))
    X = int(input("Ventas (X): "))
    J = int(input("Ventas (J): "))
    V = int(input("Ventas (V): "))
    dias = [L,M,X,J,V]
    return dias 

introducir_nombre()
semana = ventas_por_dia()
print ("lista de ventas:",semana)