from models.servicio import Servicio

class Equipo(Servicio):
    def __init__(self, id, nombre, precio_base, modelo):
        super().__init__(id, nombre, precio_base)
        self.modelo = modelo
    
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        if impuesto > 1:
            impuesto = impuesto / 100
        if descuento > 1:
            descuento = descuento / 100
        
        costo_base = self.precio_base * horas
        total_impuesto = costo_base * impuesto
        total_descuento = costo_base * descuento
        return costo_base + total_impuesto - total_descuento