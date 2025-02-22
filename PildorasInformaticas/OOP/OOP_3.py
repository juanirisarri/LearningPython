
# Conceptos vistos en de este ejemplo: 
#       - Herencia: super y sub clase
#       - Sobreescritura de métodos, atributos, ... (override)


class Vehiculos():   # Esta es la super clase (superclass) de la cual hereda moto

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False


    def arrancar(self):
        self.enMarcha = True


    def acelerar(self):
        self.acelera = True


    def frenar(self):
        self.frena = True


    def estado(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("En marcha: ", self.enMarcha)
        print("Acelera: ", self.acelera)
        print("Frena: ", self.frena)









class Moto(Vehiculos):  # Esta es una subclase (subclass) de Vehiculo (hereda de ella)
                        # Hereda los constructores, los atributos y métodos de su superclase
                        # Puede sobreescribir los constructores, los atributos y los métodos de su superclase
                        # Puede definir sus propios constructores, atributos y métodos 
    
    hcaballito = "No hago caballito"         # Atributo propio
    
    def caballito(self):                     # Metodo propio
        self.hcaballito = "Hago caballito"

    def estado(self):                        # sobreescribo este metodo heredado
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("En marcha: ", self.enMarcha)
        print("Acelera: ", self.acelera)
        print("Frena: ", self.frena)
        print(self.hcaballito)










# Fin de las clases
#--------------------------------------------------------
#--------------------------------------------------------



print("\n")

miMoto = Moto("Honda", "CBR")
miMoto.estado()
print("---------------------------------")
miMoto.acelerar()
miMoto.caballito()
miMoto.estado()

print("\n")











