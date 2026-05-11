from datetime import datetime
from models.cliente import Cliente
from models.servicio import Servicio
from exceptions import ReservaInvalidaError

class Reserva:
    def __init__(self, id: int, cliente: Cliente, servicio: Servicio, fecha: datetime):
        self.id = id
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.validar_reserva()

    def validar_reserva(self):
        if self.fecha < datetime.now():
            raise ReservaInvalidaError("No se puede reservar en una fecha pasada.")
        if self.servicio is None:
            raise ReservaInvalidaError("El servicio no puede ser nulo.")
        if self.cliente is None:
            raise ReservaInvalidaError("El cliente no puede ser nulo.")

    def calcular_total(self) -> float:
        return self.servicio.calcular_costo()

    def mostrar_info(self) -> str:
        fecha_str = self.fecha.strftime("%d/%m/%Y %H:%M")
        return (
            f"Reserva ID: {self.id}\n"
            f"  Cliente: {self.cliente.nombre}\n"
            f"  Servicio: {self.servicio.nombre}\n"
            f"  Fecha: {fecha_str}\n"
            f"  Total: ${self.calcular_total():,.0f}"
        )