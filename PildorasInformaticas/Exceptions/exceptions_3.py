
# Con raise se pueden lanzar nuestras propias excepciones 
# Se pueden crear clases que sean excepciones como por ejemplo 'negativeAge' 

def evaluaEdad(edad):

    if edad<0:
        raise ValueError("La edad debe ser positiva")       # Puedes poner ValueError o la excepción que consideres.

    if edad<18:
        return "Eres menor de edad"
    elif edad<21:
        return "Eres mayor de edad salvo en EEUU"
    else:
        return "Eres mayor de edad en todos los paises"
    
print(" ")
print(evaluaEdad(-9))   # En este ejemplo salta una excepción en esta línea (y no la hemos controlado) por lo que no se ejecuta lo siguiente
print("Fin del código")
print(" ")

