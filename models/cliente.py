class Cliente:
    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def __str__(self):
        return f"{self.nombre} - ID: {self.id} - Email: {self.email} - Tel: {self.telefono}"