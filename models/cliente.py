from .entidad import Entidad
from exceptions import DatoInvalidoError

class Cliente(Entidad):
    """Hereda de Entidad"""
    
    def __init__(self, id, nombre, email, telefono):
        super().__init__(id, nombre)
        self.email = email
        self.telefono = telefono
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise DatoInvalidoError("Email inválido")
        self._email = valor
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit() or len(valor) != 10:
            raise DatoInvalidoError("Teléfono debe tener 10 dígitos")
        self._telefono = valor
    
    def mostrar_info(self):
        return f"Cliente #{self._id} | {self._nombre} | {self._email} | {self._telefono}"