# lista = [1, 2, 3, 4, 5, 6]
# print(lista)

# heterogenea = [1, "a", 3.14, True]
# print(heterogenea)

# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [8, 9, 10, 11]

# lista3 = lista1 + lista2
# lista4 = lista1 * 2

# print(lista4)
# lista1[0] = 0
# print("Original:", lista1)

# sub_lista = lista1[0:4:2]
# print(sub_lista)
# lista1[0:4] = [9,8,7,6]
# print(lista1)

# lista1.append(7)
# lista1.append(8)
# lista1.append([10, 11, 12])
# print(lista1[-1])
# lista1.insert(0, 99)
# lista1.insert(100, 99)
# lista1.append(99)

# print("Appends:", lista1)

# if 99 in lista1:
#     lista1.remove(99)
# else:
#     print("elemento 99 no está en lista po lo que no se puede eliminar")

# del lista1[0]

# valor = lista1.pop()
# print(valor)
# lista1.clear()
# lista1.sort(reverse = True)
# print("Final:", lista1)

# ---------------------------------
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [8, 9, 10, 11]
# lista1.append(lista2)
# print(lista1)

# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [8, 9, 10, 11]
# lista1.extend(lista2)
# print(lista1)
# ---------------------------------
# cadena = "Hello World"
# nueva_lista = list(cadena)
# nueva_lista = cadena.split(" ")
# nueva_lista2 = cadena.split("0")

# print(nueva_lista)
# print(nueva_lista2)
# ---------------------------------
# cadena = "Hello World"
# nueva_lista = cadena.split("o")
# nueva_cadena = "o".join(nueva_lista)
# print(nueva_lista)
# print(nueva_cadena)
# ---------------------------------
lista6 = ["uno", "dos", "tres", "cuatro"]
indice = lista6.index("dos")

print(indice)