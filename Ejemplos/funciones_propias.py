#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 70
# 
# Erick Marroquin - 123456
# Funciones propias basicas Turtle
# 13/02/24
#==========================================================

import turtle

def cuadrado(tortuga, largo):
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)

def cuadradoRelleno(tortuga, largo, color):
    tortuga.fillcolor(color)

    tortuga.begin_fill()

    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)

    tortuga.end_fill()

ventana = turtle.Screen()
donatello = turtle.Turtle()
donatello.shape("turtle")
donatello.color("red")
donatello.speed(0)


donatello.circle(100)

lado = 150

# donatello.fillcolor("yellow")
# donatello.begin_fill()
# cuadrado(donatello, lado)
# donatello.end_fill()

# donatello.fillcolor("green")
# donatello.begin_fill()
# cuadrado(donatello, (lado / 2))
# donatello.end_fill()

cuadradoRelleno(donatello, lado, "yellow")
cuadradoRelleno(donatello, (lado / 2), "blue")

ventana.exitonclick()
turtle.done()