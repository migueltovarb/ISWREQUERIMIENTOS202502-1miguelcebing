__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

class Pedido:

    ######################
    # Constructor
    ######################

    def __init__(self):
        self.productos = []  # Lista de productos
        self.es_estudiante = False
    
    ##################################################
    # Metodos
    ##################################################
    
    def agregar_producto(self, nombre, precio, cantidad):
        # Buscar si ya existe el producto
        encontrado = False
        for i in range(len(self.productos)):
            if self.productos[i]['nombre'] == nombre:
                self.productos[i]['cantidad'] = self.productos[i]['cantidad'] + cantidad
                encontrado = True
                break
        
        # Si no existe, agregar nuevo
        if not encontrado:
            producto_nuevo = {
                'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad
            }
            self.productos.append(producto_nuevo)
    
    def quitar_producto(self, nombre):
        for i in range(len(self.productos)):
            if self.productos[i]['nombre'] == nombre:
                del self.productos[i]
                return True
        return False
    
    def calcular_total(self):
        subtotal = 0
        # Sumar todos los productos
        for producto in self.productos:
            subtotal = subtotal + (producto['precio'] * producto['cantidad'])
        
        # Calcular descuento
        descuento = 0
        if self.es_estudiante == True:
            descuento = subtotal * 0.10
        
        total = subtotal - descuento
        return subtotal, descuento, total
    
    def mostrar_resumen(self):
        if len(self.productos) == 0:
            print("El pedido esta vacio")
            return
        
        print("")
        print("=" * 35)
        print("        RESUMEN DEL PEDIDO")
        print("=" * 35)
        
        # Mostrar cada producto
        for producto in self.productos:
            nombre = producto['nombre']
            cantidad = producto['cantidad']  
            precio = producto['precio']
            subtotal_producto = precio * cantidad
            print(nombre + " x" + str(cantidad) + " = $" + str(int(subtotal_producto)))
        
        # Mostrar totales
        subtotal, descuento, total = self.calcular_total()
        print("-" * 35)
        print("Subtotal: $" + str(int(subtotal)))
        
        if self.es_estudiante == True:
            print("Descuento estudiante: -$" + str(int(descuento)))
        
        print("TOTAL A PAGAR: $" + str(int(total)))
        print("=" * 35)
    
    def esta_vacio(self):
        return len(self.productos) == 0