#Contador de líneas

try:
    nombre_achivo = input("Ingrese el nombre del archivo y sus extensión: ")
    ruta = "C:\\Users\\zeled\\OneDrive\\Documentos\\PROGRAMACIÓN\\Archivo_ejemplo\\"
    mi_archivo = open(ruta + nombre_achivo, 'r')
    lineas = mi_archivo.readlines()
    contador_lineas = len(lineas)
    print(f"El archivo contiene {contador_lineas} líneas")
    mi_archivo.close()
except FileNotFoundError:
    print("El archivo no se enccuentra en la ruta")