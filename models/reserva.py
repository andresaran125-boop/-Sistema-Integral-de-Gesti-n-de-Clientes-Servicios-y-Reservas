from datetime import datetime
<<<<<<< HEAD

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
=======
from .entidad import Entidad
from exceptions import ReservaInvalidaError

class Reserva(Entidad):
    def __init__(self, id, cliente, servicio, fecha):
        super().__init__(id, f"Reserva de {cliente.nombre}")
        
        if fecha < datetime.now():
            raise ReservaInvalidaError("La fecha no puede ser en el pasado")
            
        self._cliente = cliente
        self._servicio = servicio
        self._fecha = fecha
        self._estado = "Pendiente"
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        if valor not in ["Pendiente", "Completada", "Cancelada"]:
            raise ReservaInvalidaError("Estado inválido")
        self._estado = valor
    
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, valor):
        if valor < datetime.now():
            raise ReservaInvalidaError("La fecha no puede ser en el pasado")
        self._fecha = valor
    
    def completar(self):
        self._estado = "Completada"
    
    def cancelar(self):
        self._estado = "Cancelada"
    
    def mostrar_info(self):
        fecha_formateada = self._fecha.strftime("%d/%m/%Y %H:%M")
        return f"Reserva #{self._id} | Cliente: {self._cliente.nombre} | Servicio: {self._servicio.nombre} | Fecha: {fecha_formateada} | Estado: {self._estado}"
>>>>>>> 84aaa0fd267b485a5bfdd2bf9238119ee604ff9d
