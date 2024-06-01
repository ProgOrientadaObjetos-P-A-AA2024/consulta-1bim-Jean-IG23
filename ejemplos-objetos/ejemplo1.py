class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def descripcion(self):
        return f"{self.titulo} por {self.autor}, publicado en {self.anio_publicacion}."

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)

print(libro1.descripcion())
print(libro2.descripcion())
