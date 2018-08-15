
def leer_archivo():
    archivo = open("archivo_ent.txt")

    for linea in archivo.readlines():
        print (linea)
        lista = linea.split(" ")
    print(lista)
    archivo.close()
    return lista



