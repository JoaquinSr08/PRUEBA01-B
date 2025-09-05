from material import Material

class Libro(Material):
    
    def __init__(self, titulo, autor, precio, paginas):
        super().__init__(titulo, autor, precio)
        self.paginas = paginas
    
    def descripcion(self):
        return super().descripcion() + f", Paginas: {self.paginas}"