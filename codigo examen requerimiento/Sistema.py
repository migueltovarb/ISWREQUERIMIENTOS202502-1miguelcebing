__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"

from Usuario import Usuario

    ################################################################
    #constructor
    ################################################################

class Sistema:
    def __init__(self):
        self.usuarios = []
        try:
            with open("contactos.csv", "r", encoding="utf-8") as f:
                for linea in f:
                    u = Usuario.from_line(linea)
                    if u: self.usuarios.append(u)
        except: pass

    def guardar(self):
        with open("contactos.csv", "w", encoding="utf-8") as f:
            for u in self.usuarios:
                f.write(u.to_line())

    def correo_existe(self, correo):
        return any(u.correo == correo for u in self.usuarios)

    def registrar(self):
        nombre = input("Nombre completo: ")
        tel = input("Teléfono: ")
        correo = input("Correo: ")
        if self.correo_existe(correo):
            print("Correo ya registrado."); return
        self.usuarios.append(Usuario(nombre, tel, correo,))
        self.guardar()
        print("Contacto registrado.")

    def buscar(self):
        q = input("Buscar por nombre o correo: ").lower()
        encontrados = [u for u in self.usuarios if q in u.nombre.lower() or q in u.correo.lower()]
        if encontrados:
            for u in encontrados:
                print(f"{u.nombre}, {u.telefono}, {u.correo},")
        else:
            print("No encontrado.")

    def listar(self):
        if not self.usuarios:
            print("No hay contactos."); return
        for u in self.usuarios:
            print(f"{u.nombre}, {u.telefono}, {u.correo},")

    def eliminar(self):
        correo = input("Correo a eliminar: ")
        for i, u in enumerate(self.usuarios):
            if u.correo == correo:
                del self.usuarios[i]
                self.guardar()
                print("Eliminado."); return
        print("No encontrado.")

    def actualizar(self):
        correo = input("Correo del contacto a actualizar: ")
        for u in self.usuarios:
            if u.correo == correo:
                u.nombre = input(f"Nuevo nombre ({u.nombre}): ") or u.nombre
                u.telefono = input(f"Nuevo teléfono ({u.telefono}): ") or u.telefono
                self.guardar()
                print("Actualizado."); return
        print("No encontrado.")

    def menu(self):
        while True:
            print("\n1. Registrar\n2. Buscar\n3. Listar\n4. Eliminar\n5. Actualizar\n6. Salir")
            op = input("Opción: ")
            if op == "1": self.registrar()
            elif op == "2": self.buscar()
            elif op == "3": self.listar()
            elif op == "4": self.eliminar()
            elif op == "5": self.actualizar()
            elif op == "6": break
            else: print("Opción no válida.")

if __name__ == "__main__":
    Sistema().menu()
    

    