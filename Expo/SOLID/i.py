# I: Interface Segregation Principle (Principio de Segregación de Interfaces)
'''No obligues a una clase a implementar métodos que no necesita.'''

# Codigo Defectuoso
class Trabajador:
    def trabajar(self):
        pass

    def comer(self):
        pass

class Robot(Trabajador):
    def comer(self):
        raise Exception("¡No como!")

# Codigo Arreglado
class Trabajador:
    def trabajar(self):
        pass

class Comedor:
    def comer(self):
        pass

class Humano(Trabajador, Comedor):
    def trabajar(self):
        print("Estoy trabajando")

    def comer(self):
        print("Estoy comiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("Soy un robot trabajando")



