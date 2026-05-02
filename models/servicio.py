from abc import ABC, abstractmethod
from .entidad import Entidad
from exceptions import ServicioNoDisponibleError

class Servicio(Entidad, ABC):
    """Clase abstracta para todos los servicios"""
    
    def __init__(self, id, nombre, costo_base):
        super().__init__(id, nombre)
        if costo_base <= 0:
            raise ServicioNoDisponibleError("El costo debe ser mayor a 0")
        self._costo_base = costo_base
    
    @property
    def costo_base(self):
        return self._costo_base
    
    @abstractmethod
    def calcular_precio_final(self):
        pass

class ReservaSala(Servicio):
    def __init__(self, id, nombre, costo_base, capacidad, horas):
        super().__init__(id, nombre, costo_base)
        if capacidad <= 0 or horas <= 0:
            raise ServicioNoDisponibleError("Capacidad y horas deben ser > 0")
        self._capacidad = capacidad
        self._horas = horas
    
    def calcular_precio_final(self):
        if self._capacidad > 50:
            return self._costo_base * self._horas * 1.2
        return self._costo_base * self._horas
    
    def mostrar_info(self):
        return f"Sala #{self._id} | {self._nombre} | Cap: {self._capacidad} | {self._horas}h | ${self.calcular_precio_final()}"

class AlquilerEquipo(Servicio):
    def __init__(self, id, nombre, costo_base, dias):
        super().__init__(id, nombre, costo_base)
        if dias <= 0:
            raise ServicioNoDisponibleError("Los días deben ser > 0")
        self._dias = dias
    
    def calcular_precio_final(self):
        if self._dias > 7:
            return self._costo_base * self._dias * 0.9
        return self._costo_base * self._dias
    
    def mostrar_info(self):
        return f"Equipo #{self._id} | {self._nombre} | {self._dias} días | ${self.calcular_precio_final()}"

class AsesoriaEspecializada(Servicio):
    def __init__(self, id, nombre, costo_base, horas, es_urgente=False):
        super().__init__(id, nombre, costo_base)
        if horas <= 0:
            raise ServicioNoDisponibleError("Las horas deben ser > 0")
        self._horas = horas
        self._es_urgente = es_urgente
    
    def calcular_precio_final(self):
        precio = self._costo_base * self._horas
        if self._es_urgente:
            precio *= 1.5
        return precio
    
    def mostrar_info(self):
        urgencia = "URGENTE" if self._es_urgente else "Normal"
        return f"Asesoría #{self._id} | {self._nombre} | {self._horas}h | {urgencia} | ${self.calcular_precio_final()}"