# S: Single Responsibility Principle (Principio de Responsabilidad Única)
'''Una clase solo debe tener una razon para cambiar.'''

# Codigo Defectuoso
class Reporte:
    def __init__(self, datos):
        self.datos = datos

    def generar_reporte(self):
        return f"Reporte: {self.datos}"

    def guardar_pdf(self):
        print("Guardando reporte en PDF...")

# Codigo Arreglado
'''class Reporte:
    def __init__(self, datos):
        self.datos = datos

    def generar_reporte(self):
        return f"Reporte: {self.datos}"

class GuardarArchivo:
    def guardar_pdf(self, reporte):
        print(f"Guardando '{reporte}' en PDF...")'''




