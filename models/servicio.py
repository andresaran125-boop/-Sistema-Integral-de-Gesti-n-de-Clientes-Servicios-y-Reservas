class Servicio:
    def __init__(self, id, nombre, precio_base):
        self.id = id
        self.nombre = nombre
        self.precio_base = float(precio_base)  # <- Convierte a número sí o sí
    
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        pass
    
    def __str__(self):
        return f"{self.nombre} - ID: {self.id} - Precio base: ${self.precio_base:,.0f}"