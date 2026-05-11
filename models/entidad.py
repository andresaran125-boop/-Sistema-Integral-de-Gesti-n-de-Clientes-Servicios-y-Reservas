from abc import ABC, abstractmethod

class Entidad(ABC):
    """Clase abstracta base. No se puede crear sola."""
    
    def __init__(self, id, nombre):
        if id <= 0:
            raise ValueError("El ID debe ser mayor a 0")
        if not nombre or len(nombre) < 3:
            raise ValueError("El nombre debe tener mínimo 3 letras")
        
        self._id = id
        self._nombre = nombre
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @abstractmethod
    def mostrar_info(self):
        """Las clases hijas están obligadas a crear este método"""
        pass