class Biblioteca:
    #clase para gestionar los materiales de la biblioteca
    
    def __init__(self):
        self.materiales = []
    
    def agregar_material(self, material):
        self.materiales.append(material)
        print(f"Material agregado: {material.descripcion()}")
    
    def mostrar_catalogo(self):
        total_valor = 0
        print("\n" + "="*50)
        print("CATALOGO COMPLETO DE LA BIBLIOTECA")
        print("="*50)
        
        for i, material in enumerate(self.materiales, 1):
            print(f"{i}. {material.descripcion()}")
            total_valor += material.get_precio()
        
        print("="*50)
        print(f"VALOR TOTAL DEL CATÁLOGO: ${total_valor:.2f}")
        print("="*50)