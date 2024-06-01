class ListaPaises:
    def __init__(self, paises):
        self.lista_paises = paises

    def obtener_paises_por_letra(self, letra):
        resultado = []
        for pais in self.lista_paises:
            if pais[0].lower() == letra.lower():
                resultado.append(pais)
        return resultado

nombres_paises = ["España", "Francia", "Alemania", "Italia", "Egipto", "Ecuador", "Suecia", "Noruega", "Finlandia"]

paises_con_e = ListaPaises(nombres_paises)

paises = paises_con_e.obtener_paises_por_letra('E')
print("Países que comienzan con 'E':")
for pais in paises:
    print(pais)
