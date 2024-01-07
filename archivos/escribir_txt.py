with open("archivos\\leer.txt", 'w', encoding="UTF-8") as archivo: #abrir el archivo con el nombre de variable archivo, w escribe en el archivo y si no lo encuentra lo crea
    #archivo.write("HOOLA") #sobreescribe el archivo, borra el contenido y coloca lo ingresado
    archivo.writelines(["linea1\n", "linea2\n"])#escribe lineas usando \n, tambien sobreescribe
