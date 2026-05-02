import logging

# Configura el archivo donde se guardan los errores
logging.basicConfig(
    filename='sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - ERROR - %(message)s'
)

def registrar_error(error):
    """Guarda el error en sistema.log"""
    logging.error(f"{type(error).__name__}: {str(error)}")
    print(f"ERROR REGISTRADO: {error}")