
# Cuando hay un error en tiempo de ejecución se cae el programa en esa línea y no se ejecuta el código que está a continuación 
# Para evitar que se deje de ejecutar el código entero se pueden controlar las excepciones 

# ZeroDivisionError
# valueError

print(" ")
print("--------------------------")

def division(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        return "Error. No se puede dividir entre cero"
    except TypeError:
        return "Error. No se puede dividir. Se debe introducir un número"


try:
    a = division(8,0)
except NameError:
    print("Error. La variable introducida en la función no está definida")


try:
    print(a)
except NameError:
    print("Error. La variable introducida en el print no está definida")
print("--------------------------")






try:
    b = division(8,"hola")
except NameError:
    print("Error. La variable introducida en la función no está definida")

try:
    print(b)
except NameError:
    print("Error. La variable introducida en el print no está definida")
print("--------------------------")




try:
    c = division(8,x)
except NameError:
    print("Error. La variable introducida en la función no está definida")


try:
    print(c)
except NameError:
    print("Error. La variable introducida en el print no está definida")
print("--------------------------")


print(" ")