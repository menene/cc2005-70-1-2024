# CUADRADO
def cuadrado(tortuga, largo):
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)
    tortuga.forward(largo)
    tortuga.left(90)

def cuadrado_relleno(tortuga, largo, color):
    tortuga.fillcolor(color)
    tortuga.begin_fill()

    cuadrado(tortuga, largo)

    tortuga.end_fill()

# TRIANGULO
def triangulo(tortuga, largo):
    tortuga.forward(largo)
    tortuga.left(120)
    tortuga.forward(largo)
    tortuga.left(120)
    tortuga.forward(largo)
    tortuga.left(120)

def triangulo_relleno(tortuga, largo, color):
    tortuga.fillcolor(color)
    tortuga.begin_fill()

    triangulo(tortuga, largo)

    tortuga.end_fill()

# HEXAGONO
def hexagono(tortuga, largo):
    tortuga.forward(largo)
    tortuga.left(60)
    tortuga.forward(largo)
    tortuga.left(60)
    tortuga.forward(largo)
    tortuga.left(60)
    tortuga.forward(largo)
    tortuga.left(60)
    tortuga.forward(largo)
    tortuga.left(60)
    tortuga.forward(largo)
    tortuga.left(60)

# OCTAGONO
def octagono(tortuga, largo):
    tortuga.forward(largo)
    tortuga.left(45)
    tortuga.forward(largo)
    tortuga.left(45)
    tortuga.forward(largo)
    tortuga.left(45)
    tortuga.forward(largo)
    tortuga.left(45)
    tortuga.forward(largo)
    tortuga.left(45)
    tortuga.forward(largo)
    tortuga.left(45)
    tortuga.forward(largo)
    tortuga.left(45)
    tortuga.forward(largo)
    tortuga.left(45)

def poligono(tortuga, lados, largo):
    if lados == 3:
        triangulo(tortuga, largo)
    elif lados == 4:
        cuadrado(tortuga, largo)
    elif lados == 6:
        hexagono(tortuga, largo)
    elif lados == 8:
        octagono(tortuga, largo)
