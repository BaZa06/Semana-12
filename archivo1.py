try:
    mi_ruta = "C:\\Users\\zeled\\OneDrive\\Documentos\\PROGRAMACIÓN\\Archivo_ejemplo\\"
    mi_archivo = open(mi_ruta + 'Datos.txt', 'r' )
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close()
except FileNotFoundError:
    print("El archivo no se enccuentra en la ruta especificada")