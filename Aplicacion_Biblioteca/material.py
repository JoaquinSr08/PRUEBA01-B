class Material:
    #Clase base para todos los materiales de la biblioteca
    
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a 0")
    
    def descripcion(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Precio: ${self.__precio:.2f}"