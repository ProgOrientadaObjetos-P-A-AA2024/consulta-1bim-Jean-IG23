class Libro:
    def __init__(self, titulo, autor, info_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.info_publicacion = info_publicacion

    def detalles(self):
        anio, editorial = self.info_publicacion
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAño: {anio}\nEditorial: {editorial}"

libro1 = Libro("1984", "George Orwell", (1949, "Secker & Warburg"))
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", (1967, "Editorial Sudamericana"))

print(libro1.detalles())
print(libro2.detalles())
