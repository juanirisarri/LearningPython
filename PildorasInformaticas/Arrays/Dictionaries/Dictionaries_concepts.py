
# Se definen con {} y con clave:valor ::  miDiccionario = { "Alemania":"Berlin", "Francia":"Paris", 1.52:2}
# Los elementos no están ordenados. No hay índices

# El valor y la clave puede ser de cualquier tipo (int, float, str, ...)

# Añadir nuevos elementos (sobreescribe si la clave ya existía) ::  miDiccionario[Clave] = valor

# Elimar elementos :: del miDiccionario[Clave]

# .keys()   :: Devuelve las llaves
# .values() :: Devuelve los valores
# len(miDiccionario) :: Devuelve el tamaño

miDiccionario = { "Alemania":"Berlin", "Francia":"Paris", 1.52:2}

miDiccionario["Italia"] = "a"
miDiccionario["Italia"] = True

del miDiccionario["Alemania"]

print(" ")
print("A ----------------")
print(" ")
print(miDiccionario["Francia"])
print(miDiccionario[1.52])
print(miDiccionario["Italia"])
print(" ")
print("B ----------------")
print(" ")
print(miDiccionario)
print(" ")
print(" ")
print("C ----------------")
print(" ")
miTupla = ("Juan", 13,)
miDiccionario[miTupla[0]] = "El listo"

print(miDiccionario)

print(" ")
print("D ----------------")
print(" ")
hobbies = ["bucear", "comer"] # Es una tupla
miVida = {"Nombre":"Juan", "Edad":24, "hobbies":hobbies}
print(miVida)
print(" ")
print("E ----------------")
print(" ")
hobbies2 = ["bailar", "cantar"] # Es una tupla
suVida = {"Nombre":"Pepito", "Edad":12, "hobbies":hobbies2}
Vidas = {"Juan":miVida, "Pepito":suVida}
print(Vidas)
print(" ")
print(Vidas["Pepito"])
print(" ")
print("F ----------------")
print(" ")
print(suVida.keys())
print(Vidas["Pepito"].keys())
print(suVida.values())
print( len(miDiccionario))
print(" ")


















