
# in :: revisa si una variable pertenece a un array

optativas = ("Mates", "Materiales", "Física",  "Química")

print(" ")
print("Asignaturas optativas: ")
print("Mates - Materiales - Física - Química")


asignatura = input("Elige tu optativa : ")

if asignatura in optativas:
    print("Has elegido: " + asignatura)
else:
    print("Esa asignatura no es válida")


print(" ")

