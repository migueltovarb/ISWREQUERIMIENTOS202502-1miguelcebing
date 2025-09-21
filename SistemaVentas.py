__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

from Producto import Producto
from Pedido import Pedido

class Sistema:

    ######################
    # Constructor
    ######################

    def __init__(self):
        # Crear productos del menu
        self.productos = []
        self.productos.append(Producto(1, "Cafe americano", 2500))
        self.productos.append(Producto(2, "Cafe con leche", 3000))
        self.productos.append(Producto(3, "Sandwich", 5000))
        self.productos.append(Producto(4, "Empanada", 2800))
        self.productos.append(Producto(5, "Jugo natural", 3500))
        self.productos.append(Producto(6, "Agua", 1500))
        
        # Lista para guardar ventas
        self.ventas = []
    
    ##################################################
    # Metodos
    ##################################################
    
    def mostrar_menu(self):
        print("")
        print("=" * 40)
        print("      MENU - CAFETERIA CAMPUS")
        print("=" * 40)
        for producto in self.productos:
            producto.mostrar()
        print("=" * 40)
    
    def buscar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None
    
    def hacer_pedido(self):
        pedido = Pedido()
        
        # PASO 1: Mostrar menu
        self.mostrar_menu()
        
        # PASO 2: Agregar productos
        print("")
        print("Selecciona productos (0 para terminar)")
        
        while True:
            try:
                print("")
                id_producto = int(input("ID del producto: "))
                
                # Si ingresa 0, terminar
                if id_producto == 0:
                    break
                
                # Buscar el producto
                producto = self.buscar_producto(id_producto)
                if producto == None:
                    print("ERROR: Producto no existe")
                    continue
                
                # Pedir cantidad
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("ERROR: Cantidad debe ser mayor a 0")
                    continue
                
                # Agregar al pedido
                pedido.agregar_producto(producto.nombre, producto.precio, cantidad)
                print("AGREGADO: " + producto.nombre + " x" + str(cantidad))
                
            except:
                print("ERROR: Solo ingresa numeros")
        
        # Verificar si el pedido tiene productos
        if pedido.esta_vacio():
            print("Pedido cancelado - no hay productos")
            return
        
        # PASO 3: Verificar si es estudiante
        print("")
        respuesta = input("Es estudiante? (s/n): ")
        if respuesta == "s" or respuesta == "S":
            carnet = input("Numero de carne: ")
            if len(carnet) >= 3:
                pedido.es_estudiante = True
                print("Descuento de estudiante aplicado")
            else:
                print("ERROR: Carne invalido (minimo 3 caracteres)")
        
        # PASO 4: Mostrar resumen y confirmar
        pedido.mostrar_resumen()
        print("")
        confirmar = input("Confirmar pedido? (s/n): ")
        
        if confirmar == "s" or confirmar == "S":
            self.guardar_venta(pedido)
            print("")
            print("EXITO: Pedido procesado correctamente!")
        else:
            print("Pedido cancelado")
    
    def guardar_venta(self, pedido):
        subtotal, descuento, total = pedido.calcular_total()
        
        # Crear registro de venta
        venta = {
            'productos': pedido.productos,
            'es_estudiante': pedido.es_estudiante,
            'subtotal': subtotal,
            'descuento': descuento,
            'total': total
        }
        
        # Agregar a la lista de ventas
        self.ventas.append(venta)
    
    def ver_ventas_dia(self):
        if len(self.ventas) == 0:
            print("No hay ventas registradas hoy")
            return
        
        print("")
        print("=" * 40)
        print("       VENTAS DEL DIA")
        print("=" * 40)
        
        total_dia = 0
        total_descuentos = 0
        
        # Mostrar cada venta
        for i in range(len(self.ventas)):
            venta = self.ventas[i]
            numero_venta = i + 1
            print("Venta " + str(numero_venta) + ": $" + str(int(venta['total'])))
            total_dia = total_dia + venta['total']
            total_descuentos = total_descuentos + venta['descuento']
        
        print("-" * 40)
        print("Numero de ventas: " + str(len(self.ventas)))
        print("Total descuentos: $" + str(int(total_descuentos)))
        print("TOTAL DEL DIA: $" + str(int(total_dia)))
        print("=" * 40)
    
    def agregar_producto_menu(self):
        print("")
        print("--- AGREGAR PRODUCTO ---")
        
        nombre = input("Nombre del producto: ")
        if len(nombre) == 0:
            print("ERROR: El nombre no puede estar vacio")
            return
        
        try:
            precio = float(input("Precio: $"))
            if precio <= 0:
                print("ERROR: El precio debe ser mayor a 0")
                return
            
            # Crear nuevo ID
            nuevo_id = len(self.productos) + 1
            
            # Crear y agregar producto
            producto_nuevo = Producto(nuevo_id, nombre, precio)
            self.productos.append(producto_nuevo)
            
            print("EXITO: Producto agregado - " + nombre + " ($" + str(int(precio)) + ")")
            
        except:
            print("ERROR: Precio invalido")
    
    def ejecutar(self):
        print("*" * 40)
        print("    BIENVENIDO A CAFETERIA CAMPUS")
        print("*" * 40)
        
        while True:
            print("")
            print("MENU PRINCIPAL:")
            print("1. Hacer pedido")
            print("2. Ver ventas del dia")  
            print("3. Agregar producto al menu")
            print("4. Salir")
            print("")
            
            opcion = input("Selecciona una opcion: ")
            
            if opcion == "1":
                self.hacer_pedido()
            elif opcion == "2":
                self.ver_ventas_dia()
            elif opcion == "3":
                self.agregar_producto_menu()
            elif opcion == "4":
                print("")
                print("Gracias por usar Cafeteria Campus!")
                print("Hasta luego!")
                break
            else:
                print("ERROR: Opcion invalida. Selecciona 1, 2, 3 o 4")