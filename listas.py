aprendices = []
edades = []
for i in range(31):
    nombre = input("Ingrese el nombre del aprendiz: ")
    edad = int(input("Ingrese la edad del aprendiz: "))
    aprendices.append(nombre)
    edades.append(edad)

print("Aprendices:", aprendices)
print("Edades:", edades)

indiceMayorEdad = edades.index(max(edades))
mayorEdad = aprendices[indiceMayorEdad]
print("Aprendiz con la mayor edad:", mayorEdad)

instructor = input("Ingresa el nombre del instructor: ")
aprendices.insert(1, instructor)

count18 = edades.count(18)
print("Número de aprendices que tienen 18 anos:", count18)

aprendizNuevo = input("Ingresa el nombre de un aprendiz nuevo: ")
aprendices.append(aprendizNuevo)

aprendices.remove(instructor)

datoBuscar = input("Ingresa un dato para buscar en la lista de aprendices: ")
if datoBuscar in aprendices:
    print(datoBuscar, "esta presente en la lista.")
else:
    print(datoBuscar, "no esta presente en la lista.")

print("Primeros 10 aprendices:", aprendices[:10])


print("Últimos 10 aprendices:", aprendices[-10:])


elementosMuestra = aprendices[9:20]
print("Elementos del 10 al 20:", elementosMuestra)