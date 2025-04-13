# TALLER 2 PYTHON
# AUTOR(A): Germán Daniel Colón Carrasquilla
# FECHA: 11 de abril del 2025

from datetime import date  # fecha actual
hoy = date.today()
print("Hoy es el día: ", hoy)

a = int(input("Digite el primer número:\n"))
b = int(input("Digite el segundo número:\n"))
c = int(input("Digite el tercer número:\n"))
x = [a, b, c]

print("El valor máximo es:\n", max(x))
print("El valor mínimo es:\n", min(x))
print("La suma de los 3 números es: ", sum(x))

z = float(input("Digite un número con decimales:\n"))
redondo = round(z)
print("El valor de z, z redondeado es:\n", redondo)
print()

frase = input("Digite una oración:\n")
print("La frase en mayúscula es: ", frase.upper())
print("La frase en minúscula es: ", frase.lower())
print("La frase con mayúscula inicial es: ", frase.capitalize())
print("La frase con palabras en mayúsculas es: ", frase.title())
print("La longitud de la frase es: ", len(frase), "caracteres")
print("FIN")
