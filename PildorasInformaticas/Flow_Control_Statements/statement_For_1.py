
# for VARIABLE in ELEMENT:
#   ELEMENT puede ser tupla, lista, cadena de texto, ...


print(" ")
for i in [1,"Hola",True]:       # En este caso se recorre una lista 
    print(i)

print("---------------")

for i in (2.6,"Adios",False):     # En este caso se recorre una tupla 
    print(i, end=" - ")           # Se especifica el tipo de end
print(" ")

print("---------------")

for i in "elIndiceRecorreEsteArray":
    print(i, end=" ")

print(" ")
print("---------------")
print(" ")