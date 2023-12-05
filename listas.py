aprendices = []
edades = []

# Bucle para ingresar nombres y edades de aprendices
for i in range(31):
    nombre = input("Ingrese el nombre del aprendiz: ")
    edad = int(input("Ingrese la edad del aprendiz: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprime la lista de aprendices y edades
print("Aprendices:", aprendices)
print("Edades:", edades)

# Encuentra el aprendiz con la mayor edad y lo imprime
indiceMayorEdad = edades.index(max(edades))
mayorEdad = aprendices[indiceMayorEdad]
print("Aprendiz con la mayor edad:", mayorEdad)

# Ingresa el nombre del instructor en la posición 1 de la lista de aprendices
instructor = input("Ingresa el nombre del instructor: ")
aprendices.insert(1, instructor)

# Cuenta el número de aprendices que tienen 18 años e imprime el resultado
count18 = edades.count(18)
print("Número de aprendices que tienen 18 años:", count18)

# Ingresa el nombre de un aprendiz nuevo al final de la lista de aprendices
aprendizNuevo = input("Ingresa el nombre de un aprendiz nuevo: ")
aprendices.append(aprendizNuevo)

# Elimina al instructor de la lista de aprendices
aprendices.remove(instructor)

# Busca un dato en la lista de aprendices e imprime si está presente o no
datoBuscar = input("Ingresa un dato para buscar en la lista de aprendices: ")
if datoBuscar in aprendices:
    print(datoBuscar, "está presente en la lista.")
else:
    print(datoBuscar, "no está presente en la lista.")

# Imprime los primeros 10 aprendices de la lista
print("Primeros 10 aprendices:", aprendices[:10])

# Imprime los últimos 10 aprendices de la lista
print("Últimos 10 aprendices:", aprendices[-10:])

# Obtiene una muestra de elementos del índice 9 al 19 de la lista de aprendices
elementosMuestra = aprendices[9:20]
print("Elementos del 10 al 20:", elementosMuestra)
