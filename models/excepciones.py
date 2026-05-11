class HorasInvalidasError(Exception):
    """Se lanza cuando las horas son <= 0"""
    def __init__(self, mensaje="Las horas deben ser mayor a 0"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class CapacidadExcedidaError(Exception):
    """Se lanza cuando se intenta reservar más de la capacidad"""
    def __init__(self, mensaje="Capacidad excedida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ServicioNoDisponibleError(Exception):
    """Se lanza cuando el servicio no está disponible"""
    def __init__(self, mensaje="Servicio no disponible"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ReservaDuplicadaError(Exception):
    """Se lanza cuando ya existe una reserva idéntica"""
    def __init__(self, mensaje="Reserva duplicada"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class SalaNoDisponibleError(Exception):
    """Se lanza cuando la sala no está disponible en ese horario"""
    def __init__(self, mensaje="Sala no disponible"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)