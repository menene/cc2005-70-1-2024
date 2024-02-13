#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 70
# 
# Erick Marroquin - 123456
# Introduccion a funciones Turtle
# 13/02/24
#==========================================================

import turtle

ventana = turtle.Screen()

donatello = turtle.Turtle()


donatello.forward(200)
donatello.backward(300)
donatello.right(45)
donatello.forward(200)
donatello.left(190)
donatello.pensize(7)
donatello.forward(200)

pos = donatello.position()
print(pos)

donatello.up()
donatello.goto(100, 200)
donatello.down()

donatello.pensize(10)
donatello.home()

# donatello.clear()
# donatello.reset()


ventana.exitonclick()
turtle.done()