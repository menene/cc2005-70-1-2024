#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 70
# 
# Erick Marroquin - 123456
# Uso de variables y expresiones
# 30/01/24
#==========================================================

dia = 4
hora = 7.1

clase_progra = (dia == 2 or dia == 4) and (hora >= 7 and hora <= 8.5)

# if (dia == 2) and (hora >= 7 and hora <= 8.5):
if clase_progra:
    print("Voy a clase")
else:
    print("Me salve")

if not clase_progra:
    print("Me salve")
else:
    print("Voy a clase")
    