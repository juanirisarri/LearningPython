
# Conceptos vistos en de este ejemplo: 
#       - Encapsulación: se pone '__' antes del nombre (atributos/métodos que solo se pueden modificar/llamar desde dentro de la clase)
#       - Constructor  :  def __init__(self,input_a,input_b):


class Coche():
    
    # CONSTRUCTOR:

    def __init__(self,largoChasis,anchoChasis):
        self.largoChasis = largoChasis 
        self.anchoChasis = anchoChasis
        self.__ruedas = 4                   # se pone __ para que este atributo no se pueda modificar desde fuera de la clase
        self.__enMarcha = False 


    # ATRIBUTOS:
        # están dentro del constructor



    # MÉTODOS:

    def arrancar(self, ordenArrancar): 
        self.__enMarcha = ordenArrancar   # ordenArrancar: True o False

        if self.__enMarcha:
             checkeo = self.__checkeo_interno()    


        if (self.__enMarcha and checkeo):
            return "Checkeo positivo. El coche está en marcha"
        elif(self.__enMarcha and checkeo==False): 
            return "Chekeo negativo. No se puede arrancar el coche"
        else:
            return "El coche está parado"

    
    def estado(self):
        print("Ruedas: " , self.__ruedas)
        print("Largo: " , self.largoChasis)
        print("Ancho: " , self.anchoChasis)


    def __checkeo_interno(self):                # Método encapsulado. Solo se le puede llamar desde dentro de la clase 
        print("Realizando checkeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False
        
        



# Fin de la clase
#--------------------------------------------------------
#--------------------------------------------------------

miCoche = Coche(100,50)
print(" ")

print(miCoche.arrancar(False))
print(miCoche.arrancar(True))
miCoche.estado()

print(" ")

