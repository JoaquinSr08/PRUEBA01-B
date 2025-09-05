from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from periodico import Periodico

def main():
    #crear una biblioteca
    biblioteca = Biblioteca()
    
    #instanciar materiales
    libro = Libro("Señor de los Anillos", "J.R.R. TOLKIEN", 25000, 1800)
    revista = Revista("Inacap", "revista Inacap", 5800, 2023)
    periodico = Periodico("LUN", "LAS ULTIMAS NOTICIAS", 2300, "01/06/2024")
    
    #agregar materiales a la biblioteca
    biblioteca.agregar_material(libro)
    biblioteca.agregar_material(revista)
    biblioteca.agregar_material(periodico)
    
    #modificar precio de un material usando el setter
    print(f"\nModificando precio del libro: {libro.titulo}...")
    libro.set_precio(28000)
    
    #mostrar el catálogo completo
    biblioteca.mostrar_catalogo()

if __name__ == "__main__":
    main()