# ==========================================
# Universidad del valle de Guatemala
# CC2005 - Algoritmos y Programacion Basica
# 60
#
# Erick Marroquín
#
# 04/04/24
#
# Programa para control de notas
# ==========================================

def promedio(notas):
    n = len(notas)
    suma = 0
    for nota in notas:
        suma += nota

    return (suma / n)

estudiantes = []

opcion = ""
while opcion != "salir":
    print("\n=== CONTROL DE NOTAS ===\n")
    print("1. Nuevo estudiante")
    print("2. Agregar nota")
    print("3. Promedio estudiante")
    print("4. Promedio general")
    print("Salir para terminar")
    print("")

    opcion = input("Seleccione una de las opciones: ")
    opcion = opcion.lower()

    if opcion == "1":
        carnet = input("Ingrese el número de carnet: ")
        nombre = input("Ingrese el nombre: ")
        notas = []

        estudiante = {"carnet": carnet, "nombre": nombre, "notas": notas}
        estudiantes.append(estudiante)

    elif opcion == "2":
        carnet = input("Ingrese el número de carnet: ")

        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                nota = int(input("Ingrese la nota a agregar: "))
                estudiante["notas"].append(nota)
        
    elif opcion == "3":
        carnet = input("Ingrese el número de carnet: ")

        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                x = promedio(estudiante["notas"])

                print("El promedio del estudiante", estudiante["nombre"], "es de:", x)

    elif opcion == "4":
        print("promedio general")
    elif opcion == "salir":
        print("Adios")
    else:
        print("Opción inválida... intentalo nuevamente")
