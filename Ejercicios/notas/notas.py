# ==========================================
# Universidad del valle de Guatemala
# cc2005 - Algoritmos y Programacion Basica
# sección 60
#
# Erick Marroquín
#
# 04/04/24 ultima modificación
#
# Programa para control de notas
# ==========================================

import csv

def promedio(notas):
    n = len(notas)
    suma = 0
    for nota in notas:
        suma += nota

    return (suma / n)

seccion = input("¿Qué sección quieres consultar? (60 o 70)")

if seccion == "60":
    filename = "estudiantes-60.csv"
elif seccion == "70":
    filename = "estudiantes-70.csv"
else:
    filename = ""

estudiantes = []

if filename != "":
    with open(filename, mode="r") as archivo:
        lineas = csv.DictReader(archivo)
            
        for linea in lineas:
            estudiante = {
                "carnet": linea["Carnet"], 
                "nombre": linea["Nombre"], 
                "notas": [],
                "promedio": 0
            }

            estudiantes.append(estudiante)

    print("Importación exitosa del archivo", filename)
else:
    print("Sección no encontrada, no se importa archivo")

opcion = ""
while opcion != "6":
    print("\n=== CONTROL DE NOTAS ===\n")
    print("1. Nuevo estudiante")
    print("2. Agregar nota")
    print("3. Promedio estudiante")
    print("4. Promedio general")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("")

    opcion = input("Seleccione una de las opciones: ")
    # opcion = opcion.lower()

    if opcion == "1":
        # pedirle al usuario los datos del estudiante
        carnet = input("Ingrese el número de carnet: ")
        nombre = input("Ingrese el nombre: ")
        notas = []

        # crear diccionario con datos del estudiante
        # estudiante = {"carnet": carnet, "nombre": nombre, "notas": notas}
        estudiante = {
            "carnet": carnet, 
            "nombre": nombre, 
            "notas": notas,
            "promedio": 0
        }

        # agregar al estudiente a la lista de etudiantes
        estudiantes.append(estudiante)

    elif opcion == "2":
        # solicitar el numero de carnet del estudiante
        # al que se le quieren agregar las notas
        carnet = input("Ingrese el número de carnet: ")

        # recorrer el listado de estudiantes
        for estudiante in estudiantes:
            # ubicar al estudiante al que se le 
            # quieren agregar las notas usando 
            # el número de carnet
            if estudiante["carnet"] == carnet:
                # si el estudiante es ubicado, se le pide
                # la nota al usuario
                nota = int(input("Ingrese la nota a agregar: "))

                # se ingresa la nota al listado de notas
                # de ese estudiante
                estudiante["notas"].append(nota)

                # calcular el promedio usando
                # la funcion 'promdio'
                x = promedio(estudiante["notas"])

                # guarda en el diccionario del usuario
                # su promedio calculado
                estudiante["promedio"] = x
        
    elif opcion == "3":
        # pedir al usuario el numero de carnet
        # de el estudiante a imprimir el promedio
        carnet = input("Ingrese el número de carnet: ")
        
        # ubicar al estudiante al que se le 
        # desea imprimir el priomedio usando 
        # el número de carnet
        for estudiante in estudiantes:
            # si el estudiante es ubicado, se manda
            # su lista de notas a la función que 
            # calcula los promedios
            if estudiante["carnet"] == carnet:
                print("El promedio del estudiante es:", estudiante["promedio"])

    elif opcion == "4":
        # lista vacia para almacenar
        # los promedios de los estudiantes
        lista_promedios = []

        # recorremos la lista de estudiantes
        # y guardamos el valor del promedio
        # en la lista de promedios
        for est in estudiantes:
            lista_promedios.append(est["promedio"])

        # calculamos el promedio de la lista de promedios
        x = promedio(lista_promedios)
        
        print("Promedio General:", x)

    elif opcion == "5":
        print("Listado actual de etudiantes:")
        for e in estudiantes:
            print(e)
    
    elif opcion == "6":
        print("Adios... esperamos que vuelvas pronto")

    else:
        print("Opción inválida... intentalo nuevamente")

if filename != "":
    with open(filename, mode='w') as archivo_csv:
        columnas = ["Carnet", "Nombre"]
        escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)

        escritor.writeheader()
        
        for estudiante in estudiantes:
            escritor.writerow({
                "Carnet": estudiante["carnet"],
                "Nombre": estudiante["nombre"]
            })
