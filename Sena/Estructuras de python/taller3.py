# TALLER 3 PYTHON
# AUTOR(A): Germán Daniel Colón Carrasquilla
# FECHA: 12 de abril del 2025

from datetime import date
hoy = date.today()       # fecha actual
print("Hoy es el día: ", hoy)

a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))
a > b
if a > b:
    print("A es mayor o igual a B")
else:
    print("A es menor que B")

print()
curso1 = "Requerimientos"
curso2 = "Algoritmos"
print("El curso1 es: ", curso1)
print("El curso2 es: ", curso2)
if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print("Usted estudia Programación de Software")
else:
    print("Usted estudia otro programa diferente a Programación de Software")

print("**** Final del Análisis del Programa de Formación SENA ****")
print()

frase = input("Digite una oración: ")
print("La frase en mayúsculas es: ", frase.upper())
longitud = len(frase)
print("La longitud de la frase es: ", longitud, "caracteres")
if longitud > 10:
    print("La frase contiene más de 10 caracteres")
elif longitud < 11:
    print("La frase contiene menos de 11 caracteres")

print("FIN")
