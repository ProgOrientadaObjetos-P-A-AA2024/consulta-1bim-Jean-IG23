class RegistroNotas:
    def __init__(self):
        self.lista_estudiantes = []

    def añadir_alumno(self, nombre, nota):
        self.lista_estudiantes.append({"nombre": nombre, "nota": nota})

    def promedio_notas(self):
        total_notas = sum(alumno["nota"] for alumno in self.lista_estudiantes)
        cantidad_alumnos = len(self.lista_estudiantes)
        return total_notas / cantidad_alumnos if cantidad_alumnos > 0 else 0

registro = RegistroNotas()
registro.añadir_alumno("Pedro", 7)
registro.añadir_alumno("María", 8)
registro.añadir_alumno("Javier", 9)
promedio = registro.promedio_notas()
print(f"Promedio de notas del grupo: {promedio:.2f}")
