class ErrorSistema(Exception):
    """Clase base para todos los errores del sistema"""
    pass

class DatoInvalidoError(ErrorSistema):
    """Error cuando los datos de entrada son inválidos"""
    pass

class ServicioNoDisponibleError(ErrorSistema):
    """Error cuando un servicio no se puede crear"""
    pass

class ReservaInvalidaError(ErrorSistema):
    """Cuando intentan hacer operaciones ilegales con reservas"""
    pass