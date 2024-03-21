# opcion = input("Ingrese salir para terminar: ")
# # opcion = opcion.lower()

# if opcion.lower() == 'salir':
#     print('Saliendo...')
# else:
#     print("No Saliendo...")

# -------------------------------------------
# numero = int(input("Ingrese un número: "))
# numero = input("Ingrese un número: ")
# if not numero.isdigit():
#     print("Dije un número...")
# else:
#     numero = int(numero)

#     if numero == 1:
#         print("Ingresaste 1")
# -------------------------------------------
# numero = ""
# while not numero.isdigit():
#     numero = input("Ingrese un número: ")

# numero = int(numero)
# print(numero, type(numero))
# -------------------------------------------
# nombre = "Erick Francisco Marroquin Rodriguez"
# print("Erick" in nombre)

# contador = 0
# for letra in nombre.lower():
#     if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#         contador += 1

# print(contador)
# -------------------------------------------
# contador = 0
# vocales = 'aeiou'
# for letra in nombre.lower():
#     if letra in vocales:
#         contador += 1

# print(contador)
# -------------------------------------------
nombre = "Erick"
for letra in nombre:
    if letra.islower():
        print(letra, 'Minuscula')
    else:
        print(letra, "Mayuscula")