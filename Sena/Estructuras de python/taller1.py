''' TALLER 1 PYTHON
AUTOR(A): RAINER ZULUAGA REYES
FECHA: 11 de abril del 2025'''

from datetime import date

hoy = date.today()
print("Hoy es el día: ", hoy)

n1 = int(input("Digite el primer número:\n")) # El \n hace que al escribir el numero quede debajo
n2 = int(input("Digite el segundo número:\n"))

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

print("La suma es = ", suma)
print("La resta es = ", resta)
print("La multiplicación es = ", producto)
print("La división es = ", division)
print("FIN")
