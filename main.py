<<<<<<< HEAD
from models.cliente import Cliente
from models.sala import Sala
from models.equipo import Equipo
from models.asesoria import Asesoria
from models.reserva import Reserva
from datetime import datetime

def main():
    print("=== SISTEMA SOFTWARE FJ - SIMULACIÓN 10 OPERACIONES ===\n")
    
    # --- CREACIÓN DE SERVICIOS ---
    # Sala(id, nombre, precio_base, capacidad)
    sala_a = Sala("S001", "Sala A", 100000, 20)
    sala_b = Sala("S002", "Sala B", 80000, 15)
    
    # Equipo(id, nombre, precio_base, modelo)
    equipo1 = Equipo("E001", "Proyector 4K", 50000, "Audiovisual")
    equipo2 = Equipo("E002", "Laptop Gamer", 70000, "Cómputo")
    
    # Asesoria(id, nombre, precio_base, especialidad)
    asesoria1 = Asesoria("A001", "Consultoría Legal", 120000, "Dr. Pérez")
    asesoria2 = Asesoria("A002", "Marketing Digital", 100000, "Ing. López")
    
    servicios = [sala_a, sala_b, equipo1, equipo2, asesoria1, asesoria2]
    
    # --- MOSTRAR SERVICIOS DISPONIBLES ---
    print("--- SERVICIOS DISPONIBLES ---")
    for s in servicios:
        print(f"{s.nombre} - ID: {s.id} - Precio base: ${s.precio_base:,.0f}")
    print()
    
    # --- CREACIÓN DE CLIENTES ---
    # Cliente(id, nombre, email, telefono)
    cliente1 = Cliente("C001", "Katerine", "katerine@mail.com", "3001234567")
    cliente2 = Cliente("C002", "Yobany", "yobany@mail.com", "3007654321")
    cliente3 = Cliente("C003", "Carlos", "carlos@mail.com", "3009876543")
    
    # --- LISTA PARA GUARDAR RESERVAS ---
    reservas_exitosas = []
    total_ingresos = 0
    
    # --- 10 OPERACIONES ---
    operaciones = [
        ("OPERACIÓN 1", cliente1, sala_a, "2026-05-10", 2, 0.15, 0.05),
        ("OPERACIÓN 2", cliente2, equipo1, "2026-05-11", 3, 0.19, 0.10),
        ("OPERACIÓN 3", cliente3, asesoria1, "2026-05-12", 1, 0.19, 0.0),
        ("OPERACIÓN 4", cliente1, sala_b, "2026-05-13", 4, 0.15, 0.05),
        ("OPERACIÓN 5", cliente2, equipo2, "2026-05-14", 5, 0.19, 0.15),
        ("OPERACIÓN 6", cliente3, asesoria2, "2026-05-15", 2, 0.19, 0.05),
        ("OPERACIÓN 7", cliente1, equipo1, "2026-05-16", 1, 0.19, 0.0),
        ("OPERACIÓN 8", cliente2, sala_a, "2026-05-17", 6, 0.15, 0.10),
        ("OPERACIÓN 9", cliente3, sala_b, "2026-05-18", 3, 0.15, 0.0),
        ("OPERACIÓN 10", cliente1, asesoria2, "2026-05-19", 2, 0.19, 0.05),
    ]
    
    for num, cliente, servicio, fecha, horas, impuesto, descuento in operaciones:
        print(f"{num}: Reserva {servicio.nombre} - {cliente.nombre}")
        try:
            reserva = Reserva(cliente, servicio, fecha, horas, impuesto, descuento)
            reservas_exitosas.append(reserva)
            total_ingresos += reserva.costo_total
            print(f"OK - Costo: ${reserva.costo_total:,.1f}\n")
        except Exception as e:
            print(f"ERROR: {e}\n")
    
    # --- RESUMEN FINAL ---
    print("=== RESUMEN FINAL ===")
    print(f"Total de reservas exitosas: {len(reservas_exitosas)}")
    print(f"Total de ingresos: ${total_ingresos:,.2f}")
    print("\nRevisa el archivo logs.txt para ver todos los registros.")
=======
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
>>>>>>> 84aaa0fd267b485a5bfdd2bf9238119ee604ff9d

if __name__ == "__main__":
    main()