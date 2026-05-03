from datetime import datetime

class Reserva:
    contador_id = 1
    
    def __init__(self, cliente, servicio, fecha, horas, impuesto=0, descuento=0):
        self.id = Reserva.contador_id
        Reserva.contador_id += 1
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.horas = horas
        self.impuesto = impuesto
        self.descuento = descuento
        self.estado = "Pendiente"
        self.fecha_creacion = datetime.now()
        self.costo_total = self.servicio.calcular_costo(horas, impuesto, descuento)
    
    def __str__(self):
        return f"Reserva #{self.id}: {self.cliente.nombre} - {self.servicio.nombre} - {self.fecha} - {self.horas}h - Total: ${self.costo_total:,.0f}"