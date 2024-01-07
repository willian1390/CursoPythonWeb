with open("archivos\\leer.txt", 'a', encoding="UTF-8") as archivo: #abrir el archivo con el nombre de variable archivo, a agrega sin sobre escribir

    for i in range(5):
        archivo.write(f"linea {i+1} agregada \n")

