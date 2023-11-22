aprendiz = []
edades = []

count = 0

while count < 3:
    aprendices = input("Ingresa el nombre del aprendiz o presiona enter para finalizar el programa: ")
    if aprendices == "":
        break
    edad = int(input("Ingresa la edad del aprendiz: "))
    aprendiz.append(aprendices)
    edades.append(edad)
    
    count += 1

print("Lista de aprendices:")
for nombre, edadd in zip(aprendiz, edades):
    print(nombre,"Edad:", edad)
    
    
