calificacion = int(input("Ingrese su calificación"))

# if calificacion < 61:
#     print("lo sentimos, ud. perdió")
# elif calificacion > 85:
#     print("usted ganó con honores")
# else:
#     print("usted ganó")

if calificacion >= 61:
    if calificacion >= 85:
        print("usted ganó con honores")
    else:
        print("usted ganó")
else:
    print("usted perdió")