# O: Open-Closed Principle (Principio de Abierto/Cerrado)
'''El código debe estar abierto para extensión, pero cerrado para modificación.'''

# Codigo Defectuoso
class Calculadora:
    def calcular(self, a, b, operacion):
        if operacion == "sumar":
            return a + b
        elif operacion == "restar":
            return a - b

# Codigo Arreglado
from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Sumar(Operacion):
    def calcular(self, a, b):
        return a + b

class Restar(Operacion):
    def calcular(self, a, b):
        return a - b

# Uso
def operar(operacion, a, b):
    return operacion.calcular(a, b)

print(operar(Sumar(), 5, 3))  # 8
print(operar(Restar(), 5, 3)) # 2



