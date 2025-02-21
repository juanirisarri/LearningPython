
# Conceptos vistos en de este ejemplo:
#       - Atributos

class Coche():
    
    # No hay CONSTRUCTOR. Ver OOP_2.py

    #ATRIBUTOS:
    
    largoChasis = 250 # atributo común a todos los objetos de esta clase
    anchoChasis = 120
    ruedas = 4
    enMarcha = False


    #MÉTODOS:

    def arrancar(self): 
        # self :: Hace referencia al propio objeto
        self.enMarcha = True

      # No tiene inputs (salvo el propio objeto)
      # No tiene outputs



    def estado(self):
        if self.enMarcha == False:
            return("El coche está parado")
        else: 
            return("El coche ha arrancado")
        
      # No tiene inputs (salvo el propio objeto)
      # Tiene un output de tipo str



# Fin de la clase
#--------------------------------------------------------
#--------------------------------------------------------

miCoche = Coche()
print(" ")
print("El largo del coche es: " , miCoche.largoChasis)

if miCoche.enMarcha == False:
    print("El coche no ha arrancado")
else: 
    print("El coche está en marcha")



miCoche.arrancar()
print(miCoche.estado())

print(" ")

