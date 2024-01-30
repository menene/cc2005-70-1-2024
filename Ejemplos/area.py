#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 70
# 
# Erick Marroquin - 123456
# Calcula el area de un cuadrado
# 25/01/24
#==========================================================

# constante pi
pi = 3.14159265 

# pedir y convertir el largo
largo = input("Ingrese el largo del cuadrado: ")
largo = int(largo)

# pedir y convertir el alto
alto = int(input("ingrese el alto del cuadrado: "))

#calcular el area
area = largo * alto

#mostrar el resultado
print("")
# print("El area de un cuadrado de alto " + str(alto) + " y de largo " + str(largo) + " es:", area)
print("El area de un cuadrado de alto", alto, "y de largo", largo, "es:", area)