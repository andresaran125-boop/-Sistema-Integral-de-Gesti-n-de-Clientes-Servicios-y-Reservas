from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from models.reserva import Reserva
from exceptions import ErrorSistema
from logger import registrar_error

# LISTAS EN MEMORIA - Aquí se guarda todo
clientes = []
servicios = []
reservas = []

def main():
    print("=== SISTEMA DE RESERVAS ===")
        
    # 1. CREAR CLIENTES - Operación 1
    print("\n1. Creando clientes...")
    c1 = Cliente(1, "Ana Torres", "ana@mail.com", "3001234567")
    c2 = Cliente(2, "Luis Mora", "luis@mail.com", "3109876543")
    clientes.extend([c1, c2])
    print(f"Clientes creados: {len(clientes)}")
    
    # 2. Creando servicios...
try:
    sala1 = ReservaSala(1, "Sala VIP", 50000, 60, 3)  # ← id, nombre, costo, capacidad, horas
    print(f"✅ Servicio creado: {sala1.mostrar_info()}")
except ErrorSistema as e:
    registrar_error(e)

try:
    equipo1 = AlquilerEquipo(2, "Proyector 4K", 80000, 5)  # ← id, nombre, costo, dias
    print(f"✅ Servicio creado: {equipo1.mostrar_info()}")
except ErrorSistema as e:
    registrar_error(e)

try:
    asesoria1 = AsesoriaEspecializada(3, "Marketing Digital", 120000, 2, True)  # ← id, nombre, costo, horas, urgente
    print(f"✅ Servicio creado: {asesoria1.mostrar_info()}")
except ErrorSistema as e:
    registrar_error(e)
    
    # 3. MOSTRAR INFO - Operación 3 - POLIMORFISMO
    print("\n3. Lista de servicios:")
    for servicio in servicios:
        print(servicio.mostrar_info())
    
    # 4. CREAR RESERVAS - Operación 4
    print("\n4. Creando reservas...")
    r1 = Reserva(1, c1, s1, 3)  # Ana reserva Sala x 3h
    r2 = Reserva(2, c2, s2, 6)  # Luis alquila Proyector x 6h = 10% desc
    r3 = Reserva(3, c1, s3, 2)  # Ana pide Asesoría x 2h = +20000
    reservas.extend([r1, r2, r3])
    print(f"Reservas creadas: {len(reservas)}")
    
    # 5. CALCULAR COSTOS - Operación 5 - POLIMORFISMO
    print("\n5. Costos calculados:")
    for reserva in reservas:
        print(f"{reserva.mostrar_info()}")
    
    # 6. CONFIRMAR RESERVA - Operación 6
    print("\n6. Confirmando reserva #1...")
    r1.confirmar()
    print(f"Estado: {r1.estado}")
    
    # 7. CANCELAR RESERVA - Operación 7
    print("\n7. Cancelando reserva #2...")
    r2.cancelar()
    print(f"Estado: {r2.estado}")
    
    # 8. COMPLETAR RESERVA - Operación 8
    print("\n8. Completando reserva #1...")
    r1.completar()
    print(f"Estado: {r1.estado}")
    
    # 9. LISTAR RESERVAS POR ESTADO - Operación 9
    print("\n9. Reservas COMPLETADAS:")
    completadas = [r for r in reservas if r.estado == "COMPLETADA"]
    for r in completadas:
        print(r.mostrar_info())
    
    # 10. PROBAR EXCEPCIONES - Operación 10
    print("\n10. Probando errores...")
    try:
        # Error 1: Email malo
        Cliente(3, "Pedro", "correo_malo", "123")
    except ErrorSistema as e:
        registrar_error(e)
        
    try:
        # Error 2: Servicio no disponible
        s1.disponible = False
        Reserva(4, c1, s1, 1)
    except ErrorSistema as e:
        registrar_error(e)
        
    try:
        # Error 3: Cancelar reserva completada
        r1.cancelar()
    except ErrorSistema as e:
        registrar_error(e)
    
    print("\n=== FIN DEL SISTEMA ===")
    print("Revisa el archivo 'sistema.log' para ver los errores registrados")
    
except Exception as e:
    registrar_error(e)
    print(f"Error crítico: {e}")

if __name__ == "__main__":
    main()
