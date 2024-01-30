#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 70
# 
# Erick Marroquin - 123456
# Solicion del ejercicio individual 1
# 30/01/24
#==========================================================
import math

a = input("Ingrese el valor del cateto A: ")
print(type(a))
a = int(a)
print(type(a))

b = int(input("Ingrese el valor del cateto B: "))

c = math.sqrt((a * a) + (b * b))

print("El valor de c es:", c)