from material import Material

class Revista(Material):
    #Clase Revista que hereda de Material
    
    def __init__(self, titulo, autor, precio, edicion):
        super().__init__(titulo, autor, precio)
        self.edicion = edicion
    
    def descripcion(self):
        return super().descripcion() + f", Edicion: {self.edicion}"