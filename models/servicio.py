from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, id: int, nombre: str, costo_base: float):
        self.id = id
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def mostrar_info(self) -> str:
        pass

class ReservaSala(Servicio):
    def __init__(self, id: int, nombre: str, costo_base: float, capacidad: int, horas: int):
        super().__init__(id, nombre, costo_base)
        self.capacidad = capacidad
        self.horas = horas

    def calcular_costo(self) -> float:
        return self.costo_base * self.horas

    def mostrar_info(self) -> str:
        return f"Sala: {self.nombre} - Capacidad: {self.capacidad} - ${self.calcular_costo():,.0f} por {self.horas}h"

class AlquilerEquipo(Servicio):
    def __init__(self, id: int, nombre: str, costo_base: float, dias: int):
        super().__init__(id, nombre, costo_base)
        self.dias = dias

    def calcular_costo(self) -> float:
        return self.costo_base * self.dias

    def mostrar_info(self) -> str:
        return f"Equipo: {self.nombre} - ${self.calcular_costo():,.0f} por {self.dias} días"

class AsesoriaEspecializada(Servicio):
    def __init__(self, id: int, nombre: str, costo_base: float, horas: int, es_virtual: bool):
        super().__init__(id, nombre, costo_base)
        self.horas = horas
        self.es_virtual = es_virtual

    def calcular_costo(self) -> float:
        recargo = 0.9 if self.es_virtual else 1.0
        return self.costo_base * self.horas * recargo

    def mostrar_info(self) -> str:
        tipo = "Virtual" if self.es_virtual else "Presencial"
        return f"Asesoría: {self.nombre} - {tipo} - ${self.calcular_costo():,.0f} por {self.horas}h"