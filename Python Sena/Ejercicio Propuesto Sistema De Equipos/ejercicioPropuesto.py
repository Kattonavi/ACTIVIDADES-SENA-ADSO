# Importar la clase datetime de la libreria datetime
from datetime import datetime

# Función para crear la tabla de equipos y dispositivos
def crearTabla():
    equipos = {}  # Diccionario para almacenar equipos
    dispositivos = {}  # Diccionario para almacenar dispositivos (no utilizado en el codigo actual)
    return equipos, dispositivos  # Devuelve los diccionarios

# Funcion para insertar un nuevo equipo en el diccionario de equipos
def insertarEquipo(equipos, equipoId, nombrePropietario, tipo, dispositivos, estado, razon, codigoAmbiente):
    fechaHoraActual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
    equipos[equipoId] = {'nombrePropietario': nombrePropietario, 'tipo': tipo, 'dispositivos': dispositivos, 'estado': estado, 'razon': razon, 'fechaRegistro': fechaHoraActual, 'codigoAmbiente': codigoAmbiente}
    return equipos  # Devuelve el diccionario actualizado de equipos

# Funcion para actualizar el estado y la razon de un equipo existente
def actualizarEstadoRazon(equipos, equipoId, estado, razon):
    if equipoId not in equipos:
        print(f"No se encontró el equipo con ID {equipoId}")
        return equipos

    equipos[equipoId]['estado'] = estado
    equipos[equipoId]['razon'] = razon
    return equipos  # Devuelve el diccionario actualizado de equipos

# Funcion para modificar un equipo existente
def modificarEquipo(equipos, equipoId, nombrePropietario, tipo):
    if equipoId not in equipos:
        print(f"No se encontró el equipo con ID {equipoId}")
        return equipos

    equipos[equipoId]['nombrePropietario'] = nombrePropietario
    equipos[equipoId]['tipo'] = tipo
    return equipos  # Devuelve el diccionario actualizado de equipos

# Funcion para eliminar un equipo existente
def eliminarEquipo(equipos, dispositivoId):
    if dispositivoId not in equipos:
        print(f"No se encontró el equipo con ID {dispositivoId}")
        return equipos

    del equipos[dispositivoId]
    return equipos  # Devuelve el diccionario actualizado de equipos

# Funcion para buscar un equipo en el diccionario por su ID y mostrar su información
def buscarEquipo(equipos, dispositivoId):
    if dispositivoId not in equipos:
        print(f"No se encontró el equipo con ID {dispositivoId}")
    else:
        equipoInfo = equipos[dispositivoId]
        print(f"Información del equipo {dispositivoId}: {equipoInfo}")

# Funcion para mostrar la informacion de todos los equipos o equipos filtrados por codigo de ambiente
def consultarDatos(equipos):
    print("Equipos:")
    for equipoId, equipoInfo in equipos.items():
        print(f"{equipoId}: Nombre del Propietario: {equipoInfo['nombrePropietario']}, Tipo: {equipoInfo['tipo']}, Dispositivos: {equipoInfo['dispositivos']}, Estado: {equipoInfo['estado']}, Razon: {equipoInfo['razon']}, Fecha de Registro: {equipoInfo['fechaRegistro']}, Código de Ambiente: {equipoInfo['codigoAmbiente']}")

# Funcion para mostrar el menu de opciones
def mirarMenu():
    print("\nMenu:")
    print("1. Agregar un nuevo equipo")
    print("2. Actualizar estado y razón de un equipo")
    print("3. Modificar un equipo")
    print("4. Eliminar un equipo")
    print("5. Mostrar información de equipos")
    print("0. Salir")

# Punto de entrada principal
if __name__ == '__main__':
    equipos, dispositivos = crearTabla()  # Inicializa los diccionarios de equipos y dispositivos

    while True:
        mirarMenu()  # Muestra el menu
        opcion = input("Seleccione una opción: ")  # Solicita al usuario seleccionar una opción

        if opcion == "1":
            while True:
                # Agregar un nuevo equipo
                equipoId = input("Ingrese el ID del equipo: ")
                nombrePropietario = input("Ingrese el nombre del propietario: ")
                tipoEquipo = input("Ingrese el tipo del equipo: ")
                dispositivos = input("Ingrese el dispositivo: ")
                estadoEquipo = input("Ingrese el estado del equipo: ")
                razon = input("Ingrese la razón del equipo: ")
                codigoAmbiente = input("Ingrese el código del ambiente: ")

                equipos = insertarEquipo(equipos, equipoId, nombrePropietario, tipoEquipo, dispositivos, estadoEquipo, razon, codigoAmbiente)

                seguirAgregando = input("¿Desea agregar otro equipo (Si/No)? ")
                if seguirAgregando.lower() not in ['si', 'sí']:
                    break

        elif opcion == "2":
            # Actualizar estado y razón de un equipo
            equipoId = input("Ingrese el ID del equipo: ")
            estadoEquipo = input("Ingrese el nuevo estado del equipo: ")
            razon = input("Ingrese la nueva razón del equipo: ")
            equipos = actualizarEstadoRazon(equipos, equipoId, estadoEquipo, razon)

        elif opcion == "3":
            # Modificar un equipo
            equipoId = input("Ingrese el ID del equipo que desea modificar: ")
            nombrePropietario = input("Ingrese el nuevo nombre del propietario: ")
            tipoEquipo = input("Ingrese el nuevo tipo del equipo: ")
            equipos = modificarEquipo(equipos, equipoId, nombrePropietario, tipoEquipo)

        elif opcion == "4":
            # Eliminar un equipo
            equipoId = input("Ingrese el ID del equipo que desea eliminar: ")
            equipos = eliminarEquipo(equipos, equipoId)

        elif opcion == "5":
            # Mostrar informacion de equipos
            codigoAmbiente = input("Ingrese el código del ambiente para filtrar los equipos: ")
            equipos_filtrados = {id: info for id, info in equipos.items() if info['codigoAmbiente'] == codigoAmbiente}
            consultarDatos(equipos_filtrados)

        elif opcion == "0":
            # Salir del programa
            break

        else:
            print("Opción no válida. Intente nuevamente.")  # Mensaje para opciones no válidas
