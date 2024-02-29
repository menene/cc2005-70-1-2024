#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 70
# 
# Erick Marroquin - 123456
# Funciones propias en modulos
# 22/02/24
#==========================================================

import turtle
import dibujar
import calculos

ventana = turtle.Screen()
cr7 = turtle.Turtle()
cr7.shape("turtle")
cr7.color("red")
cr7.speed(9)


# dibujar.poligono(cr7, 3, 100)
# dibujar.poligono(cr7, 12, 50)
# dibujar.poligono(cr7, 6, 100)
# dibujar.poligono(cr7, 8, 100)
opcion = "lo que sea"
while opcion != "salir":
    opcion = input("¿Qué figura quieres dibujar? ")

    if opcion == "triangulo":
        dibujar.poligono(cr7, 3, 100)
    elif opcion == "cuadrado":
        dibujar.poligono(cr7, 4, 100)
    elif opcion == "pentagono":
        dibujar.poligono(cr7, 5, 100)
    elif opcion == "salir":
        print("Hasta luego 👋🏽")
        turtle.Terminator()
    else:
        print("Figura no reconocida... intentalo nuevamente")


