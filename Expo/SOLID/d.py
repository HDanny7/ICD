# Dependency Inversion Principle (Principio de Inversión de Dependencias)
'''Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones.'''

# Codigo Defectuoso
class MySQLDB:
    def conectar(self):
        print("Conectando a MySQL")

class Aplicacion:
    def __init__(self):
        self.db = MySQLDB()  # Dependencia directa

    def ejecutar(self):
        self.db.conectar()

# Codigo Arreglado
from abc import ABC, abstractmethod

class BaseDatos(ABC):
    @abstractmethod
    def conectar(self):
        pass

class MySQLDB(BaseDatos):
    def conectar(self):
        print("Conectando a MySQL")

class PostgreSQLDB(BaseDatos):
    def conectar(self):
        print("Conectando a PostgreSQL")

class Aplicacion:
    def __init__(self, db: BaseDatos):
        self.db = db  # Se inyecta la dependencia

    def ejecutar(self):
        self.db.conectar()

# Uso
app = Aplicacion(PostgreSQLDB())  # Cambiar de BD es fácil
app.ejecutar()
