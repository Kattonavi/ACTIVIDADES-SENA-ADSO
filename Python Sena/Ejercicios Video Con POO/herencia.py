# Definición de la clase base 'Personaje'
class Personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def mostrarInformacion(self):
        print(f"Nombre: {self.nombre} - Salud: {self.salud} - Ataque: {self.ataque}")

# Clase derivada 'Guerrero' que hereda de 'Personaje'
class Guerrero(Personaje):
    def __init__(self, nombre, salud, ataque, arma):
        super().__init__(nombre, salud, ataque)  # Llama al constructor de la clase base
        self.arma = arma

    def mostrarInformacion(self):
        super().mostrarInformacion()  # Llama al método de la clase base
        print(f"Arma: {self.arma}")

# Crear instancias de las clases
personaje_generico = Personaje("Kattonavi", 100, 10)
guerrero_poderoso = Guerrero("Kattonavi", 1050, 2000, "Martillo De Las Sombras")

# Mostrar información de los personajes
print("Información del Personaje Base:")
personaje_generico.mostrarInformacion()

print("\nInformacion del Personaje con la clase Guerrero:")
guerrero_poderoso.mostrarInformacion()
