import math 

# COMPARTIDAS
def apotema(lados, largo):
    angulo = (360 / (2 * lados))
    res = largo / (2 * math.tan(angulo))
    if res < 0:
        res = res * -1

    return res

# CUADRADO
def perimetro_cuadrado(largo):
    return largo * 4

def area_cuadrado(largo):
    area = largo * largo
    return area

# TRIANGULO
def area_triangulo(largo):
    b = (largo / 2)
    altura = math.sqrt(largo ** 2 - b ** 2)

    area = (largo * altura) / 2

    return area

def perimetro_triangulo(largo):
    return largo * 3

# HEXAGONO
def perimetro_hexagono(largo):
    return largo * 6

def area_hexagono(largo):
    perimetro = perimetro_hexagono(largo)
    a = apotema(6, largo)
    area = (perimetro * a) / 2

    return area

# OCTAGONO
def perimetro_octagono(largo):
    return largo * 8

def area_octagono(largo):
    perimetro = perimetro_octagono(largo)
    a = apotema(8, largo)
    area = (perimetro * a) / 2

    return area