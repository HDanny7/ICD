# TALLER 5 PYTHON
# AUTOR(A): Germán Daniel Colón Carrasquilla
# FECHA: 12 de abril del 2025

from datetime import date
hoy = date.today()          # fecha actual
print("Hoy es el día: ", hoy)
print()

print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segundo número (mayor): "))
print("Ciclo para el primer número")
for i in range(num1):
    print(i)
print("Fin del ciclo")

print()

print("Ciclo desde el primer número hasta el segundo número")
for i in range(num1, num2):
    print(i)
print("Fin del ciclo")

print()

print("Ciclo desde el primero hasta el segundo número con incrementos de 2")
for i in range(num1, num2, 2):
    print(i)
print("Fin del ciclo")

print()

empresa = input("Digite nombre de una empresa: ")
empresa = empresa.lower()
for character in empresa:
    print(character)
print("Fin del ciclo")

print()
print("FIN")

