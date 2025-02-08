# L: Liskov Substitution Principle (Principio de Sustitución
'''Las subclases deben poder reemplazar a sus clases base sin afectar el programa.'''

# Codigo Defectuoso
class Ave:
    def volar(self):
        print("Puedo volar")

class Pinguino(Ave):
    def volar(self):
        raise Exception("No puedo volar")

# Codigo Arreglado
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("Puedo volar")

class Pinguino(Ave):
    def nadar(self):
        print("Puedo nadar")



