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

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        registrar_error(e)
        print(f"Error crítico no controlado en el sistema: {e}")