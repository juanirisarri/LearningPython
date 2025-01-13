
# Se definen con () :: miTupla = (e1,e2)
# Se puede prescindir de los paréntesis para definir la tupla (no recomendado)
# El primer índice es el 0 (Posición 1)

# Son listas inmutables (No se pueden modificar)  
# Son más rápidas de computar
# Pueden utilizarse como claves en un diccionario (las listas no)

# .count() :: cuenta el número de veces que aparece el elemento indicado

# len(miTupla)   :: devuelve el número de elememtos 

# elem in miTupla :: Da True si elem pertenece a miTupla. Si no da False

# miLista = list(miTupla)  :: Crea una lista con el contenido de la tupla
# miTupla = tuple(miLista) :: Crea una tupla con el contenido de la lista

# (a,b,c,d,e) = miTupla :: Desempaqueta la tupla en las variables 

miTupla = ("Juan", 13, 1, True,13)


print(" ")
print("A ----------------")
print(" ")
print(miTupla[0])
print( 13 in miTupla )
print(miTupla)
print(list(miTupla))
print(" ")
print("B ----------------")
print(" ")
print(miTupla.count(13))
print("length = ", len(miTupla))
print(" ")
print("C ----------------")
print(" ")
(a,b,c,d,e) = miTupla
print(a)
print(c)
print(" ")














