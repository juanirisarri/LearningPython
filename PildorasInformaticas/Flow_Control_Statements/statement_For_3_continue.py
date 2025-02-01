
# continue :: hace que no se ejecute lo que tiene debajo y se vuelva al bucle for para seguir con la siguiente iteración


print(" ")


for letra in "Python":


    if letra == "h":
        continue                            # Se vuelve al for para seguir con la letra "o". No se ejecuta el print con letra == h 

    print("Viendo la letra: " + letra)


print(" ")
print("------------------")
print(" ")

nombre = "Juan Irisarri"
contador_caracteres = 0;

for letra in nombre:

    if letra == " ":            # Para que los espacios en blanco no se cuenten
        continue

    contador_caracteres = contador_caracteres + 1

print("Nº de caracteres: " + str(contador_caracteres))
print(" ")

