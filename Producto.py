__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

class Producto:

    ######################
    # Constructor
    ######################

    def _init_(self, pNombre, pPrecio):
        self.__nombre = pNombre
        self.__precio = pPrecio

    ##################################################
    # Metodos
    ##################################################

    _method_= "darNombre"
    _params_= "ninguno"
    _returns_= "nombre"
    _description_= "metodo que permite dar el nombre del producto" 
    def darNombre(self):
        #aqui va mi codigo
        return self.__nombre
    
    _method_= "darPrecio"
    _params_= "ninguno"
    _returns_= "precio"
    _description_= "metodo que permite dar el precio del producto" 
    def darPrecio(self):
        #aqui va mi codigo
        return self.__precio
    