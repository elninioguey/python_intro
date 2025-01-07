def creacion_diccionario():
    dic = {}
    return dic

def añadir_numeros(dic):
    numero = input("Seleccione el número: ")
    while numero.isdigit():
        if numero not in dic: 
            dic[numero] = 1
        else: 
            dic[numero] = dic[numero] +1 #dic[numero] += 1
        numero = input("Seleccione el número: ")
    return numero

def imprimir_tabla(dic,numero):
    for numero in dic.keys():
        print (numero,":","#"*dic[numero])

print ("-"*40)
dicc = creacion_diccionario()
numeros = añadir_numeros(dicc)
print ("-"*40)
imprimir_tabla(dicc,numeros)
print ("-"*40)
