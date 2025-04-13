# TALLER 4 PYTHON
# AUTOR(A): Germán Daniel Colón Carrasquilla
# FECHA: 12 de abril del 2025

from datetime import date
hoy = date.today()         # fecha actual
print("Hoy es el día: ", hoy)
print()

print("EJERCICIO DE LAS CLASES DE TRIÁNGULOS")
a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))
c = int(input("Digite el valor de C: "))

if a == b and a == c and b == c:
    print("EL TRIÁNGULO ES EQUILÁTERO")
else:
    if a == b or b == c or a == c:
        print("EL TRIÁNGULO ES ISÓSCELES")
    else:
        print("EL TRIÁNGULO ES ESCALENO")

print()

animal = input("Digite el nombre de un animal: ")
animal = animal.upper()

if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre: ", animal)
elif animal == "GATO":
    print("Este animal persigue a los ratones: ", animal)
elif animal == "OSO":
    print("Este animal vive en el polo norte: ", animal)
else:
    print("No es PERRO, no es GATO, ni es OSO... es: ", animal)

print("FIN")
