import calculos

def poligono(tortuga, lados, largo):
    angulo = calculos.angulo(lados)

    x = 1
    while x <= lados:
        tortuga.forward(largo)
        tortuga.left(angulo)
        x = x + 1
