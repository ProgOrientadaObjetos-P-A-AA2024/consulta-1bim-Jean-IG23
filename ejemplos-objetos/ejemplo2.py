class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    def descripcion(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Valor Total: {self.valor_total()}"

producto1 = Producto("Laptop", 1000, 5)
producto2 = Producto("Teléfono", 500, 10)

print(producto1.descripcion())
print(producto2.descripcion())
