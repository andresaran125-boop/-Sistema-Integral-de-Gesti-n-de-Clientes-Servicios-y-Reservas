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
from models.servicio import Servicio, ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from models.reserva import Reserva
from exceptions import DatoInvalidoError, ServicioNoDisponibleError, ReservaInvalidaError
from logger import registrar_error

# --- DATOS EN MEMORIA ---
clientes_registrados = []
reservas_creadas = []

# ReservaSala: id, nombre, costo_base, capacidad, horas
servicios_disponibles = [
    ReservaSala(1, "Sala VIP", 200000, 10, 4),  # 10 personas, 4 horas
    AlquilerEquipo(2, "Proyector 4K", 50000, 3),  # 3 días
    AsesoriaEspecializada(3, "Asesoría Legal", 100000, 2, False)  # 2 horas, no urgente
]

# --- FUNCIONES DE VALIDACIÓN ---
def solicitar_numero_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise DatoInvalidoError("El valor debe ser un número positivo mayor a cero.")
            return valor  # CORREGIDO: faltaba 'valor'
        except ValueError:
            print("Error: Solo se permiten números enteros.")
        except DatoInvalidoError as e:
            print(f"Error: {e}")

def solicitar_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: Este campo es obligatorio, no puede estar vacío.")

def solicitar_email_valido(mensaje):
    while True:
        email = input(mensaje).strip()
        if "@" in email and "." in email.split("@")[-1]:
            return email
        print("Error: Ingrese un email válido que contenga @ y dominio.")

# --- FUNCIONES DEL MENÚ ---
def registrar_cliente():
    print("\n--- Registro de Nuevo Cliente ---")
    try:
        id_cliente = solicitar_numero_entero("ID del cliente: ")
        if any(c.id == id_cliente for c in clientes_registrados):
            raise DatoInvalidoError("Ya existe un cliente registrado con ese ID.")
        
        nombre = solicitar_texto_no_vacio("Nombre completo: ")
        email = solicitar_email_valido("Correo electrónico: ")
        telefono = solicitar_texto_no_vacio("Número de teléfono: ")

        nuevo_cliente = Cliente(id_cliente, nombre, email, telefono)
        clientes_registrados.append(nuevo_cliente)
        print(f"Cliente registrado correctamente: {nuevo_cliente.mostrar_info()}")

    except DatoInvalidoError as e:
        print(f"Error: {e}")
    except Exception as e:
        registrar_error(e)
<<<<<<< HEAD
        print(f"Error inesperado al registrar cliente: {e}")

def consultar_servicios():
    print("\n--- Servicios Disponibles ---")
    if not servicios_disponibles:
        print("No hay servicios disponibles por el momento.")
        return
    for servicio in servicios_disponibles:
        print(f" - {servicio.mostrar_info()}")

def crear_reserva():
    print("\n--- Crear Nueva Reserva ---")
    if not clientes_registrados:
        print("Error: No se puede crear una reserva. Debe registrar al menos un cliente primero.")
        return
    
    try:
        print("\nClientes disponibles:")
        for i, cliente in enumerate(clientes_registrados, 1):
            print(f"{i}. {cliente.nombre}")
        
        num_cliente = solicitar_numero_entero("Digite el número del cliente: ")
        if not (1 <= num_cliente <= len(clientes_registrados)):
            raise DatoInvalidoError("El número de cliente seleccionado no es válido.")
        cliente_seleccionado = clientes_registrados[num_cliente - 1]

        print("\nServicios disponibles:")
        for i, servicio in enumerate(servicios_disponibles, 1):
            print(f"{i}. {servicio.nombre} - ${servicio.calcular_precio_final()}")
        
        num_servicio = solicitar_numero_entero("Digite el número del servicio: ")
        if not (1 <= num_servicio <= len(servicios_disponibles)):
            raise DatoInvalidoError("El número de servicio seleccionado no es válido.")
        servicio_seleccionado = servicios_disponibles[num_servicio - 1]

        dias_futuro = solicitar_numero_entero("¿Dentro de cuántos días será la reserva?: ")
        fecha_reserva = datetime.now() + timedelta(days=dias_futuro)
        
        nuevo_id = len(reservas_creadas) + 1
        nueva_reserva = Reserva(nuevo_id, cliente_seleccionado, servicio_seleccionado, fecha_reserva)  # CORREGIDO: línea completa
        reservas_creadas.append(nueva_reserva)
        print("\n¡Reserva creada exitosamente!")
        print(nueva_reserva.mostrar_info())

    except DatoInvalidoError as e:
        print(f"Error: {e}")
    except ReservaInvalidaError as e:
        print(f"Error en la reserva: {e}")
    except ServicioNoDisponibleError as e:
        print(f"Error al crear reserva: {e}")
    except Exception as e:
        registrar_error(e)
        print(f"Error inesperado al crear la reserva: {e}")

def listar_reservas():
    print("\n--- Listado de Todas las Reservas ---")
    if not reservas_creadas:
        print("Aún no se ha creado ninguna reserva.")
        return
    for reserva in reservas_creadas:
        print(reserva.mostrar_info())

# --- BUCLE PRINCIPAL ---
def main():
    while True:
        print("\n=== SISTEMA DE RESERVAS INTERACTIVO ===")
        print("1. Registrar nuevo cliente")
        print("2. Consultar servicios disponibles")
        print("3. Crear nueva reserva")
        print("4. Listar todas las reservas")
        print("5. Salir del sistema")
        
        opcion = input("Seleccione una opción del menú: ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            consultar_servicios()
        elif opcion == "3":
            crear_reserva()
        elif opcion == "4":
            listar_reservas()
        elif opcion == "5":
            print("Cerrando el sistema de reservas. Hasta pronto.")
            break
        else:
            print("Error: Opción inválida. Por favor seleccione un número del 1 al 5.")
=======
        print(f"ERROR CRÍTICO: {e}")
>>>>>>> 84aaa0fd267b485a5bfdd2bf9238119ee604ff9d
>>>>>>> efbb406a20492003ec4645d064802ce69a208f04

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        registrar_error(e)
        print(f"Error crítico no controlado en el sistema: {e}")