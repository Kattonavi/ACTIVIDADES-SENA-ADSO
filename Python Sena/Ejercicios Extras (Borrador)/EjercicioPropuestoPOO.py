from datetime import datetime

class Equipo:
    def __init__(self, equipo_id, nombre_propietario, tipo, dispositivos, estado, razon, codigo_ambiente):
        self.equipo_id = equipo_id
        self.nombre_propietario = nombre_propietario
        self.tipo = tipo
        self.dispositivos = dispositivos
        self.estado = estado
        self.razon = razon
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.codigo_ambiente = codigo_ambiente

class SistemaEquipos:
    def __init__(self):
        self.equipos = {}

    def insertar_equipo(self, equipo):
        self.equipos[equipo.equipo_id] = equipo

    def actualizar_estado_razon(self, equipo_id, estado, razon):
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
            return

        self.equipos[equipo_id].estado = estado
        self.equipos[equipo_id].razon = razon

    def modificar_equipo(self, equipo_id, nombre_propietario, tipo):
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
            return

        self.equipos[equipo_id].nombre_propietario = nombre_propietario
        self.equipos[equipo_id].tipo = tipo

    def eliminar_equipo(self, equipo_id):
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
            return

        del self.equipos[equipo_id]

    def buscar_equipo(self, equipo_id):
        if equipo_id not in self.equipos:
            print(f"No se encontró el equipo con ID {equipo_id}")
        else:
            equipo_info = self.equipos[equipo_id]
            print(f"Información del equipo {equipo_id}: {equipo_info.__dict__}")

    def consultar_datos(self, codigo_ambiente=None):
        print("Equipos:")
        equipos_filtrados = self.equipos
        if codigo_ambiente:
            equipos_filtrados = {id: info for id, info in self.equipos.items() if info.codigo_ambiente == codigo_ambiente}

        for equipo_id, equipo_info in equipos_filtrados.items():
            print(f"{equipo_id}: Nombre del Propietario: {equipo_info.nombre_propietario}, Tipo: {equipo_info.tipo}, Dispositivos: {equipo_info.dispositivos}, Estado: {equipo_info.estado}, Razon: {equipo_info.razon}, Fecha de Registro: {equipo_info.fecha_registro}, Código de Ambiente: {equipo_info.codigo_ambiente}")

    def mostrar_menu(self):
        print("\nMenu:")
        print("1. Agregar un nuevo equipo")
        print("2. Actualizar estado y razón de un equipo")
        print("3. Modificar un equipo")
        print("4. Eliminar un equipo")
        print("5. Mostrar información de equipos")
        print("0. Salir")

if __name__ == '__main__':
    sistema_equipos = SistemaEquipos()

    while True:
        sistema_equipos.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            equipo_id = input("Ingrese el ID del equipo: ")
            nombre_propietario = input("Ingrese el nombre del propietario: ")
            tipo_equipo = input("Ingrese el tipo del equipo: ")
            dispositivos = input("Ingrese el dispositivo: ")
            estado_equipo = input("Ingrese el estado del equipo: ")
            razon = input("Ingrese la razón del equipo: ")
            codigo_ambiente = input("Ingrese el código del ambiente: ")

            nuevo_equipo = Equipo(equipo_id, nombre_propietario, tipo_equipo, dispositivos, estado_equipo, razon, codigo_ambiente)
            sistema_equipos.insertar_equipo(nuevo_equipo)

            seguir_agregando = input("¿Desea agregar otro equipo (Si/No)? ")
            if seguir_agregando.lower() not in ['si', 'sí']:
                break

        elif opcion == "2":
            equipo_id = input("Ingrese el ID del equipo: ")
            estado_equipo = input("Ingrese el nuevo estado del equipo: ")
            razon = input("Ingrese la nueva razón del equipo: ")
            sistema_equipos.actualizar_estado_razon(equipo_id, estado_equipo, razon)

        elif opcion == "3":
            equipo_id = input("Ingrese el ID del equipo que desea modificar: ")
            nombre_propietario = input("Ingrese el nuevo nombre del propietario: ")
            tipo_equipo = input("Ingrese el nuevo tipo del equipo: ")
            sistema_equipos.modificar_equipo(equipo_id, nombre_propietario, tipo_equipo)

        elif opcion == "4":
            equipo_id = input("Ingrese el ID del equipo que desea eliminar: ")
            sistema_equipos.eliminar_equipo(equipo_id)

        elif opcion == "5":
            codigo_ambiente = input("Ingrese el código del ambiente para filtrar los equipos: ")
            sistema_equipos.consultar_datos(codigo_ambiente)

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intente nuevamente.")
