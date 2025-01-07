import saludos

def introducir_nombre():
    nombre = input("Introduzca su nombre: ")
    return nombre

def elegir_idioma():
    idioma = int(input("""idioma preferido:
1. Español
2. Inglés
3. Francés
idioma: """))
    return idioma

def saludo_final(nombre,idioma):
    if idioma == 1: 
        saludos.saludo_español(nombre)

    elif idioma == 2:
        saludos.saludo_ingles(nombre)

    elif idioma == 3: 
        saludos.saludo_frances(nombre)

    else:
        print("seleccione un idioma válido")

nombre = introducir_nombre()
idioma = elegir_idioma()
saludo_final(nombre,idioma)





