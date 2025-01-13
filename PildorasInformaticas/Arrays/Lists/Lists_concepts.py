
# Se definen con []
# La posición '1' van con índice '0'

# .append() :: Añade elemento al final
# .extend() :: Añade varios elementos al final (concatena 2 listas)
# .pop()    :: Elimina elemento al final
# .insert() :: Inserta elemento en posición indicado. Desplaza los demás elementos
# .index()  :: Devuelve el índice del elemento indicado
# .remove() :: Elimina el elemento indicado

# "elem" in miLista :: devuelve 'True' si "elem" pertenece a 'miLista'. Si no, devuelve 'False'

# miLista3 = miLista1 + miLista2 :: une las dos listas
# miLista *3 :: Crea una nueva lista repitiendo miLista 3 veces



elem0 = "Pos1_Ind0"
elem1 = 1
elem2 = True
elem3 = "Antonio"

miLista = [elem0, elem1, elem2, elem3]

miLista.append("Sandra")        # Añade elemento al final
miLista.insert(2,"Insertado")   # Añade elemento en la posición 2 (el anterior elemento en posición 2 pasa a posición 3)

miLista.extend(["Ex1", "Ex2"])

print(" ")
print("A ----------------")
print(" ")
print("Marta" in miLista)
print("Sara" in miLista)
print(miLista.index("Sandra"))
print(miLista)
print(" ")
print("B ----------------")
print(" ")
print(miLista[0])
print(miLista[2])
print(miLista[3])
print(miLista[-2])      # elemento de la 2o posición empezando por la última
print(miLista[1:4])     # elementos de índices 1 al 4 (excluye el 2)
print(miLista[:2])      # 2 primeros elementos
print(miLista[-2:])     # 2 últimos elementos
print(miLista[3:])      # Desde el índice 3
print(" ")
print("C ----------------")
print(" ")
miLista.remove("Antonio")
miLista.pop()
print(miLista)
print(" ")
print("D ----------------")
print(" ")
miLista2 = miLista + ["e1", "e2"]
miLista3 = miLista *2
print(miLista2)
print(miLista3)
print(" ")
