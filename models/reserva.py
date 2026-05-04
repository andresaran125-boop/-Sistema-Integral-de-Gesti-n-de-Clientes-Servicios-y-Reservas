from datetime import datetime
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