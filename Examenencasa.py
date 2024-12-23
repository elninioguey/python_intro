dim = int(input("Introduzca en cuantas dimensiones están los vectores: "))
vec1 = []
vec2 = []
productos = []
print("CALCULO DEL PRODUCTO ESCALAR: ")
print("-"*40)
print ("Introduce el primer vector")
for i in range(dim): 
    v1 = int(input(f'"v_{i}"'))
    vec1.append(v1)
    
print("Introduce el segundo vector")
for i in range(dim):
    v2 = int(input(f'"W_{i}"'))
    vec2.append(v2)

for i in range (dim):
    mult = vec1[i]*vec2[i]
    productos.append(mult)
    
print (productos)
print("-"*40)
print (vec1,"*",vec2,"=",sum(productos))
print("-"*40)

