def guardar_resultado (resultado):
    archivo = open("expresionesout.txt", "r+")
    contenido = archivo.read()
    final_archivo = archivo.tell()

    archivo.write(resultado+"\n")
    archivo.seek(final_archivo)
    nuevo_contenido = archivo.read()
