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

if __name__ == "__main__":
    main()