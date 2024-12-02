covid = {}
provincia = input("Inserte la provincia: ")
while (provincia != ""):
    casos = int(input("Casos: "))
    covid[provincia] = casos
    provincia = input("Inserte la provincia: ")

print (covid)

promedio = 0
maximo = 0

provincia_maxima = ""

for provincia, casos in covid.items(): 
    promedio += casos
    if casos > maximo: 
        maximo = casos
        provincia_maxima = provincia 

promedio = promedio/len(covid)

print (maximo)
print (promedio)
