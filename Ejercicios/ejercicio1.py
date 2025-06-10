#Diario personal

import datetime
ruta = "C:\\Users\\zeled\\OneDrive\\Documentos\\PROGRAMACIÓN\\Archivo_ejemplo\\"
mi_archivo = open(ruta + 'diario.txt', 'a')
usuario_entrada = input("Escribe algo para tu diario: ")
fecha = datetime.datetime.now()
contenido = mi_archivo.read()
print(f"La fecha y hora atual es: {fecha}")
print(f"El texxto ingresado es {usuario_entrada}")
mi_archivo.close()
print("La entrada se guardo correctamente.")