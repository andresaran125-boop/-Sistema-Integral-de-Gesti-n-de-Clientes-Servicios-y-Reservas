from datetime import datetime, timedelta
from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from models.reserva import Reserva
from exceptions import DatoInvalidoError, ServicioNoDisponibleError, ReservaInvalidaError
from logger import registrar_error

clientes_registrados = []
reservas_creadas = []

servicios_disponibles = [
    ReservaSala(1, "Sala VIP", 200000, 10, 4),
    AlquilerEquipo(2, "Proyector 4K", 50000, 3),
    AsesoriaEspecializada(3, "Asesoría Legal", 100000, 2, False)
]

def solicitar_numero_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise DatoInvalidoError("El valor debe ser mayor a cero.")
            return valor
        except ValueError:
            print("Error: Solo se permiten números enteros.")
        except DatoInvalidoError as e:
            print(f"Error: {e}")

def solicitar_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: Este campo es obligatorio.")

def solicitar_email_valido(mensaje):
    while True:
        email = input(mensaje).strip()
        if "@" in email and "." in email.split("@")[-1]:
            return email
        print("Error: Ingrese un email válido.")

def registrar_cliente():
    print("\n--- Registro de Nuevo Cliente ---")
    try:
        id_cliente = solicitar_numero_entero("ID del cliente: ")
        if any(c.id == id_cliente for c in clientes_registrados):
            raise DatoInvalidoError("Ya existe un cliente con ese ID.")
        
        nombre = solicitar_texto_no_vacio("Nombre completo: ")
        email = solicitar_email_valido("Correo electrónico: ")
        telefono = solicitar_texto_no_vacio("Teléfono: ")

        nuevo_cliente = Cliente(id_cliente, nombre, email, telefono)
        clientes_registrados.append(nuevo_cliente)
        print(f"Cliente registrado: {nuevo_cliente.mostrar_info()}")

    except DatoInvalidoError as e:
        print(f"Error: {e}")
    except Exception as e:
        registrar_error(e)
        print(f"Error inesperado: {e}")

def consultar_servicios():
    print("\n--- Servicios Disponibles ---")
    if not servicios_disponibles:
        print("No hay servicios disponibles.")
        return
    for servicio in servicios_disponibles:
        print(f" - {servicio.mostrar_info()}")

def crear_reserva():
    print("\n--- Crear Nueva Reserva ---")
    if not clientes_registrados:
        print("Error: Registre un cliente primero.")
        return
    
    try:
        print("\nClientes registrados:")
        for i, c in enumerate(clientes_registrados, 1):
            print(f"{i}. {c.mostrar_info()}")
        
        num_cliente = solicitar_numero_entero("Digite el número del cliente: ")
        if not (1 <= num_cliente <= len(clientes_registrados)):
            raise DatoInvalidoError("Número de cliente inválido.")
        cliente_seleccionado = clientes_registrados[num_cliente - 1]

        print("\nServicios disponibles:")
        for i, servicio in enumerate(servicios_disponibles, 1):
            print(f"{i}. {servicio.mostrar_info()}")
        
        num_servicio = solicitar_numero_entero("Digite el número del servicio: ")
        if not (1 <= num_servicio <= len(servicios_disponibles)):
            raise DatoInvalidoError("Número de servicio inválido.")
        servicio_seleccionado = servicios_disponibles[num_servicio - 1]

        dias_futuro = solicitar_numero_entero("¿Dentro de cuántos días será la reserva?: ")
        fecha_reserva = datetime.now() + timedelta(days=dias_futuro)
        
        nuevo_id = len(reservas_creadas) + 1
        nueva_reserva = Reserva(nuevo_id, cliente_seleccionado, servicio_seleccionado, fecha_reserva)
        reservas_creadas.append(nueva_reserva)
        print("\n¡Reserva creada exitosamente!")
        print(nueva_reserva.mostrar_info())

    except DatoInvalidoError as e:
        print(f"Error: {e}")
    except ReservaInvalidaError as e:
        print(f"Error en la reserva: {e}")
    except ServicioNoDisponibleError as e:
        print(f"Error: {e}")
    except Exception as e:
        registrar_error(e)
        print(f"Error inesperado: {e}")

def listar_reservas():
    print("\n--- Listado de Reservas ---")
    if not reservas_creadas:
        print("No hay reservas creadas.")
        return
    for reserva in reservas_creadas:
        print(reserva.mostrar_info())

def main():
    while True:
        print("\n=== SISTEMA DE RESERVAS INTERACTIVO ===")
        print("1. Registrar nuevo cliente")
        print("2. Consultar servicios disponibles")
        print("3. Crear nueva reserva")
        print("4. Listar todas las reservas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            consultar_servicios()
        elif opcion == "3":
            crear_reserva()
        elif opcion == "4":
            listar_reservas()
        elif opcion == "5":
            print("Cerrando sistema. Hasta pronto.")
            break
        else:
            print("Error: Opción inválida. Use 1-5.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        registrar_error(e)
        print(f"Error crítico: {e}")