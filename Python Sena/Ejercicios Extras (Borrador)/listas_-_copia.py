# punto 1
# Crear listas vacías para almacenar nombres de aprendices y sus edades
Aprendices = []
Edades = []

# Inicializar un contador
count = 0

# Comenzar un bucle para ingresar datos de 30 aprendices
while count < 6:
    # Pedir al usuario que ingrese el nombre del aprendiz y agregarlo a la lista Aprendices
    aprendiz = str(input("Ingrese el nombre del aprendiz: "))
    Aprendices.append(aprendiz)

    # Pedir al usuario que ingrese la edad del aprendiz y agregarla a la lista Edades
    Edad = int(input("Ingrese la edad del aprendiz:"))
    Edades.append(Edad)

    # Incrementar el contador en 1
    count += 1

# punto 2
# Imprimir la lista de nombres de aprendices y sus edades
print(Aprendices)
print(Edades)

# punto 3
# Encontrar la edad máxima y el aprendiz más viejo
Edad = max(Edades)
iAprendizMayor = Edades.index(Edad)
apMayor = Aprendices[iAprendizMayor]

# Imprimir el nombre del aprendiz más viejo
print("El aprendiz mayor es", apMayor)

# punto 4
# Insertar un nuevo aprendiz y su edad al principio de las listas
Aprendices.insert(0, "Adriana Lucia")
Edades.insert(0, 40)

# Imprimir la lista actualizada de nombres de aprendices
print(Aprendices)

# punto 5
# Contar cuántas veces aparece el valor 18 en la lista de nombres de aprendices
Aprendices18 = Edades.count(18)
print("Número de aprendices con 18 años:", Aprendices18)

# punto 6
# Agregar un nuevo aprendiz ("Maria Paula") y su edad (17) al final de las listas
Aprendices.append("Maria Paula")
Edades.append(17)

# Imprimir las listas actualizadas de nombres de aprendices y edades
print(Aprendices, Edades)

# punto 7
# Eliminar el primer aprendiz y su edad de las listas
Aprendices.pop(0)
Edades.pop(0)

# Imprimir las listas actualizadas de nombres de aprendices y edades
print(Aprendices, Edades)

# punto 8
# Pedir al usuario que ingrese un nombre y buscar si existe en la lista de aprendices
nomAprendiz = str(input("Ingrese el nombre que quiere buscar: "))
coincidencias = 0

for aprendiz in Aprendices:
    if nomAprendiz == aprendiz:
        print(nomAprendiz)
        coincidencias = 1
    else:
        continue

# Si no se encontró ninguna coincidencia, imprimir el nombre buscado
if coincidencias == 0:
    print(nomAprendiz)

# punto 9
# Imprimir una porción de la lista de nombres de aprendices y edades
print("Primeras 10 entradas de Aprendices:", Aprendices[0:10])
print("Primeras 10 entradas de Edades:", Edades[0:10])

# punto 10
# Imprimir otra porción de la lista de nombres de aprendices y edades
print("Entradas 20 a 30 de Aprendices:", Aprendices[20:31])
print("Entradas 20 a 30 de Edades:", Edades[20:31])

# punto 11
# Imprimir una tercera porción de la lista de nombres de aprendices y edades
print("Entradas 10 a 20 de Aprendices:", Aprendices[10:21])
print("Entradas 10 a 20 de Edades:", Edades[10:21])
