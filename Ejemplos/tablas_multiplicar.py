x = int(input("Ingrese el número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = (x * i)
    print(x, " x ", i, "=", resultado)