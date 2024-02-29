x = int(input("Ingrese el número para ver su tabla de multiplicar: "))
limite = int(input("Ingrese hasta donde quiere llegar: "))

for i in range(limite + 1):
    resultado = (x * i)
    print(x, " x ", i, "=", resultado)