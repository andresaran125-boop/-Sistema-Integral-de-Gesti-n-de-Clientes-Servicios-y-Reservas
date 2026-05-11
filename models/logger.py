from datetime import datetime

def log(mensaje):
    """Registra un mensaje en logs.txt con timestamp"""
    with open('logs.txt', 'a', encoding='utf-8') as archivo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{timestamp}] {mensaje}\n")