
# Son como funciones pero generan el output de uno en uno

# Función tradicional:

def generaPares(limite):
    num = 1
    miLista = []

    while num < limite:
        miLista.append(num*2)
        num = num + 1

    return miLista 

print(" ")
print(generaPares(10))
print(" ")

print("---------------------")


# Generador:

def generaPares2(limite):
    num = 1

    while num < limite:
        
        yield num*2
        num = num + 1

generatorObject = generaPares2(10)  # es un objeto iterable! (se puede meter en un for)



print(" ")
print(next(generatorObject))
print(next(generatorObject))
print(" ")