__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

from Producto import Producto 

class Menu:
    ######################
    # Constructor
    ######################

    def _init_(self):
        self.__productos = []
    
    #############################################
    # Metodos
    ############################################

    _method_= "agregarProducto"
    _params_= "pProducto"
    _returns_= "ninguno"
    _description_= "metodo que permite agregar un producto al menu" 
    def agregarProducto(self, pProducto):
        #aqui va mi codigo
        self.__productos.append(pProducto)

    _method_= "eliminarProducto"
    _params_= "pProducto"
    _returns_= "ninguno"
    _description_= "metodo que permite eliminar un producto del menu" 
    def eliminarProducto(self, pProducto):
        #aqui va mi codigo
        if pProducto in self.__productos:
            self.__productos.remove(pProducto)
        else:
            print("El producto no se encuentra en el menu")

    _method_= "buscarProducto"
    _params_= "pNombre"
    _returns_= "producto"
    _description_= "metodo que permite buscar un producto en el menu" 
    def buscarProducto(self, pNombre):
        #aqui va mi codigo
        for producto in self.__productos:
            if producto.darNombre() == pNombre:
                return producto
        return None