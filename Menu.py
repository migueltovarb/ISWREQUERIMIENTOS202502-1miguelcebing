__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

from SistemaVentas import Sistema

def main():
    print("Iniciando sistema...")
    sistema = Sistema()
    sistema.ejecutar()

if __name__ == "__main__":
    main()
