archivo = open("archivos\\leer.txt", encoding="UTF-8") #variable archivo contiene la direccion o ruta del archivo a leer
#print(archivo.read()) #imprime en consola lo que esta dentro de la variable archivo y lo lee con read()
lineas = archivo.readlines() #imprime en una sola linea todo el texto
#linea = archivo.readline() # lee una sola linea, readline(5) lee las primeras 5 letras
print(lineas)
archivo.close() #cerrar el archivo