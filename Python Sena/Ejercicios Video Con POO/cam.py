# Definición de la clase Personaje
class Personaje:
    
    # Constructor que inicializa los atributos del personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    # Método para imprimir los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("· Fuerza:", self.fuerza)
        print("· Inteligencia:", self.inteligencia)
        print("· Defensa:", self.defensa)
        print("· Vida:", self.vida)

    # Método que devuelve True si el personaje está vivo, False si no
    def esta_vivo(self):
        return self.vida > 0

    # Método que establece la vida del personaje en 0 y muestra un mensaje de muerte
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método que calcula el daño que el personaje inflige a un enemigo
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Método que realiza un ataque al enemigo, reduciendo su vida
    def atacar(self, enemigo):
        # Calcular el daño
        daño = self.daño(enemigo)
        
        # Reducir la vida del enemigo
        enemigo.vida = enemigo.vida - daño

        # Mostrar mensaje de ataque y resultados
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        
        # Verificar si el enemigo está vivo
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

# Crear instancias de la clase Personaje
mi_personaje = Personaje("Kattonavi", 100, 1, 5, 100)
mi_enemigo = Personaje("Hydra", 8, 5, 3, 50)

# Realizar un ataque del personaje principal al enemigo
mi_personaje.atacar(mi_enemigo)

# Mostrar los atributos del enemigo después del ataque
mi_enemigo.atributos()
