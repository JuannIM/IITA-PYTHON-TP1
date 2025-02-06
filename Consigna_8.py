class Libro:
    
    # Representa un libro con título, autor y año de publicación.
    
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        # Muestra la información del libro.
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}"

class LibroDigital(Libro):
    
    # Representa un libro digital con un atributo adicional: formato.
    
    def __init__(self, titulo, autor, año_publicacion, formato):
        self.formato = formato
        super().__init__(titulo, autor, año_publicacion) # super() utilizado para dar acceso a los metodos a clases "hermanas"

    def mostrar_info(self):
        #Muestra la información del libro digital, incluyendo el formato.
        return f"{super().mostrar_info()}, Formato: {self.formato}"

# Ejemplo de uso
libro_fisico = Libro("1984", "George Orwell", 1949)
libro_digital = LibroDigital("1984", "George Orwell", 1949, "PDF")

print(libro_fisico.mostrar_info())
print(libro_digital.mostrar_info())
