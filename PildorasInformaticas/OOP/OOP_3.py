
# Conceptos vistos en de este ejemplo: 
#       - Herencia: super y sub clase


class Vehiculos():   # Esta es la super clase (superclass) de la cual hereda coche

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

    pass


print("\n")

miMoto = Moto("Honda", "CBR")
miMoto.estado()
print("---------------------------------")
miMoto.acelerar()
miMoto.estado()

print("\n")











