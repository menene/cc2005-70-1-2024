password = input("Ingrse una contraseña: ")
calificacion = 0

minusculas = 0
mayusculas = 0
numeros = 0
simbolos = 0
simbolos_aceptados = '.,;:+-'
for letra in password:
    if letra.islower():
        minusculas += 1
    elif letra.isupper():
        mayusculas += 1

    if letra.isdigit():
        numeros += 1

    if letra in simbolos_aceptados:
        simbolos += 1

if mayusculas > 0 and minusculas > 0:
    calificacion += 10

if numeros > 0:
    calificacion += 10

if len(password) >= 10:
    calificacion += 5

if simbolos > 0:
    calificacion += 5

if password.count(" ") > 0:
    calificacion -= 5

if "password" in password.lower():
    calificacion -= 50

print("La calificación de tu password es de:", calificacion)