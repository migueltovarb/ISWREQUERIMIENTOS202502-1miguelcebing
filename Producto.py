__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

class Producto:

    ######################
    # Constructor
    ######################

    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    ##################################################
    # Metodos
    ##################################################

    def mostrar(self):
        print(str(self.id) + ". " + self.nombre + " - $" + str(int(self.precio)))