with open("archivos\\leer.txt") as archivo: #abrir el archivo con el nombre de variable archivo
    contenido = archivo.read() #leer el archivo con read()
    print(contenido) #imprimir el archivo

    #no es necesario cerrar el archivo con with