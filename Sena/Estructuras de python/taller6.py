# TALLER 6 PYTHON
# AUTOR(A): Germán Daniel Colón Carrasquilla
# FECHA: 12 de abril del 2025

from datetime import date
hoy = date.today()         # fecha actual
print("Hoy es el día: ", hoy)
print()

print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
print("****Ciclo controlado por contador")
num1 = int(input("Digite un número: "))
i = 1
while i <= num1:
    print(i)
    i += 1
print("Fin del ciclo")

print()
print("****Ciclo controlado por evento")
numero1 = 5
numero2 = int(input("Digite un número de 1 a 10: "))
while numero2 != numero1:
    numero2 = int(input("Digite un número de 1 a 10: "))
print("¡Acertaste en el intento No.", i, "!")
print("Fin del ciclo")

print()
print("****Ciclo abortado con la sentencia break")
amistad = input("Digite nombre de una amistad: ")
amistad = amistad.upper()
for character in amistad:
    print(character)
    if character == "A":
        break
print("Fin del ciclo")

print("FIN")
