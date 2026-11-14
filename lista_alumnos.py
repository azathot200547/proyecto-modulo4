print("--------BIENVENIDO AL PROGRAMA LISTA DE ALUMNOS--------")

class Alumno:
    def __init__(self, nombre, matricula, calificaciones):
        self.nombre = nombre
        self.matricula = matricula 
        self.calificaciones = calificaciones
    def calcular_promedio(self):
        suma = sum(self.calificaciones)
        cantidad = len(self.calificaciones)
        return suma / cantidad

alumnos = []
n = int(input("Cuantos alumnos vas ingresar: "))

for i in range(n):
    nombre = input(f"Nombre del estudiante {i + 1}: ")
    matricula = input(f"Matricula del estudiante {i + 1}: ")
    texto = input(f"Ingresa las calificaciones del estudiante: {i + 1} (separadas por espacio): ")
    calificaciones = [int(p) for p in texto.split()]
    alumnos.append(Alumno(nombre, matricula, calificaciones))

matriz = [alumno.calificaciones for alumno in alumnos]
print("Matriz de calificaciones: ")
for fila in matriz:
    print(fila)
    
promedios = []

for alumno in alumnos:
    promedio = alumno.calcular_promedio()
    promedios.append(promedio)
    print(f"{alumno.nombre} ({alumno.matricula}): promedio {promedio:.2f}")
    
mayor = max(promedios)
menor = min(promedios)
general = sum(promedios) / len(promedios)

print(f"Promedio Mayor: {mayor:.2f}")
print(f"Promedio Menor: {menor:.2f}")
print(f"Promedio General: {general:.2f}")

