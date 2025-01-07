def pedir_nombre():
    nombre = input("Introduzca su nombre: ")
    return nombre

def ventas_por_dia():
    dic = {"Lunes":"lunes","Martes":"martes","Miercoles":"miercoles","Jueves":"juesves","Viernes":"viernes"}
    for dia in dic.keys():
        venta = int(input(f'"Introduzca la venta del {dia}: "'))
        dic[dia] = int(venta)
    return dic

def calcular_promedio(dic):
    prom = (sum(dic.values())/5)
    return prom

def mostrar_resumen(nombre,dic,prom):
    print ("","="*40,"\n"," "*15,"RESUMEN"," "*15,"\n","="*40)    
    print ("Nombre del empleado:",nombre)
    print ("Resumen de ventas")
    for dia in dic:
        print (f'{dia}:',dic[dia])
    print ("Promedio diario de ventas:",prom)
    

empleado = pedir_nombre()
ventas = ventas_por_dia()
promedio = calcular_promedio(ventas)
mostrar_resumen(empleado,ventas,promedio)
