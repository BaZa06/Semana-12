#Diario personal

import datetime
ruta = "C:\\Users\\zeled\\OneDrive\\Documentos\\PROGRAMACIÓN\\Archivo_ejemplo\\"
mi_archivo = open(ruta + 'diario.txt', 'a')
usuario_entrada = input("Escribe algo para tu diario: ")
fecha = datetime.datetime.now()
mi_archivo.write(f"\n{fecha} - \n{usuario_entrada}")
contenido = mi_archivo.read()
mi_archivo.close()
print("La entrada se guardo correctamente.")