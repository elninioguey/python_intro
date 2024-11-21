def crear_lista():
    contador = int(input("¿Cuántos números desea insertar?: "))
    num = []
    for _ in range(contador):
        numero = int(input("Número: "))
        num.append(numero)
    return num

def seleccion(): 
        print ("-"*40)
        opcion = int(input("""1. Sumatorio
    2. Cuadrado de cada número
    3. Promedio 
    Opción: """))
        return opcion

def operaciones(num,opcion):
    #sumatorio
    if opcion == 1: 
        print ("Sumatorio: ", sum(num))
    #cuadrado
    elif opcion == 2: 
        contador = len(num)

        for i in range (contador):
            cuadrado = num[0]
            print (cuadrado, "->", cuadrado**2)
            num.pop(0)
    #promedioç
    elif opcion == 3: 
        print("Promedio:",sum(num)/contador)
    else: 
        print("Opción no válida.")


