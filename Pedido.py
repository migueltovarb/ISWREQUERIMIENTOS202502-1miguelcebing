__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

from Producto import Producto
from Menu import Menu

class Pedido:
    ######################
    # Constructor
    ######################

    def _init_(self, pMenu):
        self.__menu = pMenu
        self.__productos_pedidos = []
    
    #############################################
    # Metodos
    ############################################

    _method_= "agregarProducto"
    _params_= "pNombreProducto"
    _returns_= "ninguno"
    _description_= "metodo que permite agregar un producto al pedido" 
    def agregarProducto(self, pNombreProducto):
        #aqui va mi codigo
        producto = self.__menu.buscarProducto(pNombreProducto)
        if producto is not None:
            self.__productos_pedidos.append(producto)
        else:
            print("El producto no se encuentra en el menu")

    _method_= "calcularTotal"
    _params_= "ninguno"
    _returns_= "total"
    _description_= "metodo que permite calcular el total del pedido" 
    def calcularTotal(self):
        #aqui va mi codigo
        total = 0
        for producto in self.__productos_pedidos:
            total += producto.darPrecio()
        return total
    
    _method_= "descuentoEstudianteCarnet"
    _params_= "porcentaje"
    _returns_= "total con descuento"
    _description_= "metodo que permite aplicar un descuento al total del pedido si el cliente es estudiante y presenta su carnet"
    def descuentoEstudianteCarnet(self, porcentaje):
        total = self.calcularTotal()
        descuento = total * (porcentaje / 100)
        return total - descuento
    
    _method_= "mostrarProductosPedidos"
    _params_= "ninguno"
    _returns_= "ninguno"
    _description_= "metodo que permite mostrar los productos pedidos"
    def mostrarProductosPedidos(self):
        for producto in self.__productos_pedidos:
            print(f"Producto: {producto.darNombre()}, Precio: {producto.darPrecio()}") 