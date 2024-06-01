class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes_y_notas = []

    def agregar_estudiante(self, nombre, notas):
        self.estudiantes_y_notas.append((nombre, notas))

    def promedio_notas(self, nombre):
        for estudiante, notas in self.estudiantes_y_notas:
            if estudiante == nombre:
                return sum(notas) / len(notas)
        return None

curso = Curso("Matemáticas")

curso.agregar_estudiante("Juan", (90, 85, 92))
curso.agregar_estudiante("Maria", (88, 90, 85))
curso.agregar_estudiante("Luis", (70, 75, 80))

print(f"Promedio de notas de Juan: {curso.promedio_notas('Juan'):.2f}")
print(f"Promedio de notas de Maria: {curso.promedio_notas('Maria'):.2f}")
print(f"Promedio de notas de Luis: {curso.promedio_notas('Luis'):.2f}")

