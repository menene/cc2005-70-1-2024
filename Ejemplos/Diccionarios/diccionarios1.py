# diccionario = {"codigo": "cc2005", "nombre": "Algoritmos", "creditos": 6}
# lista = ["cc2005", "Algoritmos", 6]

# print(diccionario)
# print(lista)

# print(diccionario["codigo"])
# print(lista[0])

# ------------------------------------
# diccionario = {"codigo": "cc2005", "nombre": "Algoritmos", "creditos": 6}
# print(diccionario)

# diccionario["creditos"] = 4
# print(diccionario)

# diccionario["catedratico"] = "Erick Marroquín"
# print(diccionario)

# del diccionario["creditos"]
# print(diccionario)
# ------------------------------------

diccionario = {"codigo": "cc2005", "nombre": "Algoritmos", "creditos": 6}

# obtener el valor de una llave
# print(diccionario.get("codigo"))

# obtener el valor de una llave y si no existe usar el valor default
# print(diccionario.get("seccion", 70))

# obtener todas las llaves de un diccionario
# llaves = diccionario.keys()

# llaves es un objeto iterable
# print(llaves)

# para convertirlo a lista
# llaves = list(llaves)

# print(llaves)

# obtener todos los valores de un diccionario
# valores = diccionario.values()

# valores es un objeto iterable
# print(valores)

# # para convertirlo a lista
# valores = list(valores)

# print(valores)

# # combinar diccionarios
diccionario2 = {"seccion": 600, "catedratico": "Erick Marroquín"}
diccionario.update(diccionario2)

print(diccionario)