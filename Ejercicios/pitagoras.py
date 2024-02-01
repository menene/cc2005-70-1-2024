#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 70
# 
# Erick Marroquin - 123456
# Solicion del ejercicio individual 1 - Pitagoras
# 30/01/24
#==========================================================

import math

modo = input("¿Conoces la hipotenusa? (si o no)")

if modo == "si":
    c = input("Ingrese el valor de la hipotenusa: ")
    c = int(c)

    b = int(input("Ingrese el valor del cateto B: "))

    a = math.sqrt((c * c) - (b * b))

    print("El valor del cateto A es:", a)
else:
    a = input("Ingrese el valor del cateto A: ")
    a = int(a)

    b = int(input("Ingrese el valor del cateto B: "))

    c = math.sqrt((a * a) + (b * b))

    print("El valor de c es:", c)

