class Libro:
    """
    Representa un libro con título, autor y año de publicación.
    """
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        """Muestra la información del libro."""
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}"

class LibroDigital(Libro):
    """
    Representa un libro digital con un atributo adicional: formato.
    """
    def __init__(self, titulo, autor, año_publicacion, formato):
        super().__init__(titulo, autor, año_publicacion)
        self.formato = formato

    def mostrar_info(self):
        """Muestra la información del libro digital, incluyendo el formato."""
        return f"{super().mostrar_info()}, Formato: {self.formato}"

    def es_pdf(self):
        """Verifica si el libro digital está en formato PDF."""
        return self.formato.lower() == "pdf"

# Función para ingresar datos del libro

def obtener_libro():
    """Solicita al usuario los datos de un libro y devuelve una instancia de Libro o LibroDigital."""
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año_publicacion = input("Ingrese el año de publicación: ")
    es_digital = input("¿Es un libro digital? (s/n): ").strip().lower()
    
    if es_digital == 's':
        formato = input("Ingrese el formato del libro digital (PDF, EPUB, MOBI, etc.): ")
        return LibroDigital(titulo, autor, año_publicacion, formato)
    else:
        return Libro(titulo, autor, año_publicacion)

# Crear libro a partir de la entrada del usuario
libro = obtener_libro()

# Mostrar información del libro
print(libro.mostrar_info())

# Si es un libro digital, verificar si es PDF
if isinstance(libro, LibroDigital):
    if libro.es_pdf():
        print("Este libro está en formato PDF.")
    else:
        print("Este libro no está en formato PDF.")
