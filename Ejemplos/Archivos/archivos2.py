import csv

estudiantes = []
with open("file.csv", mode="r") as archivo:
    lineas = csv.DictReader(archivo)
        
    for linea in lineas:
        estudiantes.append(linea)
        # print(linea)
        # print(linea["Columna 1"], linea["Columna 2"])

print(estudiantes)