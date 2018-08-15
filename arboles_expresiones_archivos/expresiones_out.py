def guardar_resultado (resultado):
    archivo = open("archivo_sal.txt", "r+")
    contenido = archivo.read()
    final_archivo = archivo.tell()

    archivo.write(resultado)
    archivo.seek(final_archivo)
    nuevo_contenido = archivo.read()

