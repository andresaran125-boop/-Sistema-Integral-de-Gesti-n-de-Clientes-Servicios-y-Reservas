from datetime import datetime, timedelta
from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from models.reserva import Reserva
from exceptions import ReservaInvalidaError
from logger import registrar_error

def main():
    try:
        print("=== SISTEMA DE RESERVAS ===")
        
        # 1. Crear clientes
        c1 = Cliente(1, "Juan Pérez", "juan@mail.com", "3001234567")
        c2 = Cliente(2, "Ana López", "ana@mail.com", "3009876543")
        print("\n1. Clientes creados:")
        print(f" - {c1.mostrar_info()}")
        print(f" - {c2.mostrar_info()}")
        
        # 2. Crear servicios
        sala1 = ReservaSala(1, "Sala VIP", 50000, 60, 3)
        equipo1 = AlquilerEquipo(2, "Proyector 4K", 80000, 5)
        asesoria1 = AsesoriaEspecializada(3, "Marketing Digital", 120000, 2, True)
        print("\n2. Servicios creados:")
        print(f" - {sala1.mostrar_info()}")
        print(f" - {equipo1.mostrar_info()}")
        print(f" - {asesoria1.mostrar_info()}")
        
        # 3. Lista de servicios
        servicios = [sala1, equipo1, asesoria1]
        print("\n3. Lista de servicios:")
        for servicio in servicios:
            print(f" - {servicio.mostrar_info()}")
        
        # 4. Crear reservas con datetime correcto
        fecha1 = datetime.now() + timedelta(days=1)
        fecha2 = datetime.now() + timedelta(days=2)
        fecha3 = datetime.now() + timedelta(days=3)
        
        r1 = Reserva(1, c1, sala1, fecha1)
        r2 = Reserva(2, c2, equipo1, fecha2)
        r3 = Reserva(3, c1, asesoria1, fecha3)
        reservas = [r1, r2, r3]
        
        print("\n4. Reservas creadas:")
        for reserva in reservas:
            print(f" - {reserva.mostrar_info()}")
        
        # 5. Completar una reserva
        print("\n5. Completando reserva...")
        r1.completar()
        print(f"Estado actualizado: {r1.mostrar_info()}")
        
        # 6. Probar excepción
        print("\n6. Probando fecha inválida...")
        try:
            fecha_pasada = datetime.now() - timedelta(days=1)
            Reserva(99, c1, sala1, fecha_pasada)
        except ReservaInvalidaError as e:
            registrar_error(e)
            print(f"Excepción capturada: {e}")
        
        print("\n=== FIN DEL SISTEMA ===")
        
    except Exception as e:
        registrar_error(e)
        print(f"ERROR CRÍTICO: {e}")

if __name__ == "__main__":
    main()