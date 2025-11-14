__author__="miguel ceballos ramirez" 
__license__="GPL"
__version__="1.0.0"
__email__="miguelceballos.ra@campusucc.edu.co"


    ################################################################
    #constructor 
    ################################################################

class Usuario:
    def __init__(self, nombre, telefono, correo, cargo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.cargo = cargo

    def to_line(self):
        return f"{self.nombre};{self.telefono};{self.correo};{self.cargo}\n"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split(";")
        if len(partes) == 4:
            return Usuario(partes[0], partes[1], partes[2], partes[3])
        return None




    

    

    

    