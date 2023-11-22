from datetime import datetime

# Definición de la clase Equipo para representar la información de un equipo
class Equipo:
    # Constructor de la clase Equipo para inicializar sus atributos
    def __init__(self, equipo_id, nombre_propietario, tipo, dispositivos, estado, razon, codigo_ambiente):
        self.equipo_id = equipo_id
        self.nombre_propietario = nombre_propietario
        self.tipo = tipo
        self.dispositivos = dispositivos
        self.estado = estado
        self.razon = razon
        # Se registra la fecha y hora actual al crear el objeto Equipo
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.codigo_ambiente = codigo_ambiente

# Definición de la clase SistemaEquipos para manejar las operaciones relacionadas con equipos
class SistemaEquipos:
    # Constructor de la clase SistemaEquipos para inicializar su atributo equipos como un diccionario vacío
    def __init__(self):
        self.equipos = {}

    # Método para insertar un nuevo equipo en el diccionario de equipos
    def insertar_equipo(self, equipo):
        self.equipos[equipo.equipo_id] = equipo

    # Método para actualizar el estado y la razón de un equipo existente
    def actualizar_estado_razon(self, equipo_id, estado, razon):
        # Verifica si el equipo con el ID proporcionado existe en el diccionario de equipos
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
            return

        # Actualiza el estado y la razón del equipo
        self.equipos[equipo_id].estado = estado
        self.equipos[equipo_id].razon = razon

    # Método para modificar un equipo existente
    def modificar_equipo(self, equipo_id, nombre_propietario, tipo):
        # Verifica si el equipo con el ID proporcionado existe en el diccionario de equipos
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
            return

        # Modifica el nombre del propietario y el tipo del equipo
        self.equipos[equipo_id].nombre_propietario = nombre_propietario
        self.equipos[equipo_id].tipo = tipo

    # Método para eliminar un equipo existente
    def eliminar_equipo(self, equipo_id):
        # Verifica si el equipo con el ID proporcionado existe en el diccionario de equipos
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
            return

        # Elimina el equipo del diccionario de equipos
        del self.equipos[equipo_id]

    # Método para buscar un equipo en el diccionario por su ID y mostrar su información
    def buscar_equipo(self, equipo_id):
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
        else:
            equipo_info = self.equipos[equipo_id]
            print(f"Información del equipo {equipo_id}: {equipo_info.__dict__}")

    # Método para mostrar la información de todos los equipos o equipos filtrados por código de ambiente
    def consultar_datos(self, codigo_ambiente=None):
        print("Equipos:")
        equipos_filtrados = self.equipos
        # Filtra los equipos por código de ambiente si se proporciona
        if codigo_ambiente:
            equipos_filtrados = {id: info for id, info in self.equipos.items() if info.codigo_ambiente == codigo_ambiente}

        # Muestra la información de los equipos
        for equipo_id, equipo_info in equipos_filtrados.items():
            print(f"{equipo_id}: Nombre del Propietario: {equipo_info.nombre_propietario}, Tipo: {equipo_info.tipo}, Dispositivos: {equipo_info.dispositivos}, Estado: {equipo_info.estado}, Razon: {equipo_info.razon}, Fecha de Registro: {equipo_info.fecha_registro}, Código de Ambiente: {equipo_info.codigo_ambiente}")

    # Método para mostrar el menú de opciones
    def mostrar_menu(self):
        print("\nMenu:")
        print("1. Agregar un nuevo equipo")
        print("2. Actualizar estado y razón de un equipo")
        print("3. Modificar un equipo")
        print("4. Eliminar un equipo")
        print("5. Mostrar información de equipos")
        print("0. Salir")

# Punto de entrada principal
if __name__ == '__main__':
    # Se crea una instancia de la clase SistemaEquipos
    sistema_equipos = SistemaEquipos()

    # Bucle principal del programa
    while True:
        # Se muestra el menú
        sistema_equipos.mostrar_menu()
        # Se solicita al usuario seleccionar una opción
        opcion = input("Seleccione una opción: ")

        # Bloque de código para cada opción del menú
        if opcion == "1":
            # Agregar un nuevo equipo
            equipo_id = input("Ingrese el ID del equipo: ")
            nombre_propietario = input("Ingrese el nombre del propietario: ")
            tipo_equipo = input("Ingrese el tipo del equipo: ")
            dispositivos = input("Ingrese el dispositivo: ")
            estado_equipo = input("Ingrese el estado del equipo: ")
            razon = input("Ingrese la razón del equipo: ")
            codigo_ambiente = input("Ingrese el código del ambiente: ")

            # Se crea una instancia de la clase Equipo y se inserta en el sistema
            nuevo_equipo = Equipo(equipo_id, nombre_propietario, tipo_equipo, dispositivos, estado_equipo, razon, codigo_ambiente)
            sistema_equipos.insertar_equipo(nuevo_equipo)

            # Se pregunta al usuario si desea agregar otro equipo
            seguir_agregando = input("¿Desea agregar otro equipo (Si/No)? ")
            if seguir_agregando.lower() not in ['si', 'sí']:
                break

        elif opcion == "2":
            # Actualizar estado y razón de un equipo
            equipo_id = input("Ingrese el ID del equipo: ")
            estado_equipo = input("Ingrese el nuevo estado del equipo: ")
            razon = input("Ingrese la nueva razón del equipo: ")
            sistema_equipos.actualizar_estado_razon(equipo_id, estado_equipo, razon)

        elif opcion == "3":
            # Modificar un equipo
            equipo_id = input("Ingrese el ID del equipo que desea modificar: ")
            nombre_propietario = input("Ingrese el nuevo nombre del propietario: ")
            tipo_equipo = input("Ingrese el nuevo tipo del equipo: ")
            sistema_equipos.modificar_equipo(equipo_id, nombre_propietario, tipo_equipo)

        elif opcion == "4":
            # Eliminar un equipo
            equipo_id = input("Ingrese el ID del equipo que desea eliminar: ")
            sistema_equipos.eliminar_equipo(equipo_id)

        elif opcion == "5":
            # Mostrar información de equipos
            codigo_ambiente = input("Ingrese el código del ambiente para filtrar los equipos: ")
            sistema_equipos.consultar_datos(codigo_ambiente)

        elif opcion == "0":
            # Salir del programa
            break

        else:
            # Mensaje para opciones no válidas
            print("Opción no válida. Intente nuevamente.")
