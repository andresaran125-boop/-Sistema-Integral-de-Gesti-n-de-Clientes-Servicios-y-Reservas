from datetime import datetime
from .entidad import Entidad
from exceptions import ReservaInvalidaError

class Reserva(Entidad):
    """Gestiona las reservas de servicios"""
    
    def __init__(self, id, cliente, servicio, fecha):
        super().__init__(id, f"Reserva de {cliente.nombre}")
        if fecha < datetime.now():
            raise ReservaInvalidaError("La fecha no puede ser en el pasado")
        self._cliente = cliente
        self._servicio = servicio
        self._fecha = fecha
        self._estado = "Pendiente"
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def servicio(self):
        return self._servicio
    
    @property
    def fecha(self):
        return self._fecha
    
    @property
    def estado(self):
        return self._estado
    
    def confirmar(self):
        self._estado = "Confirmada"
    
    def cancelar(self):
        self._estado = "Cancelada"
    
    def mostrar_info(self):
        return f"Reserva #{self._id} | Cliente: {self._cliente.nombre} | Servicio: {self._servicio.nombre} | Fecha: {self._fecha.strftime('%d/%m/%Y')} | Estado: {self._estado}"