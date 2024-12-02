dic = {}
numero = input("Seleccione el número: ")
while numero.isdigit():
    if numero not in dic: 
        dic[numero] = 1
    else: 
        dic[numero] = dic[numero] +1 #dic[numero] += 1
    numero = input("Seleccione el número: ")


print ("-"*40)

for numero in dic.keys():
    print (numero,":","#"*dic[numero])