__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

from Menu import Menu
from Producto import Producto
from Pedido import Pedido

class SistemaVentas:
    #######################################################
    #constructor
    ######################################################

    def _init_(self):
        self.__menu = Menu()
        self.__pedidos = []
        self.__productos = []

    #######################################################
    # Metodos
    ######################################################

    def regristroVenta(self, pPedido):
        self.__pedidos.append(pPedido)

