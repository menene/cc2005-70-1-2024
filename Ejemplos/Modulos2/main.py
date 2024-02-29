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


lado = 200
# dibujar.cuadrado_relleno(cr7, lado, "red")
# area = calculos.area_cuadrado(lado)
# print(area)

# dibujar.triangulo_relleno(cr7, lado, "blue")
# perimetro = calculos.perimetro_triangulo(lado)
# area = calculos.area_triangulo(lado)

# dibujar.hexagono(cr7, 150)
# perimetro = calculos.perimetro_hexagono(lado)
# area = calculos.area_hexagono(lado)

dibujar.poligono(cr7, 3, 100)
dibujar.poligono(cr7, 4, 100)
dibujar.poligono(cr7, 6, 100)
dibujar.poligono(cr7, 8, 100)

perimetro = calculos.perimetro_octagono(lado)
area = calculos.area_octagono(lado)

print("El perímetro es:", perimetro)
print("El área es:", area)

ventana.exitonclick()
turtle.Terminator()