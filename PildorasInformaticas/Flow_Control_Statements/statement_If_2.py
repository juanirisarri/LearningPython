
# mayor que :: >
# menor que :: <
# igual que :: ==

print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Introduce la nota: ")  # Leer nota por teclado (lo lee como un str)
nota_alumno = int(nota_alumno)


def evaluacion(nota):
    valoracion = "aprobado"

    if nota<5 : 
        valoracion = "suspenso"
    
    return valoracion

status = evaluacion(nota_alumno)

print(" ")
print(status)
print(" ")
