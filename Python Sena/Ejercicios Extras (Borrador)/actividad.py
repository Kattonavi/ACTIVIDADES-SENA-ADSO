# Crear listas vacías de aprendices y edades
aprendices = []
edades = []

# Llenar las listas
for i in range(3):
    nombre = input(f"Ingrese el nombre del aprendiz {i + 1}: ")
    if nombre == "":
        break
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir las listas
print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)

# Encontrar el aprendiz con la mayor edad
indice_mayor_edad = edades.index(max(edades))
print("El aprendiz más mayor es:", aprendices[indice_mayor_edad])

# Insertar el nombre de la instructora en la posición 1
instructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, instructora)

# Contar cuántos aprendices tienen 18 años
conteo_18_anios = edades.count(18)
print(f"Hay {conteo_18_anios} aprendices de 18 años.")

# Agregar un aprendiz al final de la lista
nuevo_aprendiz = input("Ingrese el nombre del nuevo aprendiz: ")
aprendices.append(nuevo_aprendiz)

# Borrar el nombre de la instructora de la lista
if instructora in aprendices:
    aprendices.remove(instructora)

# Indicar un dato a buscar en la lista de aprendices
dato_a_buscar = input("Ingrese un nombre a buscar en la lista de aprendices: ")
if dato_a_buscar in aprendices:
    print(f"{dato_a_buscar} se encuentra en la lista de aprendices.")
else:
    print(f"{dato_a_buscar} no se encuentra en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista
print("Los primeros 10 aprendices son:", aprendices[:10])

# Mostrar los 10 últimos aprendices de la lista
print("Los 10 últimos aprendices son:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20
print("Elementos del 10 al 20 son:", aprendices[10:21])
